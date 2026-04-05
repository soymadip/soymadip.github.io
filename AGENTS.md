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

Convert `code/` examples into concise, revision-friendly `notes/` pages.
Write in a direct, practical tone, fix obvious issues, and avoid changing the original intent.

## Workflow

- When asked to write notes, compare source code and existing notes in the same folder first; then write, update, or delete note files to reflect content changes.
- Review the last 3–4 notes in that directory when the source appears related.
- Identify the concept or topic taught by the source code.
- If the concept already exists, merge into that note instead of creating a duplicate.
- Prefer updating an existing note over creating a new one when the source clearly matches the same idea.
- Create a new note only when the source introduces a distinct concept or when no existing note covers the topic.
- Merge overlapping examples or closely related content into one stronger note when it makes sense.
- If all files/notes in a directory belong together, delete the directory and make one note.
- Keep the directory structure and sidebar order correct after merging.
- Split distinct subtopics into separate notes when needed.
- If a note already exists but has incomplete coverage, expand it instead of adding a small stub.
- If a source file is clearly an exercise, map it to the existing exercise note format and avoid adding a duplicate exercise.
- Answer source-file questions in the note, either inline or as a short FAQ.
- Keep root section `index.md` pages as overview pages only; do not add direct links to individual note files there.
- Use the language name for top-level note index pages, e.g. `Python`.

## Regular notes and metadata

Regular notes should focus on understanding a concept, not just solving a specific prompt.

- Use concept-driven titles and section headings.
- Start with a short "What to remember" list.
- Use short runnable examples and exact output blocks.
- Describe patterns and behavior, not commands.
- Avoid duplicate comments when the prose already explains the intent.
- Use real-world names like `pending_tasks`, `user_roles`, `visited_nodes`.
- Avoid pasting entire source files.
- Use callouts for tips and gotchas: `:::tip`, `:::note`, `:::warning`.
- Use Mermaid for conceptual diagrams; embed SVG/PNG for precise visuals.
- Use Mermaid, flowcharts, images, or SVGs when they help explain the concept.
- Use title case for callout and heading names.
- Add minimal boilerplate setup code when needed so the example is runnable as shown.
- Add visual aids only when they help clarify the concept.
- Keep lower-priority guidance as inline footnote-style text instead of a prominent box.
- Write enough explanation and examples to make the concept clear in practice, not just a tiny stub.
- Run the example in a real interpreter and verify the output block matches exactly, then add output to the note.
- Fold question-like comments into the note narrative or a brief FAQ.
- Use `<note no> - <name>.md` for filenames.
- Mirror the `code/` folder structure when practical.
- Prefer concept-driven filenames over narrative names.
- Keep numeric prefixes for ordering and use `sidebar_position` accordingly.
- If a merge creates a gap in numbering, do not renumber later notes; keep the next filename at its original number.
- `sidebar_position` may be a float if you need an intermediate ordering slot.
- Preserve the original code filename in `source_filename` when the note is normalized.
- Confirm the note filename, frontmatter, sidebar label, and index links are consistent.

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

Exercise notes follow all regular note rules, plus these differences:

- File names: `prefix. Exercise <exercise-number>: <exercise topic>.md`.
- Keep the ordering prefix separate from the exercise sequence.
- Titles/sidebar labels should use `Exercise <number>: <name>`.
- Visible H1 headings should use `Ex: <number> - <name>`.
- Use `## Problem`, `## Rules`, and `## Solution` sections.
- If the source has a docstring, use it as the `## Problem` prompt.
- Keep expected output visible before the solution.
- The solution may be hidden in `<details>`, but include a note like "Only view the solution after trying your best."
- Do not use `What to remember` if there is a dedicated `Rules` section.
- Use `source_filename` when the note filename is normalized.
- Confirm filenames, frontmatter, sidebar labels, and links are consistent.

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
