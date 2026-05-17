#!/bin/env bun

import { $ } from "bun";
import { join, dirname, basename } from "node:path";
import { readdirSync, statSync, existsSync, mkdirSync, rmSync } from "node:fs";

// ------------------- Configuration ------------------

const REPO_URL = "https://github.com/soymadip/portosaur";
const SYNC_ITEMS = ["static", "src", "blog", "notes"];

const COMPILER_DIR = join(process.cwd(), ".compiler");
const OUTPUT_DIR = join(process.cwd(), "build");

let contentChanged = false; // Tracks local modifications
let compilerChanged = false; // Tracks Portosaurus engine updates

// ------------------- Console Colors ------------------
const C = {
  reset: "\x1b[0m",
  blue: "\x1b[34m",
  green: "\x1b[32m",
  red: "\x1b[31m",
  cyan: "\x1b[36m",
  bold: "\x1b[1m",
};

// ------------------- Helpers -------------------

async function getChecksum(path) {
  const file = Bun.file(path);
  if (!(await file.exists())) return null;
  return Bun.hash(await file.arrayBuffer()).toString();
}

async function smartSync(src, dest, shouldDelete = true) {
  if (!existsSync(src)) {
    if (shouldDelete && existsSync(dest)) {
      rmSync(dest, { recursive: true, force: true });
      console.log(`${C.red}   🗑️ Removed: ${basename(dest)}${C.reset}`);
      contentChanged = true;
    }
    return;
  }

  const srcStat = statSync(src);
  const destExists = existsSync(dest);

  if (destExists && srcStat.isFile() !== statSync(dest).isFile()) {
    rmSync(dest, { recursive: true, force: true });
    contentChanged = true;
  }

  if (srcStat.isFile()) {
    const srcHash = await getChecksum(src);
    const destHash = await getChecksum(dest);

    if (srcHash !== destHash) {
      mkdirSync(dirname(dest), { recursive: true });
      await Bun.write(dest, Bun.file(src));
      console.log(`${C.green}   ✅ Synced: ${basename(dest)}${C.reset}`);
      contentChanged = true;
    }
  } else {
    if (!existsSync(dest)) {
      mkdirSync(dest, { recursive: true });
      contentChanged = true;
    }
    const srcFiles = readdirSync(src);

    for (const file of srcFiles) {
      if (file === ".placeholder" || file === ".git") continue;
      await smartSync(join(src, file), join(dest, file), shouldDelete);
    }

    if (shouldDelete && existsSync(dest)) {
      const destFiles = readdirSync(dest);
      for (const file of destFiles) {
        if (
          file === ".git" ||
          file === "index.mdx" ||
          file === "index.md" ||
          file === "authors.yml"
        )
          continue;

        if (!srcFiles.includes(file)) {
          rmSync(join(dest, file), { recursive: true, force: true });
          console.log(`${C.red}   🗑️ Removed: ${file}${C.reset}`);
          contentChanged = true;
        }
      }
    }
  }
}

async function replaceSiteConf(fieldPath, newValue, configPath, force = false) {
  const file = Bun.file(configPath);

  if (!(await file.exists())) return;

  let value = newValue;
  try {
    value = JSON.parse(newValue);
  } catch (_) {}

  const raw = await file.text();
  const exports = {};

  try {
    const script = raw.replace(/module\.exports\s*=/, "exports.usrConf =");
    eval(script);
  } catch (err) {
    console.error(`${C.red}❌ Parse failed: ${err.message}${C.reset}`);
    process.exit(1);
  }

  const obj = exports.usrConf;
  if (!obj) return;

  const parts = fieldPath.match(/[^.\[\]]+/g);
  let parent = obj;
  const lastKey = parts.pop();
  for (const part of parts) parent = parent[part] ||= {};

  if (parent[lastKey] === "auto" || force) {
    parent[lastKey] = value;
    await Bun.write(
      configPath,
      `exports.usrConf = ${JSON.stringify(obj, null, 2)};\n`,
    );
    console.log(`${C.cyan}✅ Config Updated: ${fieldPath}${C.reset}`);
  }
}

// -------------------- Main Logic ------------------

console.log(
  `${C.blue}${C.bold}>>> Starting Portosaurus Compilation...${C.reset}`,
);

