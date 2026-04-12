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

Convert `code/` examples into concise, `notes/` pages targeted at an **intermediate audience** (e.g., someone who knows basics or has a background in languages like C). Write in a direct, simple, and practical tone.

This guide explains how to turn each source example into a readable note. Follow the workflow first, then use the metadata and style rules to keep notes consistent and easy to review.

When I say "write notes", scan `src/code/` for changes, and write notes.

## **Workflow (Scan, Compare, Merge)**

- **Topic Folder Pattern:** Organize notes into topic-specific folders within their section only when the topic has associated exercises.
  - Each folder must contain an `index.md` which serves as the **Theory** and the "parent" page for that topic.
  - Folder names follow the `<number> - <name>` pattern (e.g., `5.1 - basics`).
  - **No `sidebar_position`** is used in these sub-folder `index.md` files; the folder's numeric prefix handles the ordering.
  - Exercises related to that topic must be placed **inside** the same folder as sub-pages.
  - If a topic has no exercises, a standalone numbered file such as `5.3 - recursion.md` is preferred over a folder.
  - Do not change code files unless filename change is needed or i told you to.

### **Visual Example (Ordering via Numbering)**

```text
notes/python/5 - Functions/
├── index.md                      <-- (ordered by '5' from dir name)
├── 5.1 - basics/                 <-- Section Folder (ordered by '5.1')
│   ├── index.md                  <-- Theory (No sidebar_position)
│   └── 5.1.1 - Exercise 19.md    <-- Exercise (No sidebar_position)
├── 5.2 - scope/                  <-- Section Folder (ordered by '5.2')
│   ├── index.md                  <-- Theory (No sidebar_position)
│   └── 5.2.1 - Exercise 20.md    <-- Exercise (No sidebar_position)
└── 5.3 - recursion.md            <-- Standalone Note (ordered by '5.3')
```

- **Scan Before Writing:** Compare source code with existing notes in the same folder. Review the last 3–4 notes to identify if the topic is already covered.
- **Merge-First Philosophy:** Do not create duplicate notes for the same concept.
  - If a concept exists, expand or merge it into the existing note.
  - If all notes in a directory belong together, consolidate them into one single note.
  - Create a new note only if the source introduces a distinct concept.
- **Maintain Structure:** Always renumber notes and prefixes to maintain a perfect, gap-free sequence in the sidebar.
  - If a merge creates a gap, renumber only the **local siblings** (notes/exercises within that same folder) to fill the hole.
  - Use sub-numbering (e.g., `5.1`, `5.1.1`) to ensure perfect ordering and easy tracking.
- **Source Footnote:** At the very end of every note and exercise, add a small italicized line: `---`\n _Source file: [<original-filename>.<ext>](/code/<slugified-path>/<slugified-filename>.<ext>)_.
  - **Slugification Rule:** Always slugify the URL path in the link (e.g., replace spaces with `-`, remove special characters, and lowercase). The visible label in brackets should remain the original filename for readability.
- **Exercise Mapping:** Map source files that are clearly exercises to the standard exercise note format.
- **Answer Questions:** If the source file has questions or comments (e.g., `# ...?` or `# why this?`), you MUST answer them. Fold the answers directly into the note narrative or use a brief FAQ if they are tangential. Never leave a source question unaddressed.
- **Index Pages:**
  - Keep top-level language index pages as landing pages (e.g., Python index). **These are the only files that use `sidebar_position`.**
  - Write section index pages with a short intro explaining the topic.

## Regular Notes and Metadata

Regular notes focus on idiomatic patterns and the "why" behind the code.

- **Intermediate Focus:** Assume the reader knows basic programming concepts. Explain language-specific behaviors and "Why/When" context.
- **Wording & Headings:** Keep language simple and direct. Do not include syntax or code in headings. **Always use Title Case for all headings.**
- **Formatting:**
  - **Directories:** `<number> - <name>/`
  - **Files:** `<number> - <name>.md` (except `index.md`)
  - **Index Files:** `index.md`
  - **Exercises:** `<number> - Exercise <number> - <name>.md`
  - **Sanitize filenames:** replace any colons `:` with hyphens `-`.
  - **Sidebar Ordering:** Use numeric prefixes in filenames and directories to control order. Do **not** use `sidebar_position` in the frontmatter of individual notes or sub-section index files.
  - Preserve original code filenames in `source_filename`.
  - Use Docusaurus callouts (`:::tip`, `:::note`, `:::warning`) with Title Case names.

- **Content & Logic:**
  - **Before the code:** Explain the intent of the pattern. Integrate key takeaways directly into this narrative; do not use a "What to Remember" or summary section.
  - **After the code:** Point out specific nuances or performance notes.
  - **Verification:** Run every example code block (`uv run <file>.py`) and show the exact output below it.

### **Frontmatter (Mandatory)**

Every note must start with Docusaurus frontmatter:

- **All string values must be wrapped in double quotes** (e.g., `title: "My Note"`).
- `id`: normalized, hyphenated unique identifier.
- `title`: page title in Title Case.
- `description`: one-line summary.
- `source_filename`: original code filename.
- `sidebar_position`: **(Only for language-level `index.md`)** numeric position.
- `sidebar_title`: optional. sidebar title to use (if wanna be different from title)

## Exercise Notes

Exercise notes follow all regular note rules, but focus on hands-on practice.

- **Filenames:** Use `<number> - Exercise <number> - <name>.md` (e.g., `5.1.1 - Exercise 19 - Student grading system.md`).
- **Headings:** Use `Ex <number>: <name>` for the main H1. No syntax in headings.
- **Problem & Rules:**
  - Use `## Problem` to describe the task (often from the source docstring).
  - Use `## Rules` to list specific constraints or requirements.
- **Boilerplate:**
  - Provide a boilerplate code block for the user to start with.
  - Use the heading: `## Boilerplate`
  - Subtext: `Copy below code and paste to your IDE for head start.`
  - Include a function stub and the test call.
- **Expected Output:**
  - Use the heading: `## Expected output`
  - Show the exact expected output of the test call in a Python code block.
  - Verify the output by running the solution code.
- **Solution & Reasoning:**
  - Place the code solution inside a hidden `<details>` block.
  - Add a "Only view the solution after trying your best" warning.
  - Do NOT include the output of the solution code here; it belongs in the `## Expected output` section.
  - Include a "Details" block inside the solution to explain the reasoning, not as a separate visible section.
- **Metadata:** Use `source_filename` to link back to the original code.

## Language-Specific Guidance

### Python

- **Use `uv` for running python files.**
- Use current Python syntax (3.12+) and typed examples.
- Mention version limits only when a feature is unsupported in 3.12.

### JavaScript/TypeScript

- Use `bun` to run files.

## Gemini

If you are Gemini, try not to use `generalist` sub-agent as much as possible.
