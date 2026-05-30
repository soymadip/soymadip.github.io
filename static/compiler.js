#!/bin/env bun

import { $ } from "bun";
import { join, dirname, basename } from "node:path";
import {
  readdirSync,
  statSync,
  existsSync,
  mkdirSync,
  rmSync,
  watch,
} from "node:fs";

// ------------------- Configuration ------------------

const REPO_URL = "https://github.com/soymadip/portosaur";
const REPO_BRANCH = "legacy";
const SYNC_ITEMS = ["static", "src", "blog", "notes"];

const COMPILER_DIR = join(process.cwd(), ".compiler");
const OUTPUT_DIR = join(process.cwd(), "build");

// ------------------- Console Colors ------------------
const C = {
  reset: "\x1b[0m",
  blue: "\x1b[34m",
  green: "\x1b[32m",
  red: "\x1b[31m",
  cyan: "\x1b[36m",
  bold: "\x1b[1m",
};

const mode = process.argv[2] === "dev" ? "dev" : "build";

// ------------------- Helpers -------------------

async function getChecksum(path) {
  const file = Bun.file(path);
  if (!(await file.exists())) return null;
  return Bun.hash(await file.arrayBuffer()).toString();
}

async function smartSync(src, dest, shouldDelete = true, logActivity = true) {
  if (!existsSync(src)) {
    if (shouldDelete && existsSync(dest)) {
      rmSync(dest, { recursive: true, force: true });
      if (logActivity)
        console.log(`${C.red}   🗑️ Removed: ${basename(dest)}${C.reset}`);
    }
    return;
  }

  const srcStat = statSync(src);
  const destExists = existsSync(dest);

  if (destExists && srcStat.isFile() !== statSync(dest).isFile()) {
    rmSync(dest, { recursive: true, force: true });
  }

  if (srcStat.isFile()) {
    const srcHash = await getChecksum(src);
    const destHash = await getChecksum(dest);

    if (srcHash !== destHash) {
      mkdirSync(dirname(dest), { recursive: true });
      await Bun.write(dest, Bun.file(src));
      if (logActivity)
        console.log(`${C.green}   ✅ Synced: ${basename(dest)}${C.reset}`);
    }
  } else {
    if (!existsSync(dest)) {
      mkdirSync(dest, { recursive: true });
    }
    const srcFiles = readdirSync(src);

    for (const file of srcFiles) {
      if (file === ".placeholder" || file === ".git") continue;
      await smartSync(
        join(src, file),
        join(dest, file),
        shouldDelete,
        logActivity,
      );
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
          if (logActivity)
            console.log(`${C.red}   🗑️ Removed: ${file}${C.reset}`);
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

async function cloneCompiler() {
  const proc = Bun.spawn(
    ["git", "clone", "--depth", "1", "-b", REPO_BRANCH, REPO_URL, COMPILER_DIR],
    {
      stdio: ["inherit", "inherit", "inherit"],
    },
  );

  const exitCode = await proc.exited;

  if (exitCode !== 0) {
    throw new Error(
      `Failed to clone compiler repository. Exit code: ${exitCode}`,
    );
  }
}

// -------------------- Main Logic ------------------

console.log(
  `${C.blue}${C.bold}>>> Portosaurus Engine [Mode: ${mode.toUpperCase()}]${C.reset}`,
);

// Prepare Compiler
const isGitRepo = existsSync(join(COMPILER_DIR, ".git"));

if (isGitRepo) {
  console.log(`${C.cyan}>>> Updating compiler...${C.reset}`);
  try {
    await $`git -C ${COMPILER_DIR} pull origin ${REPO_BRANCH}`.quiet();
  } catch (e) {
    console.log(`${C.red}>>> Pull failed, performing clean clone...${C.reset}`);
    rmSync(COMPILER_DIR, { recursive: true, force: true });
    await cloneCompiler();
  }
} else {
  console.log(
    `${C.cyan}>>> Compiler directory not found or invalid, performing clean clone...${C.reset}`,
  );
  if (existsSync(COMPILER_DIR)) {
    rmSync(COMPILER_DIR, { recursive: true, force: true });
  }
  await cloneCompiler();
}

// Sync Content
console.log(`${C.blue}>>> Syncing content...${C.reset}`);

for (const item of SYNC_ITEMS) {
  const shouldDelete = !["src", "static"].includes(item);
  await smartSync(
    join(process.cwd(), item),
    join(COMPILER_DIR, item),
    shouldDelete,
    false, // quiet for initial sync
  );
}

// Config Management
const localConfigPath = join(process.cwd(), "config.js");
const compilerConfigPath = join(COMPILER_DIR, "config.js");

if (existsSync(localConfigPath)) {
  await Bun.write(compilerConfigPath, Bun.file(localConfigPath));

  let repoName = process.env._REPO_NAME;
  let repoOwner = process.env._REPO_OWNER;

  let siteUrl, sitePath;

  if (!repoName || !repoOwner) {
    if (mode === "build" && !process.env.CI) {
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
}

// Install dependencies
console.log(`${C.blue}>>> Installing dependencies...${C.reset}`);
try {
  await $`cd ${COMPILER_DIR} && bun install`.quiet();
} catch (err) {
  console.error(
    `${C.red}❌ Failed to install dependencies in .compiler${C.reset}`,
  );
  process.exit(1);
}

// -------------------- Execution Phase ------------------

if (mode === "build") {
  console.log(`\n${C.blue}>>> Compiling Portosaurus site...${C.reset}\n`);

  try {
    const proc = Bun.spawn(
      ["bun", "--bun", "x", "docusaurus", "build", "--out-dir", OUTPUT_DIR],
      {
        cwd: COMPILER_DIR,
        stdio: ["inherit", "inherit", "inherit"],
      },
    );
    const exitCode = await proc.exited;

    if (exitCode !== 0) {
      throw new Error(`Build process exited with code ${exitCode}`);
    }
  } catch (err) {
    console.error(`${C.red}❌ Build failed: ${err.message}${C.reset}`);
    process.exit(1);
  }

  console.log(
    `\n${C.green}${C.bold}>>> Build completed successfully.${C.reset}\n`,
  );
} else if (mode === "dev") {
  console.log(
    `\n${C.green}${C.bold}>>> Starting Development Server...${C.reset}\n`,
  );

  for (const item of SYNC_ITEMS) {
    const itemPath = join(process.cwd(), item);
    if (!existsSync(itemPath)) continue;

    console.log(`${C.cyan}    Watching: ${item}/${C.reset}`);

    try {
      watch(itemPath, { recursive: true }, async (event, filename) => {
        if (!filename) return;

        // Exclude some internal files if needed
        if (filename.includes(".git") || filename === ".placeholder") return;

        const srcPath = join(itemPath, filename);
        const destPath = join(COMPILER_DIR, item, filename);

        if (existsSync(srcPath)) {
          if (statSync(srcPath).isFile()) {
            mkdirSync(dirname(destPath), { recursive: true });
            await Bun.write(destPath, Bun.file(srcPath));
            console.log();
            console.log(`${C.green} 🔄 Synced: ${item}/${filename}${C.reset}`);
          }
        } else {
          if (existsSync(destPath)) {
            rmSync(destPath, { recursive: true, force: true });
            console.log(`${C.red} 🗑️ Removed: ${item}/${filename}${C.reset}`);
          }
        }
      });
    } catch (e) {
      console.log(
        `${C.red}Warning: Native recursive watch failed for ${item}. Updates might not sync automatically.${C.reset}`,
      );
    }
  }

  const proc = Bun.spawn(
    ["bun", "--bun", "x", "docusaurus", "start", "--host", "0.0.0.0"],
    {
      cwd: COMPILER_DIR,
      stdio: ["inherit", "inherit", "inherit"],
    },
  );

  await proc.exited;
}