// Prepare Compiler (Incremental)
if (!existsSync(COMPILER_DIR)) {
  console.log(`${C.cyan}>>> Cloning upstream repository...${C.reset}`);
  await $`git clone --depth 1 -b compiler ${REPO_URL} ${COMPILER_DIR}`;
  compilerChanged = true;
} else {
  console.log(`${C.cyan}>>> Updating existing compiler...${C.reset}`);

  try {
    const headBefore = (await $`git -C ${COMPILER_DIR} rev-parse HEAD`.quiet())
      .text()
      .trim();
    await $`git -C ${COMPILER_DIR} pull origin compiler`.quiet();
    const headAfter = (await $`git -C ${COMPILER_DIR} rev-parse HEAD`.quiet())
      .text()
      .trim();

    // Check if the git hash actually changed
    if (headBefore !== headAfter) {
      compilerChanged = true;
    }
  } catch (e) {
    console.log(`${C.red}>>> Pull failed, resetting compiler...${C.reset}`);

    rmSync(COMPILER_DIR, { recursive: true, force: true });
    await $`git clone --depth 1 -b compiler ${REPO_URL} ${COMPILER_DIR}`;
    compilerChanged = true;
  }
}

// Sync Content
console.log(`${C.blue}>>> Syncing content...${C.reset}`);

for (const item of SYNC_ITEMS) {
  // src and static should merge, not overwrite/delete internal compiler files
  const shouldDelete = !["src", "static"].includes(item);
  await smartSync(
    join(process.cwd(), item),
    join(COMPILER_DIR, item),
    shouldDelete,
  );
}

// Track config changes manually (to avoid infinite sync loops due to dynamic edits)
const localConfigPath = join(process.cwd(), "config.js");
const compilerConfigPath = join(COMPILER_DIR, "config.js");
const configHashPath = join(COMPILER_DIR, "config.hash");

const currentConfigHash = await getChecksum(localConfigPath);
const previousConfigHash = existsSync(configHashPath)
  ? await Bun.file(configHashPath).text()
  : "";

if (currentConfigHash !== previousConfigHash) {
  contentChanged = true;
  await Bun.write(compilerConfigPath, Bun.file(localConfigPath));

  let repoName = process.env._REPO_NAME;
  let repoOwner = process.env._REPO_OWNER;

  let siteUrl, sitePath;

  if (!repoName || !repoOwner) {
    if (!process.env.CI) {
      console.log(
        `${C.red}>>> Warning: _REPO_NAME or _REPO_OWNER not set. Defaulting to localhost.${C.reset}`,
      );
    }
    siteUrl = "http://localhost:5677";
    sitePath = "/";
  } else {
    repoName = repoName.trim();
    repoOwner = repoOwner.trim();
    const isGitLab = process.env.GITLAB_CI === "true";
    const domain = isGitLab ? "gitlab.io" : "github.io";
    siteUrl = `https://${repoOwner}.${domain}`;
    const pagesHost = `${repoOwner}.${domain}`.toLowerCase();
    sitePath = repoName.toLowerCase() === pagesHost ? "/" : `/${repoName}`;
  }

  await replaceSiteConf("site_url", siteUrl, compilerConfigPath);
  await replaceSiteConf("site_path", sitePath, compilerConfigPath);

  await Bun.write(configHashPath, currentConfigHash);
}

// Early Exit if nothing changed
if (!compilerChanged && !contentChanged && existsSync(OUTPUT_DIR)) {
  console.log(
    `\n${C.green}${C.bold}>>> Skipping compilation: No local or upstream changes detected.${C.reset}\n`,
  );
  process.exit(0);
}

// Build
console.log(`\n${C.blue}>>> Compiling Portosaurus site...${C.reset}\n`);

try {
  await $`cd ${COMPILER_DIR} && bun install`;
  await $`cd ${COMPILER_DIR} && bun run build`;
} catch (err) {
  console.error(`${C.red}❌ Build failed: ${err.message}${C.reset}`);
  process.exit(1);
}

// Copy Output
console.log(`\n${C.blue}>>> Updating build directory...${C.reset}`);
await smartSync(join(COMPILER_DIR, "build"), OUTPUT_DIR);

console.log(
  `\n${C.green}${C.bold}>>> Build completed successfully.${C.reset}\n`,
);
