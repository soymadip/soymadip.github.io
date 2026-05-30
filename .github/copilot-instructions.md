---
name: writing-agent
---

# Instructions

## What this repository is

This repo is a personal website built with Portosaur(https://gitlab.com/soymadip/portosaur).

Important locations:

- `config.js` — Portosaur configuration.
- `blog/` — posts and updates.
- `notes/` — revision notes, exercises.
- `static/code/` — source examples to convert into notes.
- `mise.toml` — pinned local tool versions.

## Role

Convert `static/code/` examples into concise `notes/` pages targeted at an **intermediate audience** (e.g., someone who knows basics or has a background in languages like C). Write in a direct, simple, and practical tone. Use first-person plural ("we", "our") rather than second-person ("you", "your").

- Trigger Phrase Behavior: When the user says "write notes", start the notes job following this document's workflow automatically, Pause and use the ask_user tool only for ambiguous scope or design choices.

## Workflow (Scan, Compare, Merge)

1. Run `git status` to find changed or new files in `static/code/`.
2. Compare with existing notes in the relevant `notes/` folder. Review the last 3–4 notes(or ideally all notes in the topic dir) to check if the topic is already covered.
3. **Merge first** — expand existing notes before creating new ones. Create a new note only if the source introduces a distinct concept.
4. Renumber local siblings to maintain a gap-free sequence after any merge or addition.

### Topic Folder Pattern

- Topic **has exercises** → create a folder `<number> - <name>/` with:
  - `index.mdx` — theory, no `sidebar_position`
  - exercise files inside the folder
- Topic **has no exercises** → standalone file `<number> - <name>.mdxx`
- Do not change code files unless a filename change is needed or explicitly asked. Code filenames shouldn't contain any spaces, special characters, in this case rename.

### Visual Example

```text
notes/python/5 - Functions/
├── index.mdx
├── 5.1 - basics/
│   ├── index.mdx
│   └── 5.1.1 - Exercise 19.mdx
├── 5.2 - scope/
│   ├── index.mdx
│   └── 5.2.1 - Exercise 20.mdx
└── 5.3 - recursion.mdx
```

### Additional Rules

- **Source Footnote:** End every note with a `SourcePreview` component.
  - Single file: `<SrcPv href="/code/<slugified-path>/<filename>" label="<original-filename>.<ext>" />`
  - Multiple files: `<SrcPv sources={[{ path: "/code/...", label: "..." }, ...]} />`
  - Keep original filename in `label`.
- **Answer Questions:** If the source has comments like `# why this?` or `# ...?`, answer them in the note. Never leave them unaddressed.
- **Respect Placeholders:** If source has `# TBD` or `# Will do later` or any comment/docstring indicating to do later, skip that section entirely.
- **Index Pages:** Top-level language `index.mdx` files are the **only** files that use `sidebar_position`. Section index pages get a short intro explaining the topic.
- **Cleanup Pass**: When normalizing notes, fix `source_filename` typos.

## Regular Notes

### Frontmatter (Mandatory)

All string values in double quotes.

```yaml
id: "hyphenated-unique-id" # in language-level indexes, it should be language-name
title: "Title Case Title"
description: "One-line summary." # must
source_filename: "original-filename.py"
# sidebar_position: only on language-level index.mdx
# sidebar_title: optional, if sidebar label should differ from title
```

### Content Rules

- **Before code:** Explain the intent and the "why". Integrate key takeaways into the narrative — no separate "What to Remember" section.
- **After code:** Point out nuances or performance notes.
- **Verification:** Run every code block with `uv run <file>.py` and show exact output.
- Always use Title Case for all headings. No syntax or code in headings.
- Use Docusaurus callouts (`:::tip`, `:::note`, `:::warning`) with Title Case labels.
- No `sidebar_position` in individual notes or sub-section index files.
- Sanitize filenames: replace `:` with `-`.

## Exercise Notes

Follow all regular note rules, plus:

- **Filename:** `<number> - Exercise <number> - <name>.mdx`
- **H1:** `Ex <number>: <name>` (no syntax in heading)
- **Sections:**
  - `## Problem` — task description, usually from source docstring
  - `## Rules` — constraints and requirements
  - `## Boilerplate` — starter code with subtext: `_Copy below code and paste to your IDE for head start._`, running the file should output exactly like given in expected output.
  - `## Expected Output` — exact output in a code block, verified by running the solution
  - Solution inside a `<details>` block with _Only view the solution after trying your best_ warning. Reasoning inside a Details block inside the solution. No output inside the solution block.

## Language-Specific Guidance

### Python

- Run files with `uv run <file>.py`.
- Use Python 3.13+ syntax with type hints.
- Mention version limits only when a feature is unsupported in <=3.13.

### JavaScript / TypeScript

- Run files with `bun`.
- Promote Es module over commonjs
