# Instructions

## What this repository is

This repo is a personal website built with Portosaurus and Docusaurus.

Important locations

- `config.js` — main site configuration.
- `blog/` — posts and updates.
- `notes/` — documentation and revision notes.
- `code/` — source examples to convert into notes.
- `mise.toml` — pinned local tool versions.

## Your role

Convert `code/` examples into concise, revision-friendly `notes/` pages targeted at an **intermediate audience** (e.g., someone who knows basics or has a background in languages like C). Write in a direct, simple, and practical tone.

This guide explains how to turn each source example into a readable note. Follow the workflow first, then use the metadata and style rules to keep notes consistent and easy to review.

When i say "write notes", scan `code/` for changes, and write notes.

## **Workflow (Scan, Compare, Merge)**

- **Scan Before Writing:** When asked to write notes, compare source code with existing notes in the same folder. Review the last 3–4 notes to identify if the topic is already covered.
- **Merge-First Philosophy:** Do not create duplicate notes for the same concept.
  - If a concept exists, expand or merge it into the existing note.
  - If all notes in a directory belong together, consolidate them into one single note.
  - Create a new note only if the source introduces a distinct concept, not sub concept/part of existing notes.
- **Maintain Structure:** Always renumber notes and exercise prefixes to maintain a perfect, gap-free sequence in the sidebar.
  - If a merge creates a gap (e.g., merging 23 into 22), renumber all subsequent notes to fill the hole.
  - Exercises must update their numeric prefix to stay grouped with their parent topic (e.g., Exercise 24.5 becomes 23.5 if the topic moves from 24 to 23).
- **Source Footnote:** At the very end of every note and exercise, add a small italicized line: `---`\n _Source file: <original-filename>.py_.
- **Exercise Mapping:** Map source files that are clearly exercises to the standard exercise note format.
- **Answer Questions:** If the source file has questions or comments, fold the answers into the note narrative or a brief FAQ.
- **Index Pages:**
  - Keep top-level language index pages as landing pages (e.g., Python index).
  - Write section index pages with a short intro explaining the topic and a list of themes covered in that section.
  - Do not add direct links to individual note files in index pages.

## Regular notes and metadata

Regular notes should focus on idiomatic Python patterns and the "why" behind the code.

- **Intermediate Focus:** Assume the reader knows basic programming concepts (no "variables are boxes" analogies). Explain Python-specific behaviors, "Why/When" context, and "Pythonic vs. Anti-pattern" comparisons.
- **Wording & Headings:** Keep language simple and direct. Do not include syntax or code in headings (e.g., use `Slicing Syntax`, not `Slicing Syntax [start:stop]`).
- **Curated Content:** Do not list every possible built-in function; focus only on the commonly used ones.
- **Formatting:**
  - Use `<note no>. <name>.md` for filenames and mirror the `code/` folder structure.
  - Use numeric prefixes and `sidebar_position` (floats allowed) for ordering.
  - Preserve original code filenames in `source_filename`.
  - Use Docusaurus callouts (`:::tip`, `:::note`, `:::warning`) with Title Case names.
  - Keep lower-priority guidance as inline footnote-style text instead of a prominent box.
- **Content & Logic:**
  - **Before the code:** Explain the intent of the pattern.
  - **After the code:** Point out specific nuances, performance notes, or "clever" parts of the execution.
  - **Density:** Every sentence must add meaning; avoid duplicate comments if the prose already explains the intent.
  - Have a"What to remember" summary list.
  - Use real-world variable names and runnable examples with exact output blocks.
  - Use Mermaid, flowcharts, or SVGs, images when they clarify a concept.
- **Verification:**
  - _Run examples in a real interpreter to verify output blocks._
  - Fold question-like comments into the note narrative or a brief FAQ.
  - Write enough to make the concept clear in practice, not just a tiny stub.

### 2. Frontmatter (mandatory)

Every note must start with Docusaurus frontmatter. At minimum include:

- `id` — normalized, hyphenated unique identifier
- `title` — page title
- `description` — one-line summary
- `sidebar_label` — sidebar label
- `sidebar_position` — derived from the filename prefix
- Optional: `source_filename` — original code filename when normalized

Notes inside language-specific folders should keep titles concise; do not append a language suffix like ` — Python` or ` — JavaScript` when the note already lives in that language section.

- Keep titles concise inside language folders; don’t append `— Python` or similar.

## Exercise notes

Exercise notes follow all regular note rules, but focus on hands-on practice.

- **Filenames:** Use `<prefix>. Exercise <number>: <name>.md`.
- **Headings:** Use `Ex <number>: <name>` for the main H1. No syntax in headings.
- **Problem & Rules:**
  - Use `## Problem` to describe the task (often from the source docstring).
  - Use `## Rules` to list specific constraints or requirements.
- **Expected Output:** Always show the exact expected output _before_ the solution.
- **Solution & Reasoning:**
  - Place the code solution inside a hidden `<details>` block.
  - Add a "Only view the solution after trying your best" warning.
  - Include a "Details" block inside the solution to explain the reasoning, not as a separate visible section.
- **Metadata:** Use `source_filename` to link back to the original code.

## Language-specific guidance

Keep general rules first and add language-specific notes after.

- Check whether a syntax, method, or pattern is supported by current industry-standard versions.
- If it is not broadly supported, add a compatibility note.

### Python

- Use current Python syntax and typed examples when meaningful.
- Mention version limits only when a feature is unsupported in Python 3.12.
- If a Python source file uses newer syntax or idioms, note compatibility and support status.

### Other languages

- Add a subheading when a note uses platform- or language-specific idioms.
- Check support against broadly adopted versions of the language or framework.
- Document compatibility caveats for nonstandard or emerging syntax.
- Keep general guidance separate from language-specific conventions.
- Keep general guidance separate from language-specific conventions.

## Practical checklist

1. Locate the source file in `code/...`.
2. Read the source and existing notes in the folder.
3. Create `notes/.../<normalized-filename>.md`.
4. Add required frontmatter and `source_filename` if normalized.
5. Add a brief title, a small summary, and focused runnable examples.
6. Avoid duplicates; merge overlapping concepts.
7. Confirm sidebar labels, frontmatter, and links are consistent.

## When to ask for clarification

Ask when:

- you want to change site structure beyond content updates
- the change affects build or deployment behavior
- you want to rename many `code/` files
- you need to modify sidebar ordering or navigation
- you’re unsure about `sidebar_position` for a note without a leading number

## Local development

Use the project README and `mise.toml` for local preview and build commands.
iew and build commands.
