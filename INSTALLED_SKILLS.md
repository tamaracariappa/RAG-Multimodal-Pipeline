# Installed Skills Inventory

Audit of every skill reachable from this Claude Code environment.

- **Audit date:** 2026-10-13
- **Machine / profile:** Windows 11, user profile `C:\Users\tamar`
- **Project directory audited:** `D:\MultimodalRAG`
- **Method:** filesystem walk of every registered skill root, then a direct parse of each `SKILL.md` YAML frontmatter and its section headings. No skill in this document was listed from memory or from documentation.

---

## 1. Overview

**372 skills discovered** across the skill roots listed below.

| # | Location | Scope | Skills | Root path |
|---|----------|-------|-------:|-----------|
| 1 | Personal skills - Anthropic-managed, synced to this account | user | 9 | `C:\Users\tamar\.claude\skills\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71` |
| 2 | Plugin `caveman@caveman` (version 11ddc0c9813c) | user (plugin) | 7 | `C:\Users\tamar\.claude\plugins\cache\caveman\caveman\11ddc0c9813c\skills` |
| 3 | Plugin `ponytail@ponytail` v4.9.0 | user (plugin) | 6 | `C:\Users\tamar\.claude\plugins\cache\ponytail\ponytail\4.9.0\skills` |
| 4 | Plugin `claude-mem@thedotmack` v13.14.0 | user (plugin) | 19 | `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills` |
| 5 | Plugin `ui-ux-pro-max@ui-ux-pro-max-skill` v2.13.0 | user (plugin) | 7 | `C:\Users\tamar\.claude\plugins\cache\ui-ux-pro-max-skill\ui-ux-pro-max\2.13.0\.claude\skills` |
| 6 | Plugin `ecc@ecc` v2.2.0 | user (plugin) | 284 | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills` |
| 7 | Synced plugin `financial-analysis` | user (plugin) | 13 | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills` |
| 8 | Synced plugin `investment-banking` | user (plugin) | 9 | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\skills` |
| 9 | Synced plugin `fund-admin` | user (plugin) | 6 | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\fund-admin\skills` |
| 10 | Synced plugin `market-researcher` | user (plugin) | 5 | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\market-researcher\skills` |
| 11 | Synced plugin `meeting-prep-agent` | user (plugin) | 4 | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\meeting-prep-agent\skills` |
| 12 | Synced plugin `operations` | user (plugin) | 2 | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\operations\skills` |
| 13 | Synced plugin `claude-for-msft-365-install` | user (plugin) | 1 | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\claude-for-msft-365-install\.claude\skills` |
| - | Project-level `D:\MultimodalRAG\.claude\skills` | project | 0 | **does not exist** |
| - | `C:\Users\tamar\.claude\skills\learned` | user | 0 | exists but empty |

**Totals by origin**

| Origin | Skills |
|--------|-------:|
| `ecc` plugin | 284 |
| `claude-mem` plugin | 19 |
| `caveman` plugin | 7 |
| `ui-ux-pro-max` plugin | 7 |
| `ponytail` plugin | 6 |
| Personal synced (Anthropic-managed) | 9 |
| Synced plugins (7 bundles) | 40 |
| **Total** | **372** |

### Enabled plugins (from `~/.claude/settings.json`)

`caveman@caveman`, `ponytail@ponytail`, `claude-mem@thedotmack`, `ui-ux-pro-max@ui-ux-pro-max-skill`, `ecc@ecc` - all installed at user scope, all set to `true` in `enabledPlugins`, all confirmed present in `~/.claude/plugins/installed_plugins.json`.

Three further marketplaces are registered under `extraKnownMarketplaces` but **no plugin from them is installed or enabled**, so none of their skills exist on disk and none are counted above: `dev-skills` (wdm0006/python-skills), `watermarks-remover`, `academic-research-skills`.

Seven additional plugin bundles are present under `~/.claude/plugins/synced/` (organisation-synced): `financial-analysis`, `investment-banking`, `fund-admin`, `market-researcher`, `meeting-prep-agent`, `operations`, `claude-for-msft-365-install`. Each carries an `.in_use` marker, and two of them (`market-researcher`, `meeting-prep-agent`) also expose agents visible in this session, which is the evidence used here that the synced bundles are active.

---

## 2. Complete Skill Inventory

Each entry comes from that skill's own `SKILL.md`. Purpose text is condensed from the frontmatter `description` (full text is at the listed path). "Workflow sections" lists the `##` headings of the file, which is the skill's own procedure outline.

### Personal skills - Anthropic-managed, synced to this account

*9 skills.*

#### `docs`

- **Purpose:** docs (editable docs people share and comment on; the default for any document, named as a doc or not: a document, report, proposal, resume, cover letter, letter, contract, policy, form, template, worksheet, essay, handbook, guide, how-to, cheat sheet, SOP or other writing to keep, share, collaborate on, send, submit, print or sign; a doc exports to Word, PDF, Markdown or Google Docs, so needing a file to send, attach, upload, submit or print is no reason to pick Word, and a file nobody asked for ...
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** model-invoked by name (`docs`), no plugin namespace
- **Source:** `C:\Users\tamar\.claude\skills\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\docs\SKILL.md`

#### `docx`

- **Purpose:** Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx) or Word templates (.dotx). Triggers include: any mention of Microsoft Word Documents, such as 'Word doc', 'word document', '.docx', '.dotx', 'microsoft doc'. Also use when extracting or reorganizing content from .docx or .dotx files, inserting or replacing images in documents, find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word docume ...
- **When to use:** Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.
- **Workflow sections:** Creating with docx-js — gotchas / Verify the output / Editing existing documents / Comments / Dependencies
- **Dependencies / tools:** bundled: `scripts/`; files: `LICENSE.txt`
- **Invocation:** model-invoked by name (`docx`), no plugin namespace
- **Source:** `C:\Users\tamar\.claude\skills\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\docx\SKILL.md`

#### `google-workspace`

- **Purpose:** Read this before the first Google Drive, Docs, Sheets or Slides connector call whenever the task creates or changes a Google file. Use this skill whenever the user wants to create or change a Google Doc, Sheet or Slides file in their Google Drive. Triggers include: a request that names Google Docs, Sheets, Slides or Drive and asks to make, edit, format, copy or rename a file; a docs.google.com link with a request to change that file, even a one-line fix or suggested edits; and any follow-up chan ...
- **When to use:** Use this skill whenever the user wants to create or change a Google Doc, Sheet or Slides file in their Google Drive.
- **Workflow sections:** Read the reference before you touch the file / 1. Check the connectors before you start / 2. Rules for every file / 3. Drive, for all three apps / 4. Helper scripts / 5. Common failures across apps / 6. What the connectors can't do
- **Dependencies / tools:** bundled: `references/`, `scripts/`
- **Invocation:** model-invoked by name (`google-workspace`), no plugin namespace
- **Source:** `C:\Users\tamar\.claude\skills\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\google-workspace\SKILL.md`

#### `import-memory`

- **Purpose:** Import a memory export from another AI assistant into Claude's memory — conversationally, additively, and with the content treated as data.
- **Workflow sections:** Ground rules — read these first / Flow / Categories (output in this order): / Format: / Output: / Edge cases
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** model-invoked by name (`import-memory`), no plugin namespace
- **Source:** `C:\Users\tamar\.claude\skills\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\import-memory\SKILL.md`

#### `morning`

- **Purpose:** Render the user's morning brief as a styled HTML artifact, or set it up as a recurring weekday task. Use only when the user explicitly asks to run, see, or set up their morning brief, or if they invoke /morning by name. A question about their day, schedule, or calendar is not by itself a request for the brief; answer it directly instead.
- **Workflow sections:** Context / Setup / Gather / Sort / Write / Build / Verify / Voice
- **Dependencies / tools:** bundled: `assets/`
- **Invocation:** model-invoked by name (`morning`), no plugin namespace
- **Source:** `C:\Users\tamar\.claude\skills\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\morning\SKILL.md`

#### `pdf`

- **Purpose:** Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.
- **When to use:** Use this skill whenever the user wants to do anything with PDF files.
- **Workflow sections:** Overview / Quick Start / Python Libraries / Command-Line Tools / Common Tasks / Quick Reference / Next Steps
- **Dependencies / tools:** bundled: `scripts/`; files: `FORMS.md`, `LICENSE.txt`, `REFERENCE.md`
- **Invocation:** model-invoked by name (`pdf`), no plugin namespace
- **Source:** `C:\Users\tamar\.claude\skills\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\pdf\SKILL.md`

#### `pptx`

- **Purpose:** Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations as PowerPoint (.pptx) files; reading, parsing, or extracting text from any .pptx or .potx file (even if the extracted content will be used elsewhere, like in an email, summary, or creating a different type of slide deck); editing, modifying, or updating existing presentations; combining or splitting slide files; working with template ...
- **When to use:** Trigger whenever the user asks for a PowerPoint or .
- **Workflow sections:** Scripts / Creating with pptxgenjs — gotchas / Editing existing decks and templates / Deck content and flow / Design Ideas / QA (Required) / Converting to Images / Dependencies
- **Dependencies / tools:** bundled: `scripts/`; files: `LICENSE.txt`
- **Invocation:** model-invoked by name (`pptx`), no plugin namespace
- **Source:** `C:\Users\tamar\.claude\skills\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\pptx\SKILL.md`

#### `skill-creator`

- **Purpose:** Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.
- **When to use:** Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.
- **Workflow sections:** Communicating with the user / Creating a skill / Report structure / Executive summary / Key findings / Recommendations / Commit message format / Running and evaluating test cases
- **Dependencies / tools:** bundled: `assets/`, `references/`, `scripts/`; files: `LICENSE.txt`, `agents/`, `eval-viewer/`
- **Invocation:** model-invoked by name (`skill-creator`), no plugin namespace
- **Source:** `C:\Users\tamar\.claude\skills\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\skill-creator\SKILL.md`

#### `xlsx`

- **Purpose:** Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .xltx, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xl ...
- **When to use:** trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved.
- **Workflow sections:** Requirements for every output / Recalculate (mandatory whenever the file contains formulas) / Choosing formulas that survive verification / openpyxl gotchas / Financial models / Dependencies
- **Dependencies / tools:** bundled: `scripts/`; files: `LICENSE.txt`
- **Invocation:** model-invoked by name (`xlsx`), no plugin namespace
- **Source:** `C:\Users\tamar\.claude\skills\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\xlsx\SKILL.md`

---

### Plugin `caveman@caveman` (version 11ddc0c9813c)

*7 skills.*

#### `cavecrew`

- **Purpose:** > | Decision guide for delegating to caveman-style subagents. Tells the main | thread WHEN to spawn `cavecrew-investigator` (locate code), `cavecrew-builder` | (1-2 file edit), or `cavecrew-reviewer` (diff review) instead of doing the | work inline or using vanilla `Explore`. Subagent output is caveman-compressed | so the tool-result injected back into main context is ~60% smaller — main | context lasts longer across long sessions. | Trigger: "delegate to subagent", "use cavecrew", "spawn invest ...
- **Workflow sections:** When to use cavecrew vs alternatives / Why this exists (the real win) / Output contracts / Chaining patterns / What NOT to do / Auto-clarity (inherited)
- **Dependencies / tools:** files: `README.md`
- **Invocation:** `/caveman:cavecrew`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\caveman\caveman\11ddc0c9813c\skills\cavecrew\SKILL.md`

#### `caveman`

- **Purpose:** > | Ultra-compressed communication mode. Cuts output tokens 65% (measured) by speaking like caveman | while keeping full technical accuracy. Supports intensity levels: lite, full (default), ultra, | wenyan-lite, wenyan-full, wenyan-ultra. | Use when user says "caveman mode", "talk like caveman", "use caveman", "less tokens", | "be brief", or invokes /caveman. Also auto-triggers when token efficiency is requested.
- **When to use:** Use when user says "caveman mode", "talk like caveman", "use caveman", "less tokens", | "be brief", or invokes /caveman.
- **Workflow sections:** Persistence / Rules / Intensity / Auto-Clarity / Boundaries
- **Dependencies / tools:** files: `README.md`
- **Invocation:** `/caveman:caveman`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\caveman\caveman\11ddc0c9813c\skills\caveman\SKILL.md`

#### `caveman-commit`

- **Purpose:** > | Ultra-compressed commit message generator. Cuts noise from commit messages while preserving | intent and reasoning. Conventional Commits format. Subject ≤50 chars, body only when "why" | isn't obvious. Use when user says "write a commit", "commit message", "generate commit", | "/commit", or invokes /caveman-commit. Auto-triggers when staging changes.
- **When to use:** Use when user says "write a commit", "commit message", "generate commit", | "/commit", or invokes /caveman-commit.
- **Workflow sections:** Rules / Examples / Auto-Clarity / Boundaries
- **Dependencies / tools:** files: `README.md`
- **Invocation:** `/caveman:caveman-commit`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\caveman\caveman\11ddc0c9813c\skills\caveman-commit\SKILL.md`

#### `caveman-compress`

- **Purpose:** > | Compress natural language memory files (CLAUDE.md, todos, preferences) into caveman format | to save input tokens. Preserves all technical substance, code, URLs, and structure. | Compressed version overwrites the original file. Human-readable backup saved as FILE.original.md. | Trigger: /caveman-compress FILEPATH or "compress memory file"
- **Workflow sections:** Purpose / Trigger / Process / Compression Rules / Pattern / Boundaries
- **Dependencies / tools:** bundled: `scripts/`; files: `README.md`, `SECURITY.md`
- **Invocation:** `/caveman:caveman-compress`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\caveman\caveman\11ddc0c9813c\skills\caveman-compress\SKILL.md`

#### `caveman-help`

- **Purpose:** > | Quick-reference card for all caveman modes, skills, and commands. | One-shot display, not a persistent mode. Trigger: /caveman-help, | "caveman help", "what caveman commands", "how do I use caveman".
- **Workflow sections:** Modes / Skills / Deactivate / Language / Configure Default Mode / More
- **Dependencies / tools:** files: `README.md`
- **Invocation:** `/caveman:caveman-help`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\caveman\caveman\11ddc0c9813c\skills\caveman-help\SKILL.md`

#### `caveman-review`

- **Purpose:** > | Ultra-compressed code review comments. Cuts noise from PR feedback while preserving | the actionable signal. Each comment is one line: location, problem, fix. Use when user | says "review this PR", "code review", "review the diff", "/review", or invokes | /caveman-review. Auto-triggers when reviewing pull requests.
- **When to use:** Use when user | says "review this PR", "code review", "review the diff", "/review", or invokes | /caveman-review.
- **Workflow sections:** Rules / Examples / Auto-Clarity / Boundaries
- **Dependencies / tools:** files: `README.md`
- **Invocation:** `/caveman:caveman-review`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\caveman\caveman\11ddc0c9813c\skills\caveman-review\SKILL.md`

#### `caveman-stats`

- **Purpose:** > | Show real token usage and estimated savings for the current session. | Reads directly from the Claude Code session log — no AI estimation. | Triggers on /caveman-stats. Output is injected by the mode-tracker hook; | the model itself does not compute the numbers.
- **Dependencies / tools:** files: `README.md`
- **Invocation:** `/caveman:caveman-stats`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\caveman\caveman\11ddc0c9813c\skills\caveman-stats\SKILL.md`

---

### Plugin `ponytail@ponytail` v4.9.0

*6 skills.*

#### `ponytail`

- **Purpose:** > | Forces the laziest solution that actually works, simplest, shortest, most | minimal. Channels a senior dev who has seen everything: question whether the | task needs to exist at all (YAGNI), reach for the standard library before | custom code, native platform features before dependencies, one line before | fifty. Supports intensity levels: lite, full (default), ultra. Use on ANY | coding task: writing, adding, refactoring, fixing, reviewing, or designing | code, and choosing libraries or dep ...
- **When to use:** use whenever the user | says "ponytail", "be lazy", "lazy mode", "simplest solution", "minimal | solution", "yagni", "do less", or "shortest path", or complains about | over-engineering, bloat, boilerplate, or unnecessary dependencies.
- **Workflow sections:** Persistence / The ladder / Rules / Output / Intensity / When NOT to be lazy / Boundaries
- **Dependencies / tools:** argument-hint: `[lite|full|ultra]`
- **Invocation:** `/ponytail:ponytail`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ponytail\ponytail\4.9.0\skills\ponytail\SKILL.md`

#### `ponytail-audit`

- **Purpose:** > | Whole-repo audit for over-engineering. Like ponytail-review, but scans the | entire codebase instead of a diff: a ranked list of what to delete, simplify, | or replace with stdlib/native equivalents. Use when the user says "audit this | codebase", "audit for over-engineering", "what can I delete from this repo", | "find bloat", "ponytail-audit", or "/ponytail-audit". One-shot report, does | not apply fixes.
- **When to use:** Use when the user says "audit this | codebase", "audit for over-engineering", "what can I delete from this repo", | "find bloat", "ponytail-audit", or "/ponytail-audit".
- **Workflow sections:** Tags / Hunt / Output / Boundaries
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/ponytail:ponytail-audit`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ponytail\ponytail\4.9.0\skills\ponytail-audit\SKILL.md`

#### `ponytail-debt`

- **Purpose:** > | Harvest every `ponytail:` comment in the codebase into a debt ledger, so the | deliberate shortcuts and deferrals ponytail leaves behind get tracked instead | of rotting into "later means never". Use when the user says "ponytail debt", | "/ponytail-debt", "what did ponytail defer", "list the shortcuts", "ponytail | ledger", or "what did we mark to do later". One-shot report, changes nothing.
- **When to use:** Use when the user says "ponytail debt", | "/ponytail-debt", "what did ponytail defer", "list the shortcuts", "ponytail | ledger", or "what did we mark to do later".
- **Workflow sections:** Scan / Output / Boundaries
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/ponytail:ponytail-debt`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ponytail\ponytail\4.9.0\skills\ponytail-debt\SKILL.md`

#### `ponytail-gain`

- **Purpose:** > | Show ponytail's measured impact as a compact scoreboard: less code, less | cost, more speed, from the benchmark medians. One-shot display, not a | persistent mode, and not a per-repo number. Trigger: /ponytail-gain, | "ponytail gain", "what does ponytail save", "show ponytail impact", | "ponytail scoreboard".
- **Workflow sections:** Scoreboard / Honesty boundary / Boundaries
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/ponytail:ponytail-gain`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ponytail\ponytail\4.9.0\skills\ponytail-gain\SKILL.md`

#### `ponytail-help`

- **Purpose:** > | Quick-reference card for all ponytail modes, skills, and commands. | One-shot display, not a persistent mode. Trigger: /ponytail-help, | "ponytail help", "what ponytail commands", "how do I use ponytail".
- **Workflow sections:** Levels / Skills / Deactivate / Configure Default Mode / Update / More
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/ponytail:ponytail-help`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ponytail\ponytail\4.9.0\skills\ponytail-help\SKILL.md`

#### `ponytail-review`

- **Purpose:** > | Code review focused exclusively on over-engineering. Finds what to delete: | reinvented standard library, unneeded dependencies, speculative abstractions, | dead flexibility. One line per finding: location, what to cut, what replaces | it. Use when the user says "review for over-engineering", "what can we | delete", "is this over-engineered", "simplify review", or invokes | /ponytail-review. Complements correctness-focused review, this one only | hunts complexity.
- **When to use:** Use when the user says "review for over-engineering", "what can we | delete", "is this over-engineered", "simplify review", or invokes | /ponytail-review.
- **Workflow sections:** Format / Examples / Scoring / Boundaries
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/ponytail:ponytail-review`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ponytail\ponytail\4.9.0\skills\ponytail-review\SKILL.md`

---

### Plugin `claude-mem@thedotmack` v13.14.0

*19 skills.*

#### `babysit`

- **Purpose:** Watch a pull request or review cycle until it is ready to merge. Use when asked to babysit, monitor, or keep checking PR comments, reviews, and CI until all actionable issues are resolved.
- **When to use:** Use when asked to babysit, monitor, or keep checking PR comments, reviews, and CI until all actionable issues are resolved.
- **Workflow sections:** Workflow / GitHub CLI Checks / Operating Rules
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/claude-mem:babysit`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\babysit\SKILL.md`

#### `cloud-sync`

- **Purpose:** Set up or check claude-mem cloud sync with cmem.ai Pro. Use when the user says "set up cloud sync", "sync my memories", "cmem pro", "cloud backup", "sync status", or wants their memory database backed up or synced to their cmem.ai account.
- **When to use:** Use when the user says "set up cloud sync", "sync my memories", "cmem pro", "cloud backup", "sync status", or wants their memory database backed up or synced to their cmem.
- **Workflow sections:** 1. Check status / 2. Obtain the connection / 3. Write installed-client settings / 4. Restart and verify / 5. Report
- **Dependencies / tools:** allowed-tools: `- Bash | - Read | - AskUserQuestion`
- **Invocation:** `/claude-mem:cloud-sync`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\cloud-sync\SKILL.md`

#### `design-is`

- **Purpose:** Audit a design against Dieter Rams' ten "Good design is..." principles, then hand off a /make-plan prompt for one of three outcomes — new design, refine design, or redesign. Use when the user says "audit this design", "design review", "check this UI against Rams", "is this UI good", "critique this design", "design audit", or asks for a critique that should lead to a plan.
- **When to use:** Use when the user says "audit this design", "design review", "check this UI against Rams", "is this UI good", "critique this design", "design audit", or asks for a critique that should lead to a plan.
- **Workflow sections:** Do not use for / The Ten Principles (Dieter Rams) / Delegation Model / Output Artifacts / Phases / Key Principles (for the auditor) / Failure Modes to Prevent
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/claude-mem:design-is`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\design-is\SKILL.md`

#### `do`

- **Purpose:** Execute a phased implementation plan using subagents. Use when asked to execute, run, or carry out a plan — especially one created by make-plan.
- **When to use:** Use when asked to execute, run, or carry out a plan — especially one created by make-plan.
- **Workflow sections:** Execution Protocol / Failure Modes to Prevent
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/claude-mem:do`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\do\SKILL.md`

#### `how-it-works`

- **Purpose:** Explain how claude-mem captures observations, when memory injection kicks in, and where data lives. Use when the user asks "how does claude-mem work?" or "what is this thing doing?".
- **When to use:** Use when the user asks "how does claude-mem work?" or "what is this thing doing?".
- **Workflow sections:** What it does / When it kicks in / Where data lives
- **Dependencies / tools:** files: `onboarding-explainer.md`
- **Invocation:** `/claude-mem:how-it-works`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\how-it-works\SKILL.md`

#### `knowledge-agent`

- **Purpose:** Build and query AI-powered knowledge bases from claude-mem observations. Use when users want to create focused "brains" from their observation history, ask questions about past work patterns, or compile expertise on specific topics.
- **When to use:** Use when users want to create focused "brains" from their observation history, ask questions about past work patterns, or compile expertise on specific topics.
- **Workflow sections:** What Are Knowledge Agents? / Workflow / Tips / Maintenance
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/claude-mem:knowledge-agent`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\knowledge-agent\SKILL.md`

#### `learn-codebase`

- **Purpose:** Prime a codebase by reading every source file in full. Use when starting work on a new or unfamiliar project, or when the user asks to "learn the codebase", "read the codebase", "prime", or "get up to speed".
- **When to use:** Use when starting work on a new or unfamiliar project, or when the user asks to "learn the codebase", "read the codebase", "prime", or "get up to speed".
- **Workflow sections:** Note for Reviewers
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/claude-mem:learn-codebase`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\learn-codebase\SKILL.md`

#### `make-plan`

- **Purpose:** Create a detailed, phased implementation plan with documentation discovery. Use when asked to plan a feature, task, or multi-step implementation — especially before executing with do.
- **When to use:** Use when asked to plan a feature, task, or multi-step implementation — especially before executing with do.
- **Workflow sections:** Delegation Model / Plan Structure / Key Principles / Anti-Patterns to Prevent / See Also
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/claude-mem:make-plan`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\make-plan\SKILL.md`

#### `mem-search`

- **Purpose:** Search claude-mem's persistent cross-session memory database. Use when user asks "did we already solve this?", "how did we do X last time?", or needs work from previous sessions.
- **When to use:** Use when user asks "did we already solve this?", "how did we do X last time?", or needs work from previous sessions.
- **Workflow sections:** When to Use / 3-Layer Workflow (ALWAYS Follow) / Examples / Why This Workflow? / Knowledge Agents
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/claude-mem:mem-search`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\mem-search\SKILL.md`

#### `mode-creator`

- **Purpose:** Interactively create, install, activate, and verify custom claude-mem modes, including domain-specific observation types, concept tags, optional Telegram alerts, bot setup, worker restart, and startup-context verification. Use this whenever someone asks to customize what claude-mem remembers, create or change a mode, track domain-specific notes, add observation types or tags, or send Telegram notifications for particular memories—even if they do not use the word "mode.
- **Workflow sections:** Ground rules / 1. Open with the purpose / 2. Discover what is worth remembering / 3. Propose the mode / 4. Ask about Telegram alerts / 5. Draft, validate, and install / 6. Connect Telegram when needed / 7. Restart and prove the result
- **Dependencies / tools:** bundled: `references/`, `scripts/`; files: `evals/`
- **Invocation:** `/claude-mem:mode-creator`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\mode-creator\SKILL.md`

#### `oh-my-issues`

- **Purpose:** Cluster a GitHub issue backlog by root cause into a small set of plan-master issues, redirect children with a standardized comment, and bundle architectural-fix PRs that close clusters atomically. Use when an issue tracker has accumulated dozens of reports that share underlying defects, when asked to triage / consolidate / cluster / dedupe issues, when asked to build a plan series or roadmap from open issues, or when routing a new incoming bug into an existing plan.
- **When to use:** Use when an issue tracker has accumulated dozens of reports that share underlying defects, when asked to triage / consolidate / cluster / dedupe issues, when asked to build a plan series or roadmap from open issues, or when routing a new incoming bug into an existing plan.
- **Workflow sections:** Core principle / When to use / When NOT to use / Three modes / Naming a plan master / The standardized redirect comment / GitHub CLI primitives / Plan master body template
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/claude-mem:oh-my-issues`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\oh-my-issues\SKILL.md`

#### `pathfinder`

- **Purpose:** Map a codebase into feature-grouped flowcharts, identify duplicated concerns across features, and propose a unified architecture. Use when asked to "find the ideal path," unify duplicated systems, or audit architecture before a refactor. Emits a proposed unified flowchart plus per-system /make-plan prompts.
- **When to use:** Use when asked to "find the ideal path," unify duplicated systems, or audit architecture before a refactor.
- **Workflow sections:** Delegation Model / Output Artifacts / Phases / Key Principles / Failure Modes to Prevent
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/claude-mem:pathfinder`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\pathfinder\SKILL.md`

#### `smart-explore`

- **Purpose:** Token-optimized structural code search using tree-sitter AST parsing. Use instead of reading full files when you need to understand code structure, find functions, or explore a codebase efficiently.
- **Workflow sections:** Your Next Tool Call / 3-Layer Workflow / When to Use Standard Tools Instead / Workflow Examples / Token Economics / Language Support
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/claude-mem:smart-explore`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\smart-explore\SKILL.md`

#### `standup`

- **Purpose:** Facilitate a read-only standup across git worktrees, branches, or PRs to compare changes and produce one consolidation plan.
- **Workflow sections:** 1. Fill the room / 2. Open the room / 3. Run it as rounds / 4. Brief the human in plain language / CLI
- **Dependencies / tools:** allowed-tools: `- Bash | - Read | - Edit | - Task | - AskUserQuestion`; files: `agent-brief.md`, `standup.mjs`
- **Invocation:** `/claude-mem:standup`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\standup\SKILL.md`

#### `timeline-report`

- **Purpose:** Generate a "Journey Into [Project]" narrative report analyzing a project's entire development history from claude-mem's timeline. Use when asked for a timeline report, project history analysis, development journey, or full project report.
- **When to use:** Use when asked for a timeline report, project history analysis, development journey, or full project report.
- **Workflow sections:** When to Use / Prerequisites / Workflow / Required Sections / Writing Style / Important / Error Handling / Example
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/claude-mem:timeline-report`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\timeline-report\SKILL.md`

#### `version-bump`

- **Purpose:** Automated semantic versioning and release workflow for Claude Code plugins. Handles version increments across package.json, marketplace.json, plugin.json manifests, build verification, git tagging, GitHub releases, and changelog generation. NPM publishing (so `npx claude-mem@X.Y.Z` resolves) is handed off to the human maintainer, who raised npm security.
- **Workflow sections:** Preparation / Workflow / Checklist
- **Dependencies / tools:** bundled: `scripts/`
- **Invocation:** `/claude-mem:version-bump`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\version-bump\SKILL.md`

#### `weekly-digests`

- **Purpose:** Generate a serial week-by-week narrative digest of a project's full claude-mem timeline. Splits the timeline into per-ISO-week files, then runs one consecutive subagent per week — each receiving the prior week's carry-forward block — to produce one chapter per ISO week of data. Use when asked for "weekly digests", "week-by-week story", "serial timeline", or "narrative chapters" of a project's history.
- **When to use:** Use when asked for "weekly digests", "week-by-week story", "serial timeline", or "narrative chapters" of a project's history.
- **Workflow sections:** When to Use / Prerequisites / Workflow / Pipeline Discipline / Error Handling / Examples
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/claude-mem:weekly-digests`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\weekly-digests\SKILL.md`

#### `what-the`

- **Purpose:** What the? Use when the user wants a plain-English breakdown of something technical — the who, what, where, why, and when.
- **When to use:** Use when the user wants a plain-English breakdown of something technical — the who, what, where, why, and when.
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/claude-mem:what-the`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\what-the\SKILL.md`

#### `wowerpoint`

- **Purpose:** Turn one document into a kawaii NotebookLM slide-deck PDF. Use for "wowerpoint this", "make a deck about <file>", "turn this report into slides", or any request to render a single document as shareable narrative slides.
- **Workflow sections:** Triggers / Setup (one-time per machine) / Workflow / Output path / Share link (WOWerpoint Server) / The prompt / Subagent template (copy-paste, parameterize) / Failure modes
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/claude-mem:wowerpoint`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\wowerpoint\SKILL.md`

---

### Plugin `ui-ux-pro-max@ui-ux-pro-max-skill` v2.13.0

*7 skills.*

#### `banner-design`

- **Purpose:** Design banners for social media, ads, website heroes, creative assets, and print. Multiple art direction options with AI-generated visuals. Actions: design, create, generate banner. Platforms: Facebook, Twitter/X, LinkedIn, YouTube, Instagram, Google Display, website hero, print. Styles: minimalist, gradient, bold typography, photo-based, illustrated, geometric, retro, glassmorphism, 3D, neon, duotone, editorial, collage. Uses ui-ux-pro-max, frontend-design, ai-artist, ai-multimodal skills.
- **When to use:** - User requests banner, cover, or header design - Social media cover/header creation - Ad banner or display ad design - Website hero section visual design - Event/print banner design - Creative asset generation for campaigns
- **Workflow sections:** When to Activate / Prerequisites / Workflow / Banner Size Quick Reference / Art Direction Styles (Top 10) / Design Rules / Security
- **Dependencies / tools:** bundled: `references/`; argument-hint: `[platform] [style] [dimensions]`
- **Invocation:** `/ui-ux-pro-max:banner-design`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ui-ux-pro-max-skill\ui-ux-pro-max\2.13.0\.claude\skills\banner-design\SKILL.md`

#### `brand`

- **Purpose:** Brand voice, visual identity, messaging frameworks, asset management, brand consistency. Activate for branded content, tone of voice, marketing assets, brand compliance, style guides.
- **When to use:** - Brand voice definition and content tone guidance - Visual identity standards and style guide development - Messaging framework creation - Brand consistency review and audit - Asset organization, naming, and approval - Color palette management and typography specs
- **Workflow sections:** When to Use / Quick Start / Brand Sync Workflow / Subcommands / References / Scripts / Templates / Routing
- **Dependencies / tools:** bundled: `references/`, `scripts/`, `templates/`; argument-hint: `[update|review|create] [args]`
- **Invocation:** `/ui-ux-pro-max:brand`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ui-ux-pro-max-skill\ui-ux-pro-max\2.13.0\.claude\skills\brand\SKILL.md`

#### `design`

- **Purpose:** Comprehensive design skill: brand identity, design tokens, UI styling, logo generation (55 styles, Gemini AI), corporate identity program (50 deliverables, CIP mockups), HTML presentations (Chart.js), banner design (22 styles, social/ads/web/print), icon design (15 styles, SVG, Gemini 3.1 Pro), social photos (HTML→screenshot, multi-platform). Actions: design logo, create CIP, generate mockups, build slides, design banner, generate icon, create social photos, social media images, brand identity, ...
- **When to use:** - Brand identity, voice, assets - Design system tokens and specs - UI styling with shadcn/ui + Tailwind - Logo design and AI generation - Corporate identity program (CIP) deliverables - Presentations and pitch decks - Banner design for social media, ads, web, print - Social photos for Instagram, Fac
- **Workflow sections:** When to Use / Sub-skill Routing / Logo Design (Built-in) / CIP Design (Built-in) / Slides (Built-in) / Banner Design (Built-in) / Icon Design (Built-in) / Social Photos (Built-in)
- **Dependencies / tools:** bundled: `data/`, `references/`, `scripts/`; argument-hint: `[design-type] [context]`
- **Invocation:** `/ui-ux-pro-max:design`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ui-ux-pro-max-skill\ui-ux-pro-max\2.13.0\.claude\skills\design\SKILL.md`

#### `design-system`

- **Purpose:** Token architecture, component specifications, and slide generation. Three-layer tokens (primitive→semantic→component), CSS variables, spacing/typography scales, component specs, strategic slide creation. Use for design tokens, systematic design, brand-compliant presentations.
- **When to use:** - Design token creation - Component state definitions - CSS variable systems - Spacing/typography scales - Design-to-code handoff - Tailwind theme configuration - **Slide/presentation generation**
- **Workflow sections:** When to Use / Token Architecture / Quick Start / References / Component Spec Pattern / Scripts / Templates / Integration
- **Dependencies / tools:** bundled: `data/`, `references/`, `scripts/`, `templates/`; argument-hint: `[component or token]`
- **Invocation:** `/ui-ux-pro-max:design-system`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ui-ux-pro-max-skill\ui-ux-pro-max\2.13.0\.claude\skills\design-system\SKILL.md`

#### `slides`

- **Purpose:** Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas, and contextual slide strategies.
- **When to use:** - Marketing presentations and pitch decks - Data-driven slides with Chart.js - Strategic slide design with layout patterns - Copywriting-optimized presentation content
- **Workflow sections:** When to Use / Subcommands / References (Knowledge Base) / Routing
- **Dependencies / tools:** bundled: `references/`; argument-hint: `[topic] [slide-count]`
- **Invocation:** `/ui-ux-pro-max:slides`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ui-ux-pro-max-skill\ui-ux-pro-max\2.13.0\.claude\skills\slides\SKILL.md`

#### `ui-styling`

- **Purpose:** Create beautiful, accessible user interfaces with shadcn/ui components (built on Radix UI + Tailwind), Tailwind CSS utility-first styling, and canvas-based visual designs. Use when building user interfaces, implementing design systems, creating responsive layouts, adding accessible components (dialogs, dropdowns, forms, tables), customizing themes and colors, implementing dark mode, generating visual designs and posters, or establishing consistent styling patterns across applications.
- **When to use:** Use when building user interfaces, implementing design systems, creating responsive layouts, adding accessible components (dialogs, dropdowns, forms, tables), customizing themes and colors, implementing dark mode, generating visual designs and posters, or establishing consistent styling patterns acr ...
- **Workflow sections:** Reference / When to Use This Skill / Core Stack / Quick Start / Component Library Guide / Theme & Customization / Accessibility Patterns / Tailwind Utilities
- **Dependencies / tools:** bundled: `references/`, `scripts/`; files: `LICENSE.txt`, `canvas-fonts/`; argument-hint: `[component or layout]`
- **Invocation:** `/ui-ux-pro-max:ui-styling`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ui-ux-pro-max-skill\ui-ux-pro-max\2.13.0\.claude\skills\ui-styling\SKILL.md`

#### `ui-ux-pro-max`

- **Purpose:** UI/UX design intelligence for web and mobile. Searchable local database with 84 styles, 192 color palettes, 74 font pairings, 192 product types, 98 UX guidelines, 104 icon entries, 16 GSAP motion presets, and 25 chart types across 22 stacks (React, Next.js, Vue, Nuxt, Svelte, Astro, SwiftUI, React Native, Flutter, Tailwind, shadcn/ui, Jetpack Compose, Angular, Laravel, JavaFX, WPF, WinUI, Avalonia, Uno Platform, UWP, Three.js, and HTML/CSS). Use when designing, building, or reviewing UI: pages, ...
- **When to use:** Use when designing, building, or reviewing UI: pages, components, color schemes, typography, layout, accessibility, animation, or data visualization.
- **Workflow sections:** When to Apply / Rule Categories by Priority / Running the search tool / Workflow / If a search returns 0 results / Example Workflow / Output Formats / Tips for Better Results
- **Dependencies / tools:** bundled: `data/`, `references/`, `scripts/`
- **Invocation:** `/ui-ux-pro-max:ui-ux-pro-max`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ui-ux-pro-max-skill\ui-ux-pro-max\2.13.0\.claude\skills\ui-ux-pro-max\SKILL.md`

---

### Plugin `ecc@ecc` v2.2.0

*284 skills.*

ECC is a large operator layer. Its skills are grouped below by domain. That grouping is derived by this audit from skill names and descriptions - ECC's frontmatter carries no category field, only `metadata: origin: ECC`.

#### Language & framework patterns (69)

##### `android-clean-architecture`

- **Purpose:** Clean Architecture patterns for Android and Kotlin Multiplatform projects — module structure, dependency rules, UseCases, Repositories, and data layer patterns.
- **When to use:** - Structuring Android or KMP project modules - Implementing UseCases, Repositories, or DataSources - Designing data flow between layers (domain, data, presentation) - Setting up dependency injection with Koin or Hilt - Working with Room, SQLDelight, or Ktor in ...
- **Workflow sections:** When to Activate / Module Structure / Domain Layer / Data Layer / Dependency Injection / Error Handling / Convention Plugins (Gradle) / Anti-Patterns to Avoid
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:android-clean-architecture`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\android-clean-architecture\SKILL.md`

##### `angular-developer`

- **Purpose:** Generates Angular code and provides architectural guidance. Trigger when creating projects, components, or services, or for best practices on reactivity (signals, linkedSignal, resource), forms, dependency injection, routing, SSR, accessibility (ARIA), animations, styling (component styles, Tailwind CSS), testing, or CLI tooling.
- **When to use:** Trigger when creating projects, components, or services, or for best practices on reactivity (signals, linkedSignal, resource), forms, dependency injection, routing, SSR, accessibility (ARIA), animations, styling (component styles, Tailwind CSS), testing, or C ...
- **Workflow sections:** When to Activate / Creating New Projects / Components / Reactivity and Data Management / Forms / Dependency Injection / Angular Aria / Routing
- **Dependencies / tools:** bundled: `references/`; files: `.orphaned_at`
- **Invocation:** `/ecc:angular-developer`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\angular-developer\SKILL.md`

##### `backend-patterns`

- **Purpose:** Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, Express, and Next.js API routes.
- **When to use:** - Designing REST or GraphQL API endpoints - Implementing repository, service, or controller layers - Optimizing database queries (N+1, indexing, connection pooling) - Adding caching (Redis, in-memory, HTTP cache headers) - Setting up background jobs or async p ...
- **Workflow sections:** When to Activate / API Design Patterns / Database Patterns / Caching Strategies / Error Handling Patterns / Authentication & Authorization / Rate Limiting / Background Jobs & Queues
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:backend-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\backend-patterns\SKILL.md`

##### `bun-runtime`

- **Purpose:** Bun as runtime, package manager, bundler, and test runner. When to choose Bun vs Node, migration notes, and Vercel support.
- **Workflow sections:** When to Use / How It Works / Examples / Best Practices
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:bun-runtime`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\bun-runtime\SKILL.md`

##### `cisco-ios-patterns`

- **Purpose:** Cisco IOS and IOS-XE review patterns for show commands, config hierarchy, wildcard masks, ACL placement, interface hygiene, and safe change-window verification.
- **When to use:** - Reviewing IOS or IOS-XE configuration before a planned change. - Choosing read-only `show` commands for troubleshooting. - Checking ACL wildcard masks and interface direction. - Explaining global, interface, routing process, and line configuration modes. - V ...
- **Workflow sections:** When to Use / Operating Rules / Mode Reference / Read-Only Collection / Wildcard Masks / ACL Placement Review / Interface Hygiene / Change-Window Verification
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:cisco-ios-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\cisco-ios-patterns\SKILL.md`

##### `ck`

- **Purpose:** Persistent per-project memory for Claude Code. Auto-loads project context on session start, tracks sessions with git activity, and writes to native memory. Commands run deterministic Node.js scripts — behavior is consistent across model versions.
- **Workflow sections:** Data Layout / Commands / SessionStart Hook / Rules
- **Dependencies / tools:** files: `.orphaned_at`, `commands/`, `hooks/`
- **Invocation:** `/ecc:ck`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ck\SKILL.md`

##### `coding-standards`

- **Purpose:** Baseline cross-project coding conventions for naming, readability, immutability, and code-quality review. Use detailed frontend or backend skills for framework-specific patterns.
- **When to use:** - Starting a new project or module - Reviewing code for quality and maintainability - Refactoring existing code to follow conventions - Enforcing naming, formatting, or structural consistency - Setting up linting, formatting, or type-checking rules - Onboardin ...
- **Workflow sections:** When to Activate / Scope Boundaries / Code Quality Principles / TypeScript/JavaScript Standards / React Best Practices / API Design Standards / File Organization / Comments & Documentation
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:coding-standards`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\coding-standards\SKILL.md`

##### `compose-multiplatform-patterns`

- **Purpose:** Compose Multiplatform and Jetpack Compose patterns for KMP projects — state management, navigation, theming, performance, and platform-specific UI.
- **When to use:** - Building Compose UI (Jetpack Compose or Compose Multiplatform) - Managing UI state with ViewModels and Compose state - Implementing navigation in KMP or Android projects - Designing reusable composables and design systems - Optimizing recomposition and rende ...
- **Workflow sections:** When to Activate / State Management / Navigation / Composable Design / KMP Platform-Specific UI / Performance / Theming / Anti-Patterns to Avoid
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:compose-multiplatform-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\compose-multiplatform-patterns\SKILL.md`

##### `cpp-coding-standards`

- **Purpose:** C++ coding standards based on the C++ Core Guidelines (isocpp.github.io). Use when writing, reviewing, or refactoring C++ code to enforce modern, safe, and idiomatic practices.
- **When to use:** Use when writing, reviewing, or refactoring C++ code to enforce modern, safe, and idiomatic practices.
- **Workflow sections:** When to Use / Cross-Cutting Principles / Philosophy & Interfaces (P.*, I.*) / Functions (F.*) / Classes & Class Hierarchies (C.*) / Resource Management (R.*) / Expressions & Statements (ES.*) / Error Handling (E.*)
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:cpp-coding-standards`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\cpp-coding-standards\SKILL.md`

##### `dart-flutter-patterns`

- **Purpose:** Production-ready Dart and Flutter patterns covering null safety, immutable state, async composition, widget architecture, popular state management frameworks (BLoC, Riverpod, Provider), GoRouter navigation, Dio networking, Freezed code generation, and clean architecture.
- **Workflow sections:** When to Use / How It Works / Examples / 1. Null Safety Fundamentals / 2. Immutable State / 3. Async Composition / 4. Widget Architecture / 5. State Management: BLoC/Cubit
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:dart-flutter-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\dart-flutter-patterns\SKILL.md`

##### `deployment-patterns`

- **Purpose:** Deployment workflows, CI/CD pipeline patterns, Docker containerization, health checks, rollback strategies, and production readiness checklists for web applications.
- **When to use:** - Setting up CI/CD pipelines - Dockerizing an application - Planning deployment strategy (blue-green, canary, rolling) - Implementing health checks and readiness probes - Preparing for a production release - Configuring environment-specific settings
- **Workflow sections:** When to Activate / Deployment Strategies / Docker / CI/CD Pipeline / Health Checks / Environment Configuration / Rollback Strategy / Production Readiness Checklist
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:deployment-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\deployment-patterns\SKILL.md`

##### `django-celery`

- **Purpose:** Django + Celery async task patterns — configuration, task design, beat scheduling, retries, canvas workflows, monitoring, and testing. Use when adding background jobs, scheduled tasks, or async processing to a Django app.
- **When to use:** Use when adding background jobs, scheduled tasks, or async processing to a Django app.
- **Workflow sections:** When to Activate / Project Setup / Task Design Patterns / Calling Tasks / Beat Scheduling (Periodic Tasks) / Canvas: Chaining and Grouping Tasks / Error Handling and Dead Letter Queue / Testing Celery Tasks
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:django-celery`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\django-celery\SKILL.md`

##### `django-patterns`

- **Purpose:** Django architecture patterns, REST API design with DRF, ORM best practices, caching, signals, middleware, and production-grade Django apps.
- **When to use:** - Building Django web applications - Designing Django REST Framework APIs - Working with Django ORM and models - Setting up Django project structure - Implementing caching, signals, middleware
- **Workflow sections:** When to Activate / Project Structure / Model Design Patterns / Django REST Framework Patterns / Service Layer Pattern / Caching Strategies / Signals / Middleware
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:django-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\django-patterns\SKILL.md`

##### `docker-patterns`

- **Purpose:** Docker and Docker Compose patterns for local development, hardened CLI installer harnesses, container security, networking, volumes, and multi-service orchestration. Use when creating or reviewing Dockerfiles and Compose services, testing installers across Linux distributions, or planning accurate native macOS and Windows validation.
- **When to use:** Use when creating or reviewing Dockerfiles and Compose services, testing installers across Linux distributions, or planning accurate native macOS and Windows validation.
- **Workflow sections:** Docker Compose for Local Development / Networking / Volume Strategies / Container Security / Hardened CLI Installer Harnesses / .dockerignore / Debugging / Anti-Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:docker-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\docker-patterns\SKILL.md`

##### `dotnet-patterns`

- **Purpose:** Idiomatic C# and .NET patterns, conventions, dependency injection, async/await, and best practices for building robust, maintainable .NET applications.
- **When to use:** - Writing new C# code - Reviewing C# code - Refactoring existing .NET applications - Designing service architectures with ASP.NET Core
- **Workflow sections:** When to Activate / Core Principles / Async/Await Patterns / Options Pattern / Result Pattern / Repository Pattern with EF Core / Middleware and Pipeline / Minimal API Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:dotnet-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\dotnet-patterns\SKILL.md`

##### `error-handling`

- **Purpose:** Patterns for robust error handling across TypeScript, Python, and Go. Covers typed errors, error boundaries, retries, circuit breakers, and user-facing error messages.
- **When to use:** - Designing error types or exception hierarchies for a new module or service - Adding retry logic or circuit breakers for unreliable external dependencies - Reviewing API endpoints for missing error handling - Implementing user-facing error messages and feedba ...
- **Workflow sections:** When to Activate / Core Principles / TypeScript / JavaScript / Python / Go / Retry with Exponential Backoff / User-Facing Error Messages / Error Handling Checklist
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:error-handling`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\error-handling\SKILL.md`

##### `fastapi-patterns`

- **Purpose:** FastAPI best practices covering project structure, Pydantic v2 schemas, dependency injection, async handlers, authentication, authorization, transactional service layers, and testing with httpx and pytest.
- **Workflow sections:** Project Structure / App Factory and Lifespan / Configuration with pydantic-settings / Pydantic Schemas (v2) / Dependency Injection / Router and Endpoint Design / Service Layer / Testing with httpx and pytest
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:fastapi-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\fastapi-patterns\SKILL.md`

##### `flutter-dart-code-review`

- **Purpose:** Library-agnostic Flutter/Dart code review checklist covering widget best practices, state management patterns (BLoC, Riverpod, Provider, GetX, MobX, Signals), Dart idioms, performance, accessibility, security, and clean architecture.
- **Workflow sections:** 1. General Project Health / 2. Dart Language Pitfalls / 3. Widget Best Practices / 4. State Management (Library-Agnostic) / 5. Performance / 6. Testing / 7. Accessibility / 8. Platform-Specific Concerns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:flutter-dart-code-review`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\flutter-dart-code-review\SKILL.md`

##### `frontend-patterns`

- **Purpose:** Frontend development patterns for React, Next.js, state management, performance optimization, and UI best practices.
- **Workflow sections:** When to Activate / Component Patterns / Custom Hooks Patterns / State Management Patterns / Performance Optimization / Form Handling Patterns / Error Boundary Pattern / Animation Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:frontend-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\frontend-patterns\SKILL.md`

##### `generating-python-installer`

- **Purpose:** Commercial-grade Python installer expert for Windows: Nuitka extreme compilation, dist slimming, DLL footprint analysis, and Inno Setup packaging to ship the smallest, fastest installers. Use only for advanced packaging/optimization (minimal size, fast startup), not basic script-to-exe conversion. 中文触发：Nuitka 极限优化、Python 商业打包、极限编译 Python、dist 瘦身、DLL 分析、最小安装包、最快启动、商业级打包风格
- **Workflow sections:** When to Activate / How It Works / Examples / 核心理念 / 实战参考案例（生产级 PySide2 桌面应用，323 MB，含 OpenCV / Playwright） / 核心工作流 (Workflow) - WARNING: 严格执行 / Nuitka 极限优化编译（基于 参考项目经验） / 完整优化工作流
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:generating-python-installer`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\generating-python-installer\SKILL.md`

##### `gget`

- **Purpose:** gget CLI and Python workflow for quick genomic database queries, sequence lookup, BLAST-style searches, enrichment checks, and reproducible bioinformatics evidence logs.
- **Workflow sections:** When to Use / Installation / Basic Patterns / Common Modules / Quick Examples / Reproducibility Log / Review Checklist / References
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:gget`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\scientific-pkg-gget\SKILL.md`

##### `golang-patterns`

- **Purpose:** Idiomatic Go patterns, best practices, and conventions for building robust, efficient, and maintainable Go applications.
- **When to use:** - Writing new Go code - Reviewing Go code - Refactoring existing Go code - Designing Go packages/modules
- **Workflow sections:** When to Activate / Core Principles / Error Handling Patterns / Concurrency Patterns / Interface Design / Package Organization / Struct Design / Memory and Performance
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:golang-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\golang-patterns\SKILL.md`

##### `growth-log`

- **Purpose:** Use after a complex task, failure, or when reviewing what was learned. Teaches how to write growth logs that extract reusable patterns — not diary entries.
- **Workflow sections:** When to Activate / The Three Rules / Entry Template / [Title: the pattern, not the event] / Entry Types / Quality Checklist / Anti-Patterns / Storage
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:growth-log`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\growth-log\SKILL.md`

##### `healthcare-cdss-patterns`

- **Purpose:** Clinical Decision Support System (CDSS) development patterns. Drug interaction checking, dose validation, clinical scoring (NEWS2, qSOFA), alert severity classification, and integration into EMR workflows.
- **When to use:** - Implementing drug interaction checking - Building dose validation engines - Implementing clinical scoring systems (NEWS2, qSOFA, APACHE, GCS) - Designing alert systems for abnormal clinical values - Building medication order entry with safety checks - Integr ...
- **Workflow sections:** When to Use / How It Works / Examples
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:healthcare-cdss-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\healthcare-cdss-patterns\SKILL.md`

##### `healthcare-emr-patterns`

- **Purpose:** EMR/EHR development patterns for healthcare applications. Clinical safety, encounter workflows, prescription generation, clinical decision support integration, and accessibility-first UI for medical data entry.
- **Workflow sections:** When to Use / How It Works / Examples
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:healthcare-emr-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\healthcare-emr-patterns\SKILL.md`

##### `homelab-vlan-segmentation`

- **Purpose:** Segmenting home networks into VLANs for IoT, guest, trusted, and server traffic using UniFi, pfSense/OPNsense, and MikroTik — including switch trunk config, firewall rules, and wireless SSID mapping.
- **Workflow sections:** When to Use / How It Works / VLAN Design Template / Examples / UniFi Configuration / pfSense / OPNsense Configuration / MikroTik Configuration / Switch Trunk vs Access Ports
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:homelab-vlan-segmentation`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\homelab-vlan-segmentation\SKILL.md`

##### `hookify-rules`

- **Purpose:** This skill should be used when the user asks to create a hookify rule, write a hook rule, configure hookify, add a hookify rule, or needs guidance on hookify rule syntax and patterns.
- **Workflow sections:** Overview / Rule File Format / Event Type Guide / Pattern Writing Tips / File Organization / Commands / Quick Reference
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:hookify-rules`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\hookify-rules\SKILL.md`

##### `ito-inference`

- **Purpose:** Inspect the availability of model serving on a completed Itô compute booking and, when the canonical backend becomes available, hand off an explicitly confirmed serving manifest. Use after ito-compute has booked GPU nodes and the user asks for an OpenAI-compatible endpoint, ito-serve, hosted Kimi, or self-hosted open-weights inference. ECC implements no serving stack of its own.
- **Workflow sections:** Current production boundary / Required entitlement / Future CLI and API contract / Confirmation and execution gates / Lifecycle and recovery / Proposed backend stages
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:ito-inference`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ito-inference\SKILL.md`

##### `ito-training`

- **Purpose:** Run an ML training job on a completed Itô compute booking through the canonical Itô backend. Use after ito-compute has booked GPU nodes and the user wants pre-training, fine-tuning, or RL on that metal. Chains off a booking record; ECC implements no training stack of its own.
- **Workflow sections:** Prerequisite / Delegation / What the backend does (Layer 0.3) / Unavailable today
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:ito-training`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ito-training\SKILL.md`

##### `java-coding-standards`

- **Purpose:** Java coding standards for Spring Boot and Quarkus services: naming, immutability, Optional usage, streams, exceptions, generics, CDI, reactive patterns, and project layout. Automatically applies framework-specific conventions.
- **When to use:** - Writing or reviewing Java code in Spring Boot or Quarkus projects - Enforcing naming, immutability, or exception handling conventions - Working with records, sealed classes, or pattern matching (Java 17+) - Reviewing use of Optional, streams, or generics - S ...
- **Workflow sections:** When to Use / How It Works / Core Principles / Examples / Naming / Immutability / Optional Usage / Streams Best Practices
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:java-coding-standards`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\java-coding-standards\SKILL.md`

##### `jpa-patterns`

- **Purpose:** JPA/Hibernate patterns for entity design, relationships, query optimization, transactions, auditing, indexing, pagination, and pooling in Spring Boot.
- **When to use:** - Designing JPA entities and table mappings - Defining relationships (@OneToMany, @ManyToOne, @ManyToMany) - Optimizing queries (N+1 prevention, fetch strategies, projections) - Configuring transactions, auditing, or soft deletes - Setting up pagination, sorti ...
- **Workflow sections:** When to Activate / Entity Design / Relationships and N+1 Prevention / Repository Patterns / Transactions / Pagination / Indexing and Performance / Connection Pooling (HikariCP)
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:jpa-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\jpa-patterns\SKILL.md`

##### `kotlin-coroutines-flows`

- **Purpose:** Kotlin Coroutines and Flow patterns for Android and KMP — structured concurrency, Flow operators, StateFlow, error handling, and testing.
- **When to use:** - Writing async code with Kotlin coroutines - Using Flow, StateFlow, or SharedFlow for reactive data - Handling concurrent operations (parallel loading, debounce, retry) - Testing coroutines and Flows - Managing coroutine scopes and cancellation
- **Workflow sections:** When to Activate / Structured Concurrency / Flow Patterns / Dispatchers / Cancellation / Testing / Anti-Patterns to Avoid / References
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:kotlin-coroutines-flows`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\kotlin-coroutines-flows\SKILL.md`

##### `kotlin-exposed-patterns`

- **Purpose:** JetBrains Exposed ORM patterns including DSL queries, DAO pattern, transactions, HikariCP connection pooling, Flyway migrations, and repository pattern.
- **When to use:** - Setting up database access with Exposed - Writing SQL queries using Exposed DSL or DAO - Configuring connection pooling with HikariCP - Creating database migrations with Flyway - Implementing the repository pattern with Exposed - Handling JSON columns and co ...
- **Workflow sections:** When to Use / How It Works / Examples / Database Setup / Table Definitions / DSL Queries / DAO Pattern / Transactions
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:kotlin-exposed-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\kotlin-exposed-patterns\SKILL.md`

##### `kotlin-ktor-patterns`

- **Purpose:** Ktor server patterns including routing DSL, plugins, authentication, Koin DI, kotlinx.serialization, WebSockets, and testApplication testing.
- **When to use:** - Building Ktor HTTP servers - Configuring Ktor plugins (Auth, CORS, ContentNegotiation, StatusPages) - Implementing REST APIs with Ktor - Setting up dependency injection with Koin - Writing Ktor integration tests with testApplication - Working with WebSockets ...
- **Workflow sections:** When to Activate / Application Structure / Routing DSL / Content Negotiation & Serialization / Authentication / Status Pages (Error Handling) / CORS Configuration / Koin Dependency Injection
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:kotlin-ktor-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\kotlin-ktor-patterns\SKILL.md`

##### `kotlin-patterns`

- **Purpose:** Idiomatic Kotlin patterns, best practices, and conventions for building robust, efficient, and maintainable Kotlin applications with coroutines, null safety, and DSL builders.
- **When to use:** - Writing new Kotlin code - Reviewing Kotlin code - Refactoring existing Kotlin code - Designing Kotlin modules or libraries - Configuring Gradle Kotlin DSL builds
- **Workflow sections:** When to Use / How It Works / Examples / Core Principles / Sealed Classes and Interfaces / Scope Functions / Extension Functions / Coroutines
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:kotlin-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\kotlin-patterns\SKILL.md`

##### `kubernetes-patterns`

- **Purpose:** Kubernetes workload patterns, resource management, RBAC, probes, autoscaling, ConfigMap/Secret handling, and kubectl debugging for production-grade deployments.
- **When to use:** > Same as **When to Activate** above. This alias satisfies repo skill-format conventions. Use this skill any time you are writing, reviewing, or debugging Kubernetes YAML and workloads.
- **Workflow sections:** When to Activate / When to Use / How It Works / Examples / Core Workload Patterns / Probes — Liveness, Readiness, Startup / Services and Ingress / ConfigMaps and Secrets
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:kubernetes-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\kubernetes-patterns\SKILL.md`

##### `laravel-patterns`

- **Purpose:** Laravel architecture patterns, routing/controllers, Eloquent ORM, service layers, queues, events, caching, and API resources for production apps.
- **When to use:** - Building Laravel web applications or APIs - Structuring controllers, services, and domain logic - Working with Eloquent models and relationships - Designing APIs with resources and pagination - Adding queues, events, caching, and background jobs
- **Workflow sections:** When to Use / How It Works / Examples
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:laravel-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\laravel-patterns\SKILL.md`

##### `laravel-plugin-discovery`

- **Purpose:** Discover and evaluate Laravel packages via LaraPlugins.io MCP. Use when the user wants to find plugins, check package health, or assess Laravel/PHP compatibility.
- **When to use:** Use when the user wants to find plugins, check package health, or assess Laravel/PHP compatibility.
- **Workflow sections:** When to Use / MCP Requirement / MCP Tools / How It Works / Examples / Filtering Best Practices / Response Interpretation / Common Use Cases
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:laravel-plugin-discovery`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\laravel-plugin-discovery\SKILL.md`

##### `logistics-exception-management`

- **Purpose:** > | Codified expertise for handling freight exceptions, shipment delays, | damages, losses, and carrier disputes. Informed by logistics professionals | with 15+ years operational experience. Includes escalation protocols, | carrier-specific behaviors, claims procedures, and judgment frameworks. | Use when handling shipping exceptions, freight claims, delivery issues, | or carrier disputes.
- **When to use:** Use when handling shipping exceptions, freight claims, delivery issues, | or carrier disputes.
- **Workflow sections:** Role and Context / When to Use / How It Works / Examples / Core Knowledge / Decision Frameworks / Key Edge Cases / Communication Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:logistics-exception-management`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\logistics-exception-management\SKILL.md`

##### `mcp-server-patterns`

- **Purpose:** Build MCP servers with Node/TypeScript SDK — tools, resources, prompts, Zod validation, stdio vs Streamable HTTP. Use Context7 or official MCP docs for latest API.
- **When to use:** Use when: implementing a new MCP server, adding tools or resources, choosing stdio vs HTTP, upgrading the SDK, or debugging MCP registration and transport issues.
- **Workflow sections:** When to Use / How It Works / Examples / Best Practices / Official SDKs and Docs
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:mcp-server-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\mcp-server-patterns\SKILL.md`

##### `motion-advanced`

- **Purpose:** Advanced motion patterns for React / Next.js — drag & drop, gestures, text animations, SVG path drawing, custom hooks, imperative sequences (useAnimate), loaders, and the full API decision tree. Requires motion-foundations.
- **Workflow sections:** When to Activate / Outputs / Principles / Rules / Decision Guidance / Core Concepts / Code Examples / End-to-End Example
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:motion-advanced`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\motion-advanced\SKILL.md`

##### `motion-foundations`

- **Purpose:** Motion tokens, spring presets, performance rules, device adaptation, accessibility enforcement, and SSR safety for React / Next.js using motion/react. Foundation layer — all other motion skills depend on this.
- **When to use:** - Starting any animated component from scratch - Setting up tokens, spring presets, or easing values - Implementing `prefers-reduced-motion` support - Debugging hydration mismatches from animation initial states - Evaluating whether an animation should exist a ...
- **Workflow sections:** When to Activate / Outputs / Principles / Rules / Decision Guidance / Core Concepts / Code Examples / Constraints / Non-Goals
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:motion-foundations`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\motion-foundations\SKILL.md`

##### `motion-patterns`

- **Purpose:** Production-ready animation patterns for React / Next.js — button, modal, toast, stagger, page transitions, exit animations, scroll, and layout — built on motion-foundations tokens and springs.
- **When to use:** - Animating a button, card, modal, or toast notification - Building list entrances with stagger - Setting up page transitions in Next.js App Router - Adding entrance or exit animations to conditional content - Implementing scroll-reveal, scroll-linked progress ...
- **Workflow sections:** When to Activate / Outputs / Principles / Rules / Decision Guidance / Core Concepts / Code Examples / End-to-End Example
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:motion-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\motion-patterns\SKILL.md`

##### `mysql-patterns`

- **Purpose:** MySQL and MariaDB schema, query, indexing, transaction, replication, and connection-pool patterns for production backends.
- **Workflow sections:** Activation / Version Check / Schema Defaults / Indexing / Query Patterns / Transactions / Connection Pools / Diagnostics
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:mysql-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\mysql-patterns\SKILL.md`

##### `nestjs-patterns`

- **Purpose:** NestJS architecture patterns for modules, controllers, providers, DTO validation, guards, interceptors, config, and production-grade TypeScript backends.
- **When to use:** - Building NestJS APIs or services - Structuring modules, controllers, and providers - Adding DTO validation, guards, interceptors, or exception filters - Configuring environment-aware settings and database integrations - Testing NestJS units or HTTP endpoints
- **Workflow sections:** When to Activate / Project Structure / Bootstrap and Global Validation / Modules, Controllers, and Providers / DTOs and Validation / Auth, Guards, and Request Context / Exception Filters and Error Shape / Config and Environment Validation
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:nestjs-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\nestjs-patterns\SKILL.md`

##### `netmiko-ssh-automation`

- **Purpose:** Safe Python Netmiko patterns for read-only collection, bounded batch SSH, TextFSM parsing, guarded config changes, timeouts, and network automation error handling.
- **When to use:** - Collecting `show` command output across routers, switches, or firewalls. - Building a small audit script for interface, routing, or config evidence. - Adding timeouts and exception handling to network SSH scripts. - Parsing command output with TextFSM when a ...
- **Workflow sections:** When to Use / Safety Defaults / Read-Only Connection Pattern / Batch Collection / Structured Parsing / Guarded Config Pattern / Review Checklist / Anti-Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:netmiko-ssh-automation`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\netmiko-ssh-automation\SKILL.md`

##### `nextjs-turbopack`

- **Purpose:** Next.js 16+ and Turbopack — incremental bundling, FS caching, dev speed, and when to use Turbopack vs webpack.
- **Workflow sections:** When to Use / How It Works / Examples / Middleware File Naming / Best Practices
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:nextjs-turbopack`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\nextjs-turbopack\SKILL.md`

##### `nodejs-keccak256`

- **Purpose:** Prevent Ethereum hashing bugs in JavaScript and TypeScript. Node's sha3-256 is NIST SHA3, not Ethereum Keccak-256, and silently breaks selectors, signatures, storage slots, and address derivation.
- **When to use:** - Computing Ethereum function selectors or event topics - Building EIP-712, signature, Merkle, or storage-slot helpers in JS/TS - Reviewing any code that hashes Ethereum data with Node crypto directly
- **Workflow sections:** When to Use / How It Works / Examples / Rule
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:nodejs-keccak256`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\nodejs-keccak256\SKILL.md`

##### `nuxt4-patterns`

- **Purpose:** Nuxt 4 app patterns for hydration safety, performance, route rules, lazy loading, and SSR-safe data fetching with useFetch and useAsyncData.
- **When to use:** - Hydration mismatches between server HTML and client state - Route-level rendering decisions such as prerender, SWR, ISR, or client-only sections - Performance work around lazy loading, lazy hydration, or payload size - Page or component data fetching with `u ...
- **Workflow sections:** When to Activate / Hydration Safety / Data Fetching / Route Rules / Lazy Loading and Performance / Review Checklist
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:nuxt4-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\nuxt4-patterns\SKILL.md`

##### `perl-patterns`

- **Purpose:** Modern Perl 5.36+ idioms, best practices, and conventions for building robust, maintainable Perl applications.
- **When to use:** - Writing new Perl code or modules - Reviewing Perl code for idiom compliance - Refactoring legacy Perl to modern standards - Designing Perl module architecture - Migrating pre-5.36 code to modern Perl
- **Workflow sections:** When to Activate / How It Works / Core Principles / Error Handling / Modern OO with Moo / Regular Expressions / Data Structures / File I/O
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:perl-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\perl-patterns\SKILL.md`

##### `postgres-patterns`

- **Purpose:** PostgreSQL database patterns for query optimization, schema design, indexing, and security. Based on Supabase best practices.
- **When to use:** - Writing SQL queries or migrations - Designing database schemas - Troubleshooting slow queries - Implementing Row Level Security - Setting up connection pooling
- **Workflow sections:** When to Activate / Quick Reference / Related
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:postgres-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\postgres-patterns\SKILL.md`

##### `prisma-patterns`

- **Purpose:** Prisma ORM patterns for TypeScript backends — schema design, query optimization, transactions, pagination, and critical traps like updateMany returning count not records, $transaction timeouts, migrate dev resetting the DB, @updatedAt skipped on bulk writes, and serverless connection exhaustion.
- **When to use:** - Designing or modifying Prisma schema models and relations - Writing queries, transactions, or pagination logic - Using `updateMany`, `deleteMany`, or any bulk operation - Running or planning database migrations - Deploying to serverless environments (Vercel, ...
- **Workflow sections:** When to Activate / Core Concepts / Code Examples / Anti-Patterns / Best Practices / Related Skills
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:prisma-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\prisma-patterns\SKILL.md`

##### `production-scheduling`

- **Purpose:** > | Codified expertise for production scheduling, job sequencing, line balancing, | changeover optimization, and bottleneck resolution in discrete and batch | manufacturing. Informed by production schedulers with 15+ years experience. | Includes TOC/drum-buffer-rope, SMED, OEE analysis, disruption response | frameworks, and ERP/MES interaction patterns. Use when scheduling production, | resolving ...
- **When to use:** Use when scheduling production, | resolving bottlenecks, optimizing changeovers, responding to disruptions, | or balancing manufacturing lines.
- **Workflow sections:** Role and Context / When to Use / How It Works / Examples / Core Knowledge / Decision Frameworks / Key Edge Cases / Communication Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:production-scheduling`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\production-scheduling\SKILL.md`

##### `python-patterns`

- **Purpose:** Pythonic idioms, PEP 8 standards, type hints, and best practices for building robust, efficient, and maintainable Python applications.
- **When to use:** - Writing new Python code - Reviewing Python code - Refactoring existing Python code - Designing Python packages/modules
- **Workflow sections:** When to Activate / Core Principles / Type Hints / Error Handling Patterns / Context Managers / Comprehensions and Generators / Data Classes and Named Tuples / Decorators
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:python-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\python-patterns\SKILL.md`

##### `pytorch-patterns`

- **Purpose:** PyTorch deep learning patterns and best practices for building robust, efficient, and reproducible training pipelines, model architectures, and data loading.
- **When to use:** - Writing new PyTorch models or training scripts - Reviewing deep learning code - Debugging training loops or data pipelines - Optimizing GPU memory usage or training speed - Setting up reproducible experiments
- **Workflow sections:** When to Activate / Core Principles / Model Architecture Patterns / Training Loop Patterns / Data Pipeline Patterns / Checkpointing Patterns / Performance Optimization / Quick Reference: PyTorch Idioms
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:pytorch-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\pytorch-patterns\SKILL.md`

##### `quarkus-patterns`

- **Purpose:** Quarkus 3.x LTS architecture patterns with Camel for messaging, RESTful API design, CDI services, data access with Panache, and async processing. Use for Java Quarkus backend work with event-driven architectures.
- **Workflow sections:** When to Activate / Service Layer with Multiple Dependencies / Custom Logging Context Pattern (Logback) / Event Service Pattern / Camel Message Publishing (RabbitMQ) / Camel Direct Routes (In-Memory) / Camel File Processing / Camel Bean Invocation
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:quarkus-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\quarkus-patterns\SKILL.md`

##### `react-native-patterns`

- **Purpose:** React Native and Expo app patterns — Expo Router navigation, state separation (server/client/route/form), TanStack Query data fetching with Zod, performant lists, NativeWind/StyleSheet styling, native APIs, and secure storage. Use when building or editing React Native / Expo screens, components, navigation, or data layers.
- **When to use:** Use when building or editing React Native / Expo screens, components, navigation, or data layers.
- **Workflow sections:** When to Activate / Core Concepts / Code Examples / Anti-Patterns / Best Practices / Related Skills
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:react-native-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\react-native-patterns\SKILL.md`

##### `react-patterns`

- **Purpose:** React 18/19 patterns including hooks discipline, server/client component boundaries, Suspense + error boundaries, form actions, data fetching, state management decision trees, and accessibility-first composition. Use when writing or reviewing React components.
- **When to use:** Use when writing or reviewing React components.
- **Workflow sections:** When to Activate / Core Principles / Hooks Discipline / State Location Decision Tree / Server / Client Components (RSC) / Suspense + Error Boundaries / Forms / Data Fetching Decision Matrix
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:react-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\react-patterns\SKILL.md`

##### `react-performance`

- **Purpose:** React and Next.js performance optimization patterns adapted from Vercel Engineering's React Best Practices (https://github.com/vercel-labs/agent-skills). Organizes 70+ rules across 8 priority categories — waterfalls, bundle size, server-side, client fetching, re-render, rendering, JS micro-perf, advanced. Use when writing, reviewing, or refactoring React/Next.js code for performance.
- **When to use:** Use when writing, reviewing, or refactoring React/Next.
- **Workflow sections:** When to Activate / Priority Index / 1. Eliminating Waterfalls (CRITICAL) / 2. Bundle Size Optimization (CRITICAL) / 3. Server-Side Performance (HIGH) / 4. Client-Side Data Fetching (MEDIUM-HIGH) / 5. Re-render Optimization (MEDIUM) / 6. Rendering Performance (MEDIUM)
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:react-performance`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\react-performance\SKILL.md`

##### `redis-patterns`

- **Purpose:** Redis data structure patterns, caching strategies, distributed locks, rate limiting, pub/sub, and connection management for production applications.
- **When to use:** - Adding caching to an application - Implementing rate limiting or throttling - Building distributed locks or coordination - Setting up session or token storage - Using Pub/Sub or Redis Streams for messaging - Configuring Redis in production (pooling, eviction ...
- **Workflow sections:** How It Works / When to Activate / Data Structure Cheat Sheet / Core Patterns / Rate Limiting / Distributed Locks / Pub/Sub & Streams / Key Design
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:redis-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\redis-patterns\SKILL.md`

##### `rust-patterns`

- **Purpose:** Idiomatic Rust patterns, ownership, error handling, traits, concurrency, and best practices for building safe, performant applications.
- **When to use:** - Writing new Rust code - Reviewing Rust code - Refactoring existing Rust code - Designing crate structure and module layout
- **Workflow sections:** When to Use / How It Works / Core Principles / Error Handling / Enums and Pattern Matching / Traits and Generics / Structs and Data Modeling / Iterators and Closures
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:rust-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\rust-patterns\SKILL.md`

##### `springboot-patterns`

- **Purpose:** Spring Boot architecture patterns, REST API design, layered services, data access, caching, async processing, and logging. Use for Java Spring Boot backend work.
- **When to use:** - Building REST APIs with Spring MVC or WebFlux - Structuring controller → service → repository layers - Configuring Spring Data JPA, caching, or async processing - Adding validation, exception handling, or pagination - Setting up profiles for dev/staging/prod ...
- **Workflow sections:** When to Activate / REST API Structure / Repository Pattern (Spring Data JPA) / Service Layer with Transactions / DTOs and Validation / Exception Handling / Caching / Async Processing
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:springboot-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\springboot-patterns\SKILL.md`

##### `swift-actor-persistence`

- **Purpose:** Thread-safe data persistence in Swift using actors — in-memory cache with file-backed storage, eliminating data races by design.
- **When to use:** - Building a data persistence layer in Swift 5.5+ - Need thread-safe access to shared mutable state - Want to eliminate manual synchronization (locks, DispatchQueues) - Building offline-first apps with local storage
- **Workflow sections:** When to Activate / Core Pattern / Key Design Decisions / Best Practices / Anti-Patterns to Avoid / When to Use
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:swift-actor-persistence`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\swift-actor-persistence\SKILL.md`

##### `swift-concurrency-6-2`

- **Purpose:** Swift 6.2 Approachable Concurrency — single-threaded by default, @concurrent for explicit background offloading, isolated conformances for main actor types.
- **When to use:** - Migrating Swift 5.x or 6.0/6.1 projects to Swift 6.2 - Resolving data-race safety compiler errors - Designing MainActor-based app architecture - Offloading CPU-intensive work to background threads - Implementing protocol conformances on MainActor-isolated ty ...
- **Workflow sections:** When to Activate / Core Problem: Implicit Background Offloading / Core Pattern — Isolated Conformances / Core Pattern — Global and Static Variables / Core Pattern — @concurrent for Background Work / Key Design Decisions / Migration Steps / Best Practices
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:swift-concurrency-6-2`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\swift-concurrency-6-2\SKILL.md`

##### `swiftui-patterns`

- **Purpose:** SwiftUI architecture patterns, state management with @Observable, view composition, navigation, performance optimization, and modern iOS/macOS UI best practices.
- **When to use:** - Building SwiftUI views and managing state (`@State`, `@Observable`, `@Binding`) - Designing navigation flows with `NavigationStack` - Structuring view models and data flow - Optimizing rendering performance for lists and complex layouts - Working with enviro ...
- **Workflow sections:** When to Activate / State Management / View Composition / Navigation / Performance / Previews / Anti-Patterns to Avoid / References
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:swiftui-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\swiftui-patterns\SKILL.md`

##### `tinystruct-patterns`

- **Purpose:** Expert guidance for developing with the tinystruct Java framework. Use when working on the tinystruct codebase or any project built on tinystruct — including creating Application classes, @Action-mapped routes, unit tests, ActionRegistry, HTTP/CLI dual-mode handling, the built-in HTTP server, the event system, JSON with Builder/Builders, database persistence with AbstractData, POJO generation, Ser ...
- **When to use:** Use when working on the tinystruct codebase or any project built on tinystruct — including creating Application classes, @Action-mapped routes, unit tests, ActionRegistry, HTTP/CLI dual-mode handling, the built-in HTTP server, the event system, JSON with Build ...
- **Workflow sections:** Core Principle / When to Activate / How It Works / Examples / MCP Server and Tools Integration / Configuration / Red Flags & Anti-patterns / Best Practices
- **Dependencies / tools:** bundled: `references/`; files: `.orphaned_at`
- **Invocation:** `/ecc:tinystruct-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\tinystruct-patterns\SKILL.md`

##### `ui-to-vue`

- **Purpose:** Use when the user has UI screenshots or design exports that need batch conversion into Vue 3 components, especially with Vant, Element Plus, or Ant Design Vue.
- **When to use:** Use when the user has UI screenshots or design exports that need batch conversion into Vue 3 components, especially with Vant, Element Plus, or Ant Design Vue.
- **Workflow sections:** When to Use / When Not to Use / Inputs / Conversion Model / CLI Usage / Options / API Key Handling / Security and Privacy
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:ui-to-vue`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ui-to-vue\SKILL.md`

##### `vite-patterns`

- **Purpose:** Vite build tool patterns including config, plugins, HMR, env variables, proxy setup, SSR, library mode, dependency pre-bundling, and build optimization. Activate when working with vite.config.ts, Vite plugins, or Vite-based projects.
- **When to use:** Activate when working with vite.
- **Workflow sections:** When to Use / How It Works / Examples / Quick Reference / Related Skills
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:vite-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\vite-patterns\SKILL.md`

##### `vue-patterns`

- **Purpose:** Vue.js 3 Composition API patterns, component architecture, reactivity best practices, Pinia state management, Vue Router navigation, and Nuxt SSR patterns. Activates for Vue, Nuxt, Vite, or Pinia projects.
- **When to use:** Activate this skill when: - The project uses Vue.js (any version), Nuxt, Vite + Vue, or Pinia. - The user asks about Vue component architecture, composables, reactivity, or state management. - Reviewing Vue Single-File Components (`.vue` files). - Setting up V ...
- **Workflow sections:** When to Activate / 1. Project Structure / 2. Component Architecture / 3. Composables (Reusable Logic) / 4. State Management / 5. Vue Router / 6. Template Patterns / 7. Performance
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:vue-patterns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\vue-patterns\SKILL.md`

#### Agents & orchestration (51)

##### `agent-architecture-audit`

- **Purpose:** Full-stack diagnostic for agent and LLM applications. Audits the 12-layer agent stack for wrapper regression, memory pollution, tool discipline failures, hidden repair loops, and rendering corruption. Produces severity-ranked findings with code-first fixes. Essential for developers building agent applications, autonomous loops, or any LLM-powered feature.
- **Workflow sections:** When to Activate / The 12-Layer Stack / Common Failure Patterns / Audit Workflow / Severity Model / Output Format / Quick Diagnostic Questions / Anti-Patterns to Avoid
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:agent-architecture-audit`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\agent-architecture-audit\SKILL.md`

##### `agent-eval`

- **Purpose:** Head-to-head comparison of coding agents (Claude Code, Aider, Codex, etc.) on custom tasks with pass rate, cost, time, and consistency metrics
- **When to use:** - Comparing coding agents (Claude Code, Aider, Codex, etc.) on your own codebase - Measuring agent performance before adopting a new tool or model - Running regression checks when an agent updates its model or tooling - Producing data-backed agent selection de ...
- **Workflow sections:** When to Activate / Installation / Core Concepts / Workflow / Judge Types / Best Practices / Links
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:agent-eval`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\agent-eval\SKILL.md`

##### `agent-harness-construction`

- **Purpose:** Design and optimize AI agent action spaces, tool definitions, and observation formatting for higher completion rates.
- **Workflow sections:** Core Model / Action Space Design / Granularity Rules / Observation Design / Error Recovery Contract / Context Budgeting / Architecture Pattern Guidance / Benchmarking
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:agent-harness-construction`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\agent-harness-construction\SKILL.md`

##### `agent-introspection-debugging`

- **Purpose:** Structured self-debugging workflow for AI agent failures using capture, diagnosis, contained recovery, and introspection reports.
- **When to use:** - Maximum tool call / loop-limit failures - Repeated retries with no forward progress - Context growth or prompt drift that starts degrading output quality - File-system or environment state mismatch between expectation and reality - Tool failures that are lik ...
- **Workflow sections:** When to Activate / Scope Boundaries / Four-Phase Loop / Failure Capture / Recovery Action / Agent Self-Debug Report / Recovery Heuristics / Integration with ECC
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:agent-introspection-debugging`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\agent-introspection-debugging\SKILL.md`

##### `agent-payment-x402`

- **Purpose:** Add x402 payment execution to AI agents with per-task budgets, spending controls, and non-custodial wallets. Supports Base through agentwallet-sdk and X Layer through OKX Payments / OKX Agent Payments Protocol.
- **When to use:** Use when: your agent needs to pay for an API call, purchase a service, settle with another agent, enforce per-task spending limits, or manage a non-custodial wallet. Pairs naturally with cost-aware-llm-pipeline and security-review skills.
- **Workflow sections:** When to Use / Decision Tree / Supported Networks / How It Works / MCP Integration / Examples / Best Practices / Production Reference
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:agent-payment-x402`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\agent-payment-x402\SKILL.md`

##### `agent-self-evaluation`

- **Purpose:** Use after completing any non-trivial task. The agent self-rates its output on 5 axes — accuracy, completeness, clarity, actionability, conciseness — with concrete evidence per criterion. Produces a structured 1-5 scorecard with specific improvement suggestions.
- **Workflow sections:** When to Activate / Core Concepts / Workflow / Code Examples / Anti-Patterns / Best Practices / Related Skills
- **Dependencies / tools:** bundled: `examples/`, `references/`, `scripts/`, `templates/`; files: `.orphaned_at`
- **Invocation:** `/ecc:agent-self-evaluation`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\agent-self-evaluation\SKILL.md`

##### `agent-sort`

- **Purpose:** Build an evidence-backed ECC install plan for a specific repo by sorting skills, commands, rules, hooks, and extras into DAILY vs LIBRARY buckets using parallel repo-aware review passes. Use when ECC should be trimmed to what a project actually needs instead of loading the full bundle.
- **When to use:** Use when ECC should be trimmed to what a project actually needs instead of loading the full bundle.
- **Workflow sections:** When to Use / Non-Negotiable Rules / Outputs / Classification Model / Evidence Sources / Parallel Review Passes / Core Workflow / Handoffs
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:agent-sort`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\agent-sort\SKILL.md`

##### `agentic-engineering`

- **Purpose:** Operate as an agentic engineer using eval-first execution, decomposition, and cost-aware model routing.
- **Workflow sections:** Operating Principles / Eval-First Loop / Task Decomposition / Model Routing / Session Strategy / Review Focus for AI-Generated Code / Cost Discipline
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:agentic-engineering`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\agentic-engineering\SKILL.md`

##### `agentic-os`

- **Purpose:** Build persistent multi-agent operating systems on Claude Code. Covers kernel architecture, specialist agents, slash commands, file-based memory, scheduled automation, and state management without external databases.
- **When to use:** - Building a multi-agent workflow inside Claude Code - Setting up persistent Claude Code automation that survives session restarts - Creating a "personal OS" or "agentic OS" for recurring tasks - User says "agentic OS", "personal OS", "multi-agent", "agent coo ...
- **Workflow sections:** When to Activate / Architecture Overview / The Kernel / Identity / Agent Registry / Routing Rules / Model Policies / Specialist Agents
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:agentic-os`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\agentic-os\SKILL.md`

##### `ai-first-engineering`

- **Purpose:** Engineering operating model for teams where AI agents generate a large share of implementation output.
- **Workflow sections:** Process Shifts / Architecture Requirements / Code Review in AI-First Teams / Hiring and Evaluation Signals / Testing Standard
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:ai-first-engineering`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ai-first-engineering\SKILL.md`

##### `autonomous-agent-harness`

- **Purpose:** Transform Claude Code into a fully autonomous agent system with persistent memory, scheduled operations, computer use, and task queuing. Replaces standalone agent frameworks (Hermes, AutoGPT) by leveraging Claude Code's native crons, dispatch, MCP tools, and memory. Use when the user wants continuous autonomous operation, scheduled tasks, or a self-directing agent loop.
- **When to use:** Use when the user wants continuous autonomous operation, scheduled tasks, or a self-directing agent loop.
- **Workflow sections:** Consent and Safety Boundaries / When to Activate / Architecture / Core Components / Active Tasks / Completed / Replacing Hermes / Setup Guide
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:autonomous-agent-harness`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\autonomous-agent-harness\SKILL.md`

##### `autonomous-loops`

- **Purpose:** Patterns and architectures for autonomous Claude Code loops — from simple sequential pipelines to RFC-driven multi-agent DAG systems.
- **When to use:** - Setting up autonomous development workflows that run without human intervention - Choosing the right loop architecture for your problem (simple vs complex) - Building CI/CD-style continuous development pipelines - Running parallel agents with merge coordinat ...
- **Workflow sections:** When to Use / Loop Pattern Spectrum / 1. Sequential Pipeline (`claude -p`) / 2. NanoClaw REPL / 3. Infinite Agentic Loop / 4. Continuous Claude PR Loop / Progress / Next Steps
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:autonomous-loops`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\autonomous-loops\SKILL.md`

##### `benchmark-optimization-loop`

- **Purpose:** Use when the user asks to make something faster, try many variants, run recursive optimization, benchmark latency/throughput/cost, or choose the best implementation by repeated measured tests.
- **When to use:** Use when the user asks to make something faster, try many variants, run recursive optimization, benchmark latency/throughput/cost, or choose the best implementation by repeated measured tests.
- **Workflow sections:** Required Baseline / Loop / Variant Table / Recursive Search / Promotion Gate
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:benchmark-optimization-loop`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\benchmark-optimization-loop\SKILL.md`

##### `claude-devfleet`

- **Purpose:** Orchestrate multi-agent coding tasks via Claude DevFleet — plan projects, dispatch parallel agents in isolated worktrees, monitor progress, and read structured reports.
- **When to use:** Use this skill when you need to dispatch multiple Claude Code agents to work on coding tasks in parallel. Each agent runs in an isolated git worktree with full tooling.
- **Workflow sections:** When to Use / Setup / How It Works / Examples / Guidelines
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:claude-devfleet`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\claude-devfleet\SKILL.md`

##### `configure-ecc`

- **Purpose:** Guide ECC installation, update, or reconfiguration from inside Claude Code, Codex, or Kimi while respecting each harness's real plugin, scope, and hook capabilities.
- **Workflow sections:** Route by the current harness / Claude Code: run the full conversational wizard / Codex: use the native plugin lifecycle / Kimi: install the project surface
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:configure-ecc`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\configure-ecc\SKILL.md`

##### `continuous-agent-loop`

- **Purpose:** Patterns for continuous autonomous agent loops with quality gates, evals, and recovery controls.
- **Workflow sections:** Loop Selection Flow / Combined Pattern / Failure Modes / Recovery
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:continuous-agent-loop`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\continuous-agent-loop\SKILL.md`

##### `continuous-learning-v2`

- **Purpose:** Instinct-based learning system that observes sessions via hooks, creates atomic instincts with confidence scoring, and evolves them into skills/commands/agents. v2.1 adds project-scoped instincts to prevent cross-project contamination.
- **When to use:** - Setting up automatic learning from Claude Code sessions - Configuring instinct-based behavior extraction via hooks - Tuning confidence thresholds for learned behaviors - Reviewing, exporting, or importing instinct libraries - Evolving instincts into full ski ...
- **Workflow sections:** When to Activate / What's New in v2.1 / What's New in v2 (vs v1) / The Instinct Model / Action / Evidence / How It Works / Project Detection
- **Dependencies / tools:** bundled: `scripts/`; files: `.orphaned_at`, `agents/`, `config.json`, `hooks/`
- **Invocation:** `/ecc:continuous-learning-v2`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\continuous-learning-v2\SKILL.md`

##### `council`

- **Purpose:** Convene a four-voice council for ambiguous decisions, tradeoffs, and go/no-go calls. Use when multiple valid paths exist and you need structured disagreement before choosing.
- **When to use:** Use when multiple valid paths exist and you need structured disagreement before choosing.
- **Workflow sections:** When to Use / When NOT to Use / Roles / Workflow / Council: [short decision title] / Persistence Rule / Multi-Round Follow-up / Anti-Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:council`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\council\SKILL.md`

##### `data-scraper-agent`

- **Purpose:** Build a fully automated AI-powered data collection agent for any public source — job boards, prices, news, GitHub, sports, anything. Runs on a schedule, enriches data with a free LLM (Gemini Flash), stores results in Notion/Sheets/Supabase, and learns from user feedback. Runs 100% free on GitHub Actions. Use when the user wants to monitor, collect, or track any public data automatically.
- **When to use:** Use when the user wants to monitor, collect, or track any public data automatically.
- **Workflow sections:** When to Activate / Core Concepts / Workflow / Common Scraping Patterns / Anti-Patterns to Avoid / Free Tier Limits Reference / Requirements Template / Quality Checklist
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:data-scraper-agent`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\data-scraper-agent\SKILL.md`

##### `dmux-workflows`

- **Purpose:** Multi-agent orchestration using dmux (tmux pane manager for AI agents). Patterns for parallel agent workflows across Claude Code, Codex, OpenCode, and other harnesses. Use when running multiple agent sessions in parallel or coordinating multi-agent development workflows.
- **When to use:** Use when running multiple agent sessions in parallel or coordinating multi-agent development workflows.
- **Workflow sections:** When to Activate / What is dmux / Quick Start / Workflow Patterns / Best Practices / Git Worktree Integration / Complementary Tools / ECC Helper
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:dmux-workflows`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\dmux-workflows\SKILL.md`

##### `dynamic-workflow-mode`

- **Purpose:** Design task-local harnesses, eval gates, and reusable skill extraction for Claude dynamic workflow mode and other adaptive agent harnesses.
- **Workflow sections:** When To Activate / Core Contract / Dynamic Harness Decision Tree / Task-Local Harness Template / Shared Skill Extraction / Control Pane Checkpoints / Eval Gates / Anti-Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:dynamic-workflow-mode`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\dynamic-workflow-mode\SKILL.md`

##### `enterprise-agent-ops`

- **Purpose:** Operate long-lived agent workloads with observability, security boundaries, and lifecycle management.
- **Workflow sections:** Operational Domains / Baseline Controls / Metrics to Track / Incident Pattern / Deployment Integrations
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:enterprise-agent-ops`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\enterprise-agent-ops\SKILL.md`

##### `eval-harness`

- **Purpose:** Formal evaluation framework for Claude Code sessions implementing eval-driven development (EDD) principles
- **When to use:** - Setting up eval-driven development (EDD) for AI-assisted workflows - Defining pass/fail criteria for Claude Code task completion - Measuring agent reliability with pass@k metrics - Creating regression test suites for prompt or agent changes - Benchmarking ag ...
- **Workflow sections:** When to Activate / Philosophy / Eval Types / Grader Types / Metrics / Eval Workflow / EVAL DEFINITION: feature-xyz / Integration Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:eval-harness`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\eval-harness\SKILL.md`

##### `flox-environments`

- **Purpose:** Create reproducible, cross-platform (macOS/Linux) development environments with Flox, a declarative Nix-based environment manager. Use when setting up project toolchains for any language, installing system-level dependencies (compilers, databases, native libs like openssl/BLAS), pinning exact package versions for a team, running local services (PostgreSQL, Redis, Kafka), onboarding developers with ...
- **When to use:** Use when setting up project toolchains for any language, installing system-level dependencies (compilers, databases, native libs like openssl/BLAS), pinning exact package versions for a team, running local services (PostgreSQL, Redis, Kafka), onboarding develo ...
- **Workflow sections:** When to Activate / Core Concepts / Essential Commands / Manifest Structure / Package Installation Patterns / Language-Specific Recipes / Hooks and Profile / Anti-Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:flox-environments`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\flox-environments\SKILL.md`

##### `gan-style-harness`

- **Purpose:** GAN-inspired Generator-Evaluator agent harness for building high-quality applications autonomously. Based on Anthropic's March 2026 harness design paper.
- **When to use:** - Building complete applications from a one-line prompt - Frontend design tasks requiring high visual quality - Full-stack projects that need working features, not just code - Any task where "AI slop" aesthetics are unacceptable - Projects where you want to in ...
- **Workflow sections:** Core Insight / When to Use / When NOT to Use / Architecture / The Three Agents / Evaluation Criteria / Evaluation Rubric / Usage
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:gan-style-harness`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\gan-style-harness\SKILL.md`

##### `gateguard`

- **Purpose:** Fact-forcing gate that blocks Edit/Write/Bash (including MultiEdit) and demands concrete investigation (importers, data schemas, user instruction) before allowing the action. Measurably improves output quality by +2.25 points vs ungated agents.
- **When to use:** - Working on any codebase where file edits affect multiple modules - Projects with data files that have specific schemas or date formats - Teams where AI-generated code must match existing patterns - Any workflow where Claude tends to guess instead of investig ...
- **Workflow sections:** When to Activate / Core Concept / Evidence / Gate Types / Quick Start / Anti-Patterns / Best Practices / Related Skills
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:gateguard`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\gateguard\SKILL.md`

##### `healthcare-eval-harness`

- **Purpose:** Patient safety evaluation harness for healthcare application deployments. Automated test suites for CDSS accuracy, PHI exposure, clinical workflow integrity, and integration compliance. Blocks deployments on safety failures.
- **When to use:** - Before any deployment of EMR/EHR applications - After modifying CDSS logic (drug interactions, dose validation, scoring) - After changing database schemas that touch patient data - After modifying authentication or access control - During CI/CD pipeline conf ...
- **Workflow sections:** When to Use / How It Works / Examples / Healthcare Eval: 2026-03-27 [commit abc1234]
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:healthcare-eval-harness`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\healthcare-eval-harness\SKILL.md`

##### `inherit-legacy-style`

- **Purpose:** Legacy-project style inheritance skill. Use when the user types /inherit-legacy-style, or when onboarding an AI coding agent onto a hand-written legacy project and you need to prevent "style drift" (the model imposing its pretrained mainstream idioms onto the project). Language- and framework-agnostic — it aligns meta-architecture only, not syntax. Once run, it becomes a behavioral constraint on a ...
- **When to use:** Use when the user types /inherit-legacy-style, or when onboarding an AI coding agent onto a hand-written legacy project and you need to prevent "style drift" (the model imposing its pretrained mainstream idioms onto the project).
- **Workflow sections:** When to Activate / When to Use / Prerequisites / Workflow / How It Works / Output Specification / Anti-Patterns / Best Practices
- **Dependencies / tools:** allowed-tools: `Read, Glob, Grep, Bash, Edit, Write, AskUserQuestion`; files: `.orphaned_at`
- **Invocation:** `/ecc:inherit-legacy-style`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\inherit-legacy-style\SKILL.md`

##### `intent-driven-development`

- **Purpose:** Turn ambiguous or high-impact product and engineering changes into scoped, verifiable acceptance criteria before or alongside implementation. Use when a user asks to clarify a feature, define acceptance criteria, de-risk a security/data/migration/integration change, prepare implementation requirements for another agent, or make a complex request testable. Do not trigger for trivial edits, straight ...
- **When to use:** Use when a user asks to clarify a feature, define acceptance criteria, de-risk a security/data/migration/integration change, prepare implementation requirements for another agent, or make a complex request testable.
- **Workflow sections:** When to Activate / How It Works / Examples / Operating Rules / Choose The Depth / Workflow / Output Template / Revision Log
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:intent-driven-development`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\intent-driven-development\SKILL.md`

##### `ito-data-atlas-agent`

- **Purpose:** Design source-grounded Data Atlas style agents for Itô basket research, market discovery, parameter drafting, and human-in-the-loop editing. Use for architecture and read-only workflow planning, not live order execution.
- **Workflow sections:** Discovery / Supported Itô data surfaces and dependency gate / Authentication and return handoff / Research workflow / Privacy and storage / Confirmation boundary / Structured output contract
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:ito-data-atlas-agent`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ito-data-atlas-agent\SKILL.md`

##### `latency-critical-systems`

- **Purpose:** Use for latency-sensitive systems such as realtime dashboards, market data, streaming agents, execution gateways, queues, caches, or HFT-like infrastructure where freshness and p95 latency matter.
- **Workflow sections:** Split The Metrics / Map The Hot Path / Optimization Order / Verification / Guardrails
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:latency-critical-systems`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\latency-critical-systems\SKILL.md`

##### `lead-intelligence`

- **Purpose:** AI-native lead intelligence and outreach pipeline. Replaces Apollo, Clay, and ZoomInfo with agent-powered signal scoring, mutual ranking, warm path discovery, source-derived voice modeling, and channel-specific outreach across email, LinkedIn, and X. Use when the user wants to find, qualify, and reach high-value contacts.
- **When to use:** Use when the user wants to find, qualify, and reach high-value contacts.
- **Workflow sections:** When to Activate / Tool Requirements / Pipeline Overview / Voice Before Outreach / Stage 1: Signal Scoring / Stage 2: Mutual Ranking / Stage 3: Warm Path Discovery / Stage 4: Enrichment
- **Dependencies / tools:** files: `.orphaned_at`, `agents/`
- **Invocation:** `/ecc:lead-intelligence`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\lead-intelligence\SKILL.md`

##### `llm-trading-agent-security`

- **Purpose:** Security patterns for autonomous trading agents with wallet or transaction authority. Covers prompt injection, spend limits, pre-send simulation, circuit breakers, MEV protection, and key handling.
- **When to use:** - Building an AI agent that signs and sends transactions - Auditing a trading bot or on-chain execution assistant - Designing wallet key management for an agent - Giving an LLM access to order placement, swaps, or treasury operations
- **Workflow sections:** When to Use / How It Works / Examples / Pre-Deploy Checklist
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:llm-trading-agent-security`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\llm-trading-agent-security\SKILL.md`

##### `loop-design-check`

- **Purpose:** Design a goal-oriented agent loop, and review it for the ways loops go wrong — spinning and burning tokens, Goodhart-gaming the verifier, or running a wrong answer to completion. Two actions: (1) WRITE a loop — gate whether to build it, define a machine-decidable goal, pick the loop type, pick a skeleton; (2) REVIEW a loop — run it past five failure modes plus decidability, boundaries, fallback, j ...
- **When to use:** Use when designing an autonomous agent loop, or when you already have one and worry it will spin, cheat, or run a wrong answer to the end.
- **Workflow sections:** When to use / not / Red-line premise: two levels of feedback / Action 1 — Write a loop (5 steps) / Action 2 — Review a loop (checklist = five failure modes) / Worked example — reviewing a "nightly green-keeper" loop / One-line close
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:loop-design-check`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\loop-design-check\SKILL.md`

##### `ml-adoption-playbook`

- **Purpose:** End-to-end methodology for AI agents and software engineers to add machine learning algorithms to existing non-ML codebases. Covers problem framing, data readiness, architectural decoupling, and baseline model integration.
- **When to use:** - A user asks to "add ML" or "add an algorithm" to their existing codebase. - Planning the integration of a new model (e.g., recommendation, classification, forecasting) into a non-ML application. - Structuring a workflow for an agent to build, train, and depl ...
- **Workflow sections:** When to Activate / Phase 1: Problem Framing & Feasibility / Phase 2: Data Readiness / Phase 3: Architectural Integration & Decoupling / Phase 4: Model Implementation & Training / Phase 5: Handoff to MLOps / Iterative Agent Workflow
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:ml-adoption-playbook`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ml-adoption-playbook\SKILL.md`

##### `nanoclaw-repl`

- **Purpose:** Operate and extend NanoClaw v2, ECC's zero-dependency session-aware REPL built on claude -p.
- **Workflow sections:** Capabilities / Operating Guidance / Extension Rules
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:nanoclaw-repl`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\nanoclaw-repl\SKILL.md`

##### `openclaw-persona-forge`

- **Purpose:** 为 OpenClaw AI Agent 锻造完整的龙虾灵魂方案。根据用户偏好或随机抽卡， 输出身份定位、灵魂描述(SOUL.md)、角色化底线规则、名字和头像生图提示词。 如当前环境提供已审核的生图 skill，可自动生成统一风格头像图片。 当用户需要创建、设计或定制 OpenClaw 龙虾灵魂时使用。 不适用于：微调已有 SOUL.md、非 OpenClaw 平台的角色设计、纯工具型无性格 Agent。 触发词：龙虾灵魂、虾魂、OpenClaw 灵魂、养虾灵魂、龙虾角色、龙虾定位、 龙虾剧本杀角色、龙虾游戏角色、龙虾 NPC、龙虾性格、龙虾背景故事、 lobster soul、lobster character、抽卡、随机龙虾、龙虾 SOUL、gacha。
- **When to use:** - 当用户需要从零创建 OpenClaw 龙虾灵魂、角色设定、SOUL.md 或 IDENTITY.md - 当用户想通过引导式问答或抽卡模式快速得到完整 persona 方案 - 当用户已经有一个粗糙设定，但还缺名字、边界规则、头像提示词或成套输出文件
- **Workflow sections:** When to Use / 前置条件 / Skill 目录约定 / 内置工具 / 可选依赖 / 核心理念 / How It Works / Step 1：选方向（引导模式）
- **Dependencies / tools:** bundled: `references/`; files: `.orphaned_at`, `gacha.py`, `gacha.sh`
- **Invocation:** `/ecc:openclaw-persona-forge`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\openclaw-persona-forge\SKILL.md`

##### `orch-add-feature`

- **Purpose:** Orchestrate building a brand-new feature end to end — research, plan, TDD implementation, review, and gated commit — by delegating each phase to the matching ECC agent. Use when adding a capability that does not exist yet.
- **When to use:** Use when adding a capability that does not exist yet.
- **Workflow sections:** When to Use / Operation settings / How It Works / Example
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:orch-add-feature`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\orch-add-feature\SKILL.md`

##### `orch-change-feature`

- **Purpose:** Orchestrate altering an existing, working feature to new desired behavior — update its tests to the new spec, change the implementation to match, review, and gated commit. Use when behavior is not broken but should be different.
- **When to use:** Use when behavior is not broken but should be different.
- **Workflow sections:** When to Use / Operation settings / How It Works / Example
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:orch-change-feature`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\orch-change-feature\SKILL.md`

##### `orch-fix-defect`

- **Purpose:** Orchestrate fixing a bug — reproduce it as a failing regression test, fix to green, review, and gated commit — by delegating each phase to the matching ECC agent. Use when existing behavior is broken or wrong.
- **When to use:** Use when existing behavior is broken or wrong.
- **Workflow sections:** When to Use / Operation settings / How It Works / Example
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:orch-fix-defect`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\orch-fix-defect\SKILL.md`

##### `orch-refine-code`

- **Purpose:** Orchestrate a behavior-preserving refactor — confirm tests are green, restructure without changing behavior, keep tests green, review, and gated commit. Use when the structure should improve but behavior must not change.
- **When to use:** Use when the structure should improve but behavior must not change.
- **Workflow sections:** When to Use / Operation settings / How It Works / Example
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:orch-refine-code`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\orch-refine-code\SKILL.md`

##### `parallel-execution-optimizer`

- **Purpose:** Use when the user wants a task done much faster through parallel work, concurrent agents, batched tool calls, isolated worktrees, or many independent verification lanes without losing correctness.
- **When to use:** Use when the user wants a task done much faster through parallel work, concurrent agents, batched tool calls, isolated worktrees, or many independent verification lanes without losing correctness.
- **Workflow sections:** Core Pattern / Lane Matrix / Execution Rules / Output Shape / Failure Modes
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:parallel-execution-optimizer`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\parallel-execution-optimizer\SKILL.md`

##### `plan-orchestrate`

- **Purpose:** Read a plan document, decompose it into steps, design a per-step agent chain from the ECC catalogue, and emit ready-to-paste /orchestrate custom prompts. Generative only — never invokes /orchestrate itself. Use when the user has a multi-step plan and wants to drive it through orchestrate without composing chains by hand.
- **When to use:** Use when the user has a multi-step plan and wants to drive it through orchestrate without composing chains by hand.
- **Workflow sections:** When to Activate / Inputs / Authoritative `/orchestrate` shape (do not deviate) / ECC install form and namespacing / Available agent catalogue (must pick from these) / How It Works / Steps overview / Step 1 — <title>
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:plan-orchestrate`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\plan-orchestrate\SKILL.md`

##### `prompt-optimizer`

- **Purpose:** >- | Analyze raw prompts, identify intent and gaps, match ECC components | (skills/commands/agents/hooks), and output a ready-to-paste optimized | prompt. Advisory role only — never executes the task itself. | TRIGGER when: user says "optimize prompt", "improve my prompt", | "how to write a prompt for", "help me prompt", "rewrite this prompt", | or explicitly asks to enhance prompt quality. Also t ...
- **When to use:** TRIGGER when: user says "optimize prompt", "improve my prompt", | "how to write a prompt for", "help me prompt", "rewrite this prompt", | or explicitly asks to enhance prompt quality.
- **Workflow sections:** When to Use / How It Works / Output Format / Examples / Related Components
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:prompt-optimizer`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\prompt-optimizer\SKILL.md`

##### `safety-guard`

- **Purpose:** Use this skill to prevent destructive operations when working on production systems or running agents autonomously.
- **When to use:** - When working on production systems - When agents are running autonomously (full-auto mode) - When you want to restrict edits to a specific directory - During sensitive operations (migrations, deploys, data changes)
- **Workflow sections:** When to Use / How It Works / Implementation / Integration
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:safety-guard`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\safety-guard\SKILL.md`

##### `santa-method`

- **Purpose:** Multi-agent adversarial verification with convergence loop. Two independent review agents must both pass before output ships.
- **Workflow sections:** When to Activate / Architecture / Phase Details / Task Specification / Output Under Review / Evaluation Rubric / Instructions / Implementation Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:santa-method`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\santa-method\SKILL.md`

##### `skill-comply`

- **Purpose:** Visualize whether skills, rules, and agent definitions are actually followed — auto-generates scenarios at 3 prompt strictness levels, runs agents, classifies behavioral sequences, and reports compliance rates with full tool call timelines
- **When to use:** - User runs `/skill-comply <path>` - User asks "is this rule actually being followed?" - After adding new rules/skills, to verify agent compliance - Periodically as part of quality maintenance
- **Workflow sections:** Supported Targets / When to Activate / Usage / Key Concept: Prompt Independence / Report Contents
- **Dependencies / tools:** bundled: `scripts/`; files: `.gitignore`, `.orphaned_at`, `fixtures/`, `prompts/`, `pyproject.toml`, `tests/`
- **Invocation:** `/ecc:skill-comply`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\skill-comply\SKILL.md`

##### `skill-stocktake`

- **Purpose:** Use when auditing Claude skills and commands for quality. Supports Quick Scan (changed skills only) and Full Stocktake modes with sequential subagent batch evaluation.
- **When to use:** Use when auditing Claude skills and commands for quality.
- **Workflow sections:** Scope / Modes / Quick Scan Flow / Full Stocktake Flow / Results File Schema / Notes
- **Dependencies / tools:** bundled: `scripts/`; files: `.orphaned_at`
- **Invocation:** `/ecc:skill-stocktake`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\skill-stocktake\SKILL.md`

##### `social-publisher`

- **Purpose:** Agent-driven scheduling and publishing of social media posts across 13 platforms via SocialClaw. Use when the user wants to publish to X, LinkedIn, Instagram, Facebook Pages, TikTok, Discord, Telegram, YouTube, Reddit, WordPress, or Pinterest — or when managing campaigns, uploading media, or monitoring post delivery status.
- **When to use:** Use when the user wants to publish to X, LinkedIn, Instagram, Facebook Pages, TikTok, Discord, Telegram, YouTube, Reddit, WordPress, or Pinterest — or when managing campaigns, uploading media, or monitoring post delivery status.
- **Workflow sections:** When to Activate / Setup / Core Workflow / Supported Providers / Security / Related Skills / Source
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:social-publisher`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\social-publisher\SKILL.md`

##### `team-agent-orchestration`

- **Purpose:** Run team-based orchestration for agent squads using work items, ownership, agent Kanban, merge gates, and control pane handoffs.
- **When to use:** - The task spans multiple agents, tools, harnesses, branches, or worktrees. - The user mentions team orchestration, agent Kanban, squad, conductor, control pane, manager, desktop app, Zellij, tmux, Hermes, Devin, Codex, Claude Code, or multi-agent work. - A pr ...
- **Workflow sections:** When To Activate / Operating Model / Agent Kanban / Team-Based Orchestration Flow / Control Pane Requirements / Dynamic Workflow Compatibility / Failure Modes To Watch / Output Standard
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:team-agent-orchestration`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\team-agent-orchestration\SKILL.md`

##### `verification-loop`

- **Purpose:** A comprehensive verification system for Claude Code sessions.
- **When to use:** Invoke this skill: - After completing a feature or significant code change - Before creating a PR - When you want to ensure quality gates pass - After refactoring
- **Workflow sections:** When to Use / Verification Phases / Output Format / Continuous Mode / Integration with Hooks
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:verification-loop`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\verification-loop\SKILL.md`

#### Infra, deploy & ops (31)

##### `canary-watch`

- **Purpose:** Use this skill to monitor and verify a deployed URL after releases — checks HTTP endpoints, SSE streams, static assets, console errors, and performance regressions after deploys, merges, or dependency upgrades. Smoke / canary / post-deploy verification.
- **When to use:** - After deploying to production or staging - After merging a risky PR - When you want to verify a fix actually fixed it - Continuous monitoring during a launch window - After dependency upgrades
- **Workflow sections:** When to Use / How It Works / Output / Canary Report — myapp.com — 2026-03-23 03:15 PST / Integration
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:canary-watch`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\canary-watch\SKILL.md`

##### `connections-optimizer`

- **Purpose:** Reorganize the user's X and LinkedIn network with review-first pruning, add/follow recommendations, and channel-specific warm outreach drafted in the user's real voice. Use when the user wants to clean up following lists, grow toward current priorities, or rebalance a social graph around higher-signal relationships.
- **When to use:** Use when the user wants to clean up following lists, grow toward current priorities, or rebalance a social graph around higher-signal relationships.
- **Workflow sections:** When to Activate / Required Inputs / Tool Requirements / Safety Defaults / Platform Rules / Modes / Scoring Model / Workflow
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:connections-optimizer`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\connections-optimizer\SKILL.md`

##### `cost-aware-llm-pipeline`

- **Purpose:** Cost optimization patterns for LLM API usage — model routing by task complexity, budget tracking, retry logic, and prompt caching.
- **When to use:** - Building applications that call LLM APIs (Claude, GPT, etc.) - Processing batches of items with varying complexity - Need to stay within a budget for API spend - Optimizing cost without sacrificing quality on complex tasks
- **Workflow sections:** When to Activate / Core Concepts / Composition / Pricing Reference (2025-2026) / Best Practices / Anti-Patterns to Avoid / When to Use
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:cost-aware-llm-pipeline`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\cost-aware-llm-pipeline\SKILL.md`

##### `customer-billing-ops`

- **Purpose:** Operate customer billing workflows such as subscriptions, refunds, churn triage, billing-portal recovery, and plan analysis using connected billing tools like Stripe. Use when the user needs to help a customer, inspect subscription state, or manage revenue-impacting billing operations.
- **When to use:** Use when the user needs to help a customer, inspect subscription state, or manage revenue-impacting billing operations.
- **Workflow sections:** When to Use / Preferred Tool Surface / Guardrails / Workflow / Output Format / Examples of Good Recommendations
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:customer-billing-ops`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\customer-billing-ops\SKILL.md`

##### `ecc-recipes`

- **Purpose:** Map a described workflow to the right ECC command-GROUP with run-order and stop condition, and browse all command-group recipe families. Adds a family-grouping + run-order + when-to-stop layer on top of the flat command catalog. Advisory only. TRIGGER when the user says which commands for X, what command group runs X, show ECC recipes, list ECC pipelines, or how do I run a workflow with ECC. DO NO ...
- **When to use:** TRIGGER when the user says which commands for X, what command group runs X, show ECC recipes, list ECC pipelines, or how do I run a workflow with ECC.
- **Workflow sections:** When to Activate / Core Principle / Family Classification (by prefix) / How It Works / Output Template (match mode) / Examples / Non-Goals
- **Dependencies / tools:** files: `.orphaned_at`; argument-hint: `<workflow description | empty=list all>`
- **Invocation:** `/ecc:ecc-recipes`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ecc-recipes\SKILL.md`

##### `email-ops`

- **Purpose:** Evidence-first mailbox triage, drafting, send verification, and sent-mail-safe follow-up workflow for ECC. Use when the user wants to organize email, draft or send through the real mail surface, or prove what landed in Sent.
- **When to use:** Use when the user wants to organize email, draft or send through the real mail surface, or prove what landed in Sent.
- **Workflow sections:** Skill Stack / When to Use / Guardrails / Workflow / Output Format / Pitfalls / Verification
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:email-ops`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\email-ops\SKILL.md`

##### `finance-billing-ops`

- **Purpose:** Evidence-first revenue, pricing, refunds, team-billing, and billing-model truth workflow for ECC. Use when the user wants a sales snapshot, pricing comparison, duplicate-charge diagnosis, or code-backed billing reality instead of generic payments advice.
- **When to use:** Use when the user wants a sales snapshot, pricing comparison, duplicate-charge diagnosis, or code-backed billing reality instead of generic payments advice.
- **Workflow sections:** Skill Stack / When to Use / Guardrails / Workflow / Output Format / Pitfalls / Verification
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:finance-billing-ops`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\finance-billing-ops\SKILL.md`

##### `github-ops`

- **Purpose:** GitHub repository operations, automation, and management. Issue triage, PR management, CI/CD operations, release management, and security monitoring using the gh CLI. Use when the user wants to manage GitHub issues, PRs, CI status, releases, contributors, stale items, or any GitHub operational task beyond simple git commands.
- **When to use:** Use when the user wants to manage GitHub issues, PRs, CI status, releases, contributors, stale items, or any GitHub operational task beyond simple git commands.
- **Workflow sections:** When to Activate / Tool Requirements / Issue Triage / PR Management / CI/CD Operations / Release Management / Security Monitoring / Quality Gate
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:github-ops`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\github-ops\SKILL.md`

##### `google-workspace-ops`

- **Purpose:** Operate across Google Drive, Docs, Sheets, and Slides as one workflow surface for plans, trackers, decks, and shared documents. Use when the user needs to find, summarize, edit, migrate, or clean up Google Workspace assets without dropping to raw tool calls.
- **When to use:** Use when the user needs to find, summarize, edit, migrate, or clean up Google Workspace assets without dropping to raw tool calls.
- **Workflow sections:** When to Use / Preferred Tool Surface / Workflow / Output Format / Good Use Cases
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:google-workspace-ops`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\google-workspace-ops\SKILL.md`

##### `hermes-imports`

- **Purpose:** Convert local Hermes operator workflows into sanitized ECC skills and release-pack artifacts. Use when preparing a Hermes workflow for public ECC reuse without leaking private workspace state, credentials, or local-only paths.
- **When to use:** Use when preparing a Hermes workflow for public ECC reuse without leaking private workspace state, credentials, or local-only paths.
- **Workflow sections:** When To Use / Import Rules / Sanitization Checklist / Conversion Pattern / Example: Launch Handoff / Example: Quiet-Hours Operator Job / Output Contract
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:hermes-imports`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\hermes-imports\SKILL.md`

##### `homelab-network-readiness`

- **Purpose:** Readiness checklist for homelab VLAN segmentation, local DNS filtering, and WireGuard-style remote access before changing router, firewall, DHCP, or VPN configuration.
- **Workflow sections:** When to Use / Safety Rules / Required Inventory / VLAN And Trust-Zone Plan / DNS Filtering Readiness / Remote Access Readiness / Change Sequence / Review Checklist
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:homelab-network-readiness`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\homelab-network-readiness\SKILL.md`

##### `homelab-network-setup`

- **Purpose:** Practical home and homelab network planning for gateways, switches, access points, IP ranges, DHCP reservations, DNS, cabling, and common beginner mistakes.
- **When to use:** - Planning a new home network or redesigning an ISP-router-only setup. - Choosing gateway, switch, and access point roles. - Designing IP ranges, DHCP scopes, static reservations, and DNS. - Preparing for future VLANs, Pi-hole, NAS, lab servers, or VPN access. ...
- **Workflow sections:** When to Use / How It Works / IP Plan / DHCP And DNS / Cabling And Wi-Fi / Examples / Anti-Patterns / See Also
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:homelab-network-setup`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\homelab-network-setup\SKILL.md`

##### `homelab-pihole-dns`

- **Purpose:** Pi-hole installation, blocklist management, DNS-over-HTTPS setup, DHCP integration, local DNS records, and troubleshooting broken DNS resolution on a home network.
- **When to use:** - Installing Pi-hole on a Raspberry Pi or Linux host - Configuring Pi-hole as the DNS server for a home network - Adding or managing blocklists - Setting up DNS-over-HTTPS (DoH) upstream resolvers - Creating local DNS records (e.g. `nas.home.lan`, `pi.home.lan ...
- **Workflow sections:** When to Use / How Pi-hole Works / Installation / Pointing Your Network at Pi-hole / Blocklist Management / DNS-over-HTTPS Upstream / Local DNS Records / Troubleshooting
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:homelab-pihole-dns`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\homelab-pihole-dns\SKILL.md`

##### `homelab-wireguard-vpn`

- **Purpose:** WireGuard VPN server setup, peer configuration, key generation, split tunneling vs full tunnel routing, and remote access to a home network from mobile and laptop clients.
- **Workflow sections:** When to Use / How WireGuard Works / Server Setup (Linux) / Client Configuration / Split Tunnel vs Full Tunnel / Key Generation and Peer Management / pfSense / OPNsense WireGuard / DDNS (Dynamic DNS) for Home Servers
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:homelab-wireguard-vpn`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\homelab-wireguard-vpn\SKILL.md`

##### `knowledge-ops`

- **Purpose:** Knowledge base management, ingestion, sync, and retrieval across multiple storage layers (local files, MCP memory, vector stores, Git repos). Use when the user wants to save, organize, sync, deduplicate, or search across their knowledge systems.
- **When to use:** Use when the user wants to save, organize, sync, deduplicate, or search across their knowledge systems.
- **Workflow sections:** When to Activate / Knowledge Architecture / Ingestion Workflow / Sync Operations / Memory Patterns / Best Practices / Quality Gate
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:knowledge-ops`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\knowledge-ops\SKILL.md`

##### `messages-ops`

- **Purpose:** Evidence-first live messaging workflow for ECC. Use when the user wants to read texts or DMs, recover a recent one-time code, inspect a thread before replying, or prove which message source was actually checked.
- **When to use:** Use when the user wants to read texts or DMs, recover a recent one-time code, inspect a thread before replying, or prove which message source was actually checked.
- **Workflow sections:** Skill Stack / When to Use / Guardrails / Workflow / Output Format / Pitfalls / Verification
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:messages-ops`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\messages-ops\SKILL.md`

##### `network-bgp-diagnostics`

- **Purpose:** Diagnostics-only BGP troubleshooting patterns for neighbor state, route exchange, prefix policy, AS path inspection, and safe evidence collection.
- **When to use:** - BGP neighbors are stuck in Idle, Connect, Active, OpenSent, or OpenConfirm. - A session is Established but expected prefixes are missing. - A route-map, prefix-list, max-prefix limit, or AS path policy may be filtering routes. - You need before/after evidenc ...
- **Workflow sections:** When to Use / Read-Only Triage Flow / State Interpretation / Transport Checks / Route Policy Checks / AS Path And Prefix Review / Parser Pattern / Change-Window Only
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:network-bgp-diagnostics`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\network-bgp-diagnostics\SKILL.md`

##### `network-config-validation`

- **Purpose:** Pre-deployment checks for router and switch configuration, including dangerous commands, duplicate addresses, subnet overlaps, stale references, management-plane risk, and IOS-style security hygiene.
- **When to use:** - Reviewing Cisco IOS or IOS-XE style snippets before deployment. - Auditing generated config from scripts or templates. - Looking for dangerous commands, duplicate IP addresses, or subnet overlaps. - Checking whether ACLs, route-maps, prefix-lists, or line po ...
- **Workflow sections:** When to Use / How It Works / Dangerous Command Detection / Duplicate IPs And Subnet Overlaps / Management-Plane Checks / Security Hygiene Checks / Examples / Anti-Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:network-config-validation`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\network-config-validation\SKILL.md`

##### `network-interface-health`

- **Purpose:** Diagnose interface errors, drops, CRCs, duplex mismatches, flapping, speed negotiation issues, and counter trends on routers, switches, and Linux hosts.
- **When to use:** - A host or VLAN has packet loss, latency spikes, or intermittent reachability. - A switch or router interface shows CRCs, runts, giants, drops, resets, or flaps. - You need to compare both ends of a link before replacing hardware. - A change window needs befo ...
- **Workflow sections:** When to Use / How It Works / Counter Reference / Diagnosis Flow / Safe Parser Example / Examples / Anti-Patterns / See Also
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:network-interface-health`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\network-interface-health\SKILL.md`

##### `opensource-pipeline`

- **Purpose:** Open-source pipeline: fork, sanitize, and package private projects for safe public release. Chains 3 agents (forker, sanitizer, packager). Triggers: '/opensource', 'open source this', 'make this public', 'prepare for open source'.
- **When to use:** - User says "open source this project" or "make this public" - User wants to prepare a private repo for public release - User needs to strip secrets before pushing to GitHub - User invokes `/opensource fork`, `/opensource verify`, or `/opensource package`
- **Workflow sections:** When to Activate / Commands / Protocol / Staging Layout / Anti-Patterns / Best Practices / Related Skills
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:opensource-pipeline`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\opensource-pipeline\SKILL.md`

##### `orch-pipeline`

- **Purpose:** Shared orchestration engine for the orch-* skill family. Defines the gated Research-Plan-TDD-Review-Commit pipeline, the size classifier, the agent map, and the two human gates that the orch-* operation skills delegate to. Not usually invoked directly.
- **When to use:** - Loaded indirectly whenever an `orch-*` operation skill runs. - Read directly only when adding a new operation to the family or tuning the shared phases, gates, or agent map.
- **Workflow sections:** When to Use / The operation family / Step 0 — Classify size (right-sizing) / The phases / The two gates / Agent / command map / Security-review trigger / Handoff artifacts
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:orch-pipeline`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\orch-pipeline\SKILL.md`

##### `project-flow-ops`

- **Purpose:** Operate execution flow across GitHub and Linear by triaging issues and pull requests, linking active work, and keeping GitHub public-facing while Linear remains the internal execution layer. Use when the user wants backlog control, PR triage, or GitHub-to-Linear coordination.
- **When to use:** Use when the user wants backlog control, PR triage, or GitHub-to-Linear coordination.
- **Workflow sections:** When to Use / Operating Model / Core Workflow / Review Rules / Output Format / Good Use Cases
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:project-flow-ops`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\project-flow-ops\SKILL.md`

##### `ralphinho-rfc-pipeline`

- **Purpose:** RFC-driven multi-agent DAG execution pattern with quality gates, merge queues, and work unit orchestration.
- **Workflow sections:** Pipeline Stages / Unit Spec Template / Complexity Tiers / Quality Pipeline per Unit / Merge Queue Rules / Recovery / Outputs
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:ralphinho-rfc-pipeline`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ralphinho-rfc-pipeline\SKILL.md`

##### `recsys-pipeline-architect`

- **Purpose:** Design composable recommendation, ranking, and feed pipelines using the six-stage Source→Hydrator→Filter→Scorer→Selector→SideEffect framework popularized by xAI's open-sourced For You algorithm. Use this skill whenever the user is building any system that picks "the top K items for a (user, context)" — social feeds, content CMSs, RAG rerankers, task prioritizers, notification triage, search rerank ...
- **When to use:** Use this skill whenever the user is building any system that picks "the top K items for a (user, context)" — social feeds, content CMSs, RAG rerankers, task prioritizers, notification triage, search reranking, ad ranking.
- **Workflow sections:** When to Use / When NOT to Use / The six-stage framework / Workflow when invoked / Key trade-offs to surface (don't default silently) / Hard rules / Anti-Patterns / Upstream contents
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:recsys-pipeline-architect`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\recsys-pipeline-architect\SKILL.md`

##### `recursive-decision-ledger`

- **Purpose:** Use when the user asks for repeated rollouts, marked decision processes, high-dimensional search, stochastic optimization, local-optima exploration, ensemble comparison, or recursive reasoning with a visible evidence trail.
- **When to use:** Use when the user asks for repeated rollouts, marked decision processes, high-dimensional search, stochastic optimization, local-optima exploration, ensemble comparison, or recursive reasoning with a visible evidence trail.
- **Workflow sections:** Ledger Contract / Rollout Loop / Coherence Mark / Promotion Rules / Summary Shape
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:recursive-decision-ledger`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\recursive-decision-ledger\SKILL.md`

##### `research-ops`

- **Purpose:** Evidence-first current-state research workflow for ECC. Use when the user wants fresh facts, comparisons, enrichment, or a recommendation built from current public evidence and any supplied local context.
- **When to use:** Use when the user wants fresh facts, comparisons, enrichment, or a recommendation built from current public evidence and any supplied local context.
- **Workflow sections:** Skill Stack / When to Use / Guardrails / Workflow / Output Format / Pitfalls / Verification
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:research-ops`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\research-ops\SKILL.md`

##### `social-graph-ranker`

- **Purpose:** Weighted social-graph ranking for warm intro discovery, bridge scoring, and network gap analysis across X and LinkedIn. Use when the user wants the reusable graph-ranking engine itself, not the broader outreach or network-maintenance workflow layered on top of it.
- **When to use:** Use when the user wants the reusable graph-ranking engine itself, not the broader outreach or network-maintenance workflow layered on top of it.
- **Workflow sections:** When To Use This Standalone / Inputs / Core Model / Scoring Signals / Workflow / Output Shape / Related Skills
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:social-graph-ranker`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\social-graph-ranker\SKILL.md`

##### `taste`

- **Purpose:** A creative-direction (taste) layer for music videos and short-form edits in the angelcore / cloud-trance / hyperpop visual family. Distills a named-genre aesthetic vocabulary, a mood + color + light system, and a beat-synced editing grammar, then chains ECC's video skills (video-editing, fal-ai-media, remotion-video-creation, motion-*, content-engine) into one production pipeline. Use when the wor ...
- **When to use:** Use when the work is not just making a video function but making it feel intentional, when building a music video, a fancam/edit, a moodboard-driven reel, or when choosing a coherent visual direction for AI-generated b-roll.
- **Workflow sections:** When to Activate / Core Thesis / The Aesthetic Vocabulary (distilled) / The Mood System — angelcore × cloud-trance / The Editing Grammar (distilled) / The Pipeline — mixing the ECC video skills / Beat Math (lock cuts to the song) / Beat-Mapped Shot Plan (this music video)
- **Dependencies / tools:** bundled: `references/`; files: `.orphaned_at`
- **Invocation:** `/ecc:taste`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\taste\SKILL.md`

##### `terminal-ops`

- **Purpose:** Evidence-first repo execution workflow for ECC. Use when the user wants a command run, a repo checked, a CI failure debugged, or a narrow fix pushed with exact proof of what was executed and verified.
- **When to use:** Use when the user wants a command run, a repo checked, a CI failure debugged, or a narrow fix pushed with exact proof of what was executed and verified.
- **Workflow sections:** Skill Stack / When to Use / Guardrails / Workflow / Output Format / Pitfalls / Verification
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:terminal-ops`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\terminal-ops\SKILL.md`

##### `uncloud`

- **Purpose:** Use when managing an Uncloud cluster — deploying services, configuring Caddy ingress, adding static proxy routes for non-cluster devices, publishing ports, scaling, inspecting logs, or managing machines and volumes with the `uc` CLI.
- **When to use:** Use when managing an Uncloud cluster — deploying services, configuring Caddy ingress, adding static proxy routes for non-cluster devices, publishing ports, scaling, inspecting logs, or managing machines and volumes with the `uc` CLI.
- **Workflow sections:** When to Activate / How It Works / Examples / Core Concepts / CLI Quick Reference / Port Publishing / Compose File Extensions / Routing to External (Non-Cluster) Devices
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:uncloud`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\uncloud\SKILL.md`

##### `unified-notifications-ops`

- **Purpose:** Operate notifications as one ECC-native workflow across GitHub, Linear, desktop alerts, hooks, and connected communication surfaces. Use when the real problem is alert routing, deduplication, escalation, or inbox collapse.
- **When to use:** Use when the real problem is alert routing, deduplication, escalation, or inbox collapse.
- **Workflow sections:** When to Use / Preferred Surface / Non-Negotiable Rules / Event Pipeline / Default Severity Model / Workflow / Output Format / Recommendation Rules
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:unified-notifications-ops`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\unified-notifications-ops\SKILL.md`

#### Testing & QA (31)

##### `ai-regression-testing`

- **Purpose:** Regression testing strategies for AI-assisted development. Sandbox-mode API testing without database dependencies, automated bug-check workflows, and patterns to catch AI blind spots where the same model writes and reviews code.
- **When to use:** - AI agent (Claude Code, Cursor, Codex) has modified API routes or backend logic - A bug was found and fixed — need to prevent re-introduction - Project has a sandbox/mock mode that can be leveraged for DB-free testing - Running `/bug-check` or similar review ...
- **Workflow sections:** When to Activate / The Core Problem / Sandbox-Mode API Testing / Integrating Tests into Bug-Check Workflow / Step 1: Automated Tests (mandatory, cannot skip) / Step 2: Code Review (AI review) / Step 3: For each bug fixed, propose a regression test / Common AI Regression Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:ai-regression-testing`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ai-regression-testing\SKILL.md`

##### `benchmark`

- **Purpose:** Use this skill to measure performance baselines, detect regressions before/after PRs, and compare stack alternatives.
- **When to use:** - Before and after a PR to measure performance impact - Setting up performance baselines for a project - When users report "it feels slow" - Before a launch — ensure you meet performance targets - Comparing your stack against alternatives
- **Workflow sections:** When to Use / How It Works / Output / Integration
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:benchmark`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\benchmark\SKILL.md`

##### `benchmark-methodology`

- **Purpose:** >- | Use after competitive-platform-analysis has produced a tiered competitor set. | Scores each competitor across nine weighted dimensions (positioning, voice, | visual craft, offer packaging, evidence, enterprise-readiness, thought | leadership, pricing, client's strategic tension) with explicit 1–5 rubrics | and a tension-plot. Precedes competitive-report-structure.
- **When to use:** - A scoped, tiered competitor set from competitive-platform-analysis is ready to score. - Need comparable, evidence-anchored scores across competitors — not gut-feel rankings. - Client's strategic tension (the paired axes defining their target white-space) has ...
- **Workflow sections:** When to Activate / Client positioning brief (establish first) / Why these dimensions / The nine dimensions (with weights) / Scoring rubric (1–5, applies to dimensions 1–8) / How to collect the data / Bias controls / Competitor profile card (output format)
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:benchmark-methodology`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\benchmark-methodology\SKILL.md`

##### `browser-qa`

- **Purpose:** Use this skill to automate visual testing and UI interaction verification using browser automation after deploying features.
- **When to use:** - After deploying a feature to staging/preview - When you need to verify UI behavior across pages - Before shipping — confirm layouts, forms, interactions actually work - When reviewing PRs that touch frontend code - Accessibility audits and responsive testing
- **Workflow sections:** When to Use / How It Works / Output Format / QA Report — [URL] — [timestamp] / Integration
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:browser-qa`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\browser-qa\SKILL.md`

##### `carrier-relationship-management`

- **Purpose:** > | Codified expertise for managing carrier portfolios, negotiating freight rates, | tracking carrier performance, allocating freight, and maintaining strategic | carrier relationships. Informed by transportation managers with 15+ years | experience. Includes scorecarding frameworks, RFP processes, market intelligence, | and compliance vetting. Use when managing carriers, negotiating rates, evalua ...
- **When to use:** Use when managing carriers, negotiating rates, evaluating | carrier performance, or building freight strategies.
- **Workflow sections:** Role and Context / When to Use / How It Works / Examples / Core Knowledge / Decision Frameworks / Key Edge Cases / Communication Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:carrier-relationship-management`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\carrier-relationship-management\SKILL.md`

##### `cpp-testing`

- **Purpose:** Use only when writing/updating/fixing C++ tests, configuring GoogleTest/CTest, diagnosing failing or flaky tests, or adding coverage/sanitizers.
- **When to use:** - Writing new C++ tests or fixing existing tests - Designing unit/integration test coverage for C++ components - Adding test coverage, CI gating, or regression protection - Configuring CMake/CTest workflows for consistent execution - Investigating test failure ...
- **Workflow sections:** When to Use / Core Concepts / TDD Workflow / Code Examples / Running Tests / Debugging Failures / Coverage / Sanitizers
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:cpp-testing`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\cpp-testing\SKILL.md`

##### `csharp-testing`

- **Purpose:** C# and .NET testing patterns with xUnit, FluentAssertions, mocking, integration tests, and test organization best practices.
- **When to use:** - Writing new tests for C# code - Reviewing test quality and coverage - Setting up test infrastructure for .NET projects - Debugging flaky or slow tests
- **Workflow sections:** When to Activate / Test Framework Stack / Unit Test Structure / Mocking with NSubstitute / ASP.NET Core Integration Tests / Test Organization / Test Data Builders / Common Anti-Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:csharp-testing`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\csharp-testing\SKILL.md`

##### `django-tdd`

- **Purpose:** Django testing strategies with pytest-django, TDD methodology, factory_boy, mocking, coverage, and testing Django REST Framework APIs.
- **When to use:** - Writing new Django applications - Implementing Django REST Framework APIs - Testing Django models, views, and serializers - Setting up testing infrastructure for Django projects
- **Workflow sections:** When to Activate / TDD Workflow for Django / Setup / Factory Boy / Model Testing / View Testing / DRF API Testing / Mocking and Patching
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:django-tdd`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\django-tdd\SKILL.md`

##### `django-verification`

- **Purpose:** Verification loop for Django projects: migrations, linting, tests with coverage, security scans, and deployment readiness checks before release or PR.
- **When to use:** - Before opening a pull request for a Django project - After major model changes, migration updates, or dependency upgrades - Pre-deployment verification for staging or production - Running full environment → lint → test → security → deploy readiness pipeline ...
- **Workflow sections:** When to Activate / Phase 1: Environment Check / Phase 2: Code Quality & Formatting / Phase 3: Migrations / Phase 4: Tests + Coverage / Phase 5: Security Scan / Phase 6: Django Management Commands / Phase 7: Performance Checks
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:django-verification`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\django-verification\SKILL.md`

##### `e2e-testing`

- **Purpose:** Playwright E2E testing patterns, Page Object Model, configuration, CI/CD integration, artifact management, and flaky test strategies.
- **Workflow sections:** Test File Organization / Page Object Model (POM) / Test Structure / Playwright Configuration / Flaky Test Patterns / Artifact Management / CI/CD Integration / Test Report Template
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:e2e-testing`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\e2e-testing\SKILL.md`

##### `energy-procurement`

- **Purpose:** > | Codified expertise for electricity and gas procurement, tariff optimization, | demand charge management, renewable PPA evaluation, and multi-facility energy | cost management. Informed by energy procurement managers with 15+ years | experience at large commercial and industrial consumers. Includes market | structure analysis, hedging strategies, load profiling, and sustainability | reporting f ...
- **When to use:** Use when procuring energy, optimizing tariffs, managing | demand charges, evaluating PPAs, or developing energy strategies.
- **Workflow sections:** Role and Context / When to Use / How It Works / Examples / Core Knowledge / Decision Frameworks / Key Edge Cases / Communication Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:energy-procurement`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\energy-procurement\SKILL.md`

##### `fsharp-testing`

- **Purpose:** F# testing patterns with xUnit, FsUnit, Unquote, FsCheck property-based testing, integration tests, and test organization best practices.
- **When to use:** - Writing new tests for F# code - Reviewing test quality and coverage - Setting up test infrastructure for F# projects - Debugging flaky or slow tests
- **Workflow sections:** When to Activate / Test Framework Stack / Unit Tests with xUnit + FsUnit / Property-Based Testing with FsCheck / Mocking Dependencies / ASP.NET Core Integration Tests / Test Organization / Common Anti-Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:fsharp-testing`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\fsharp-testing\SKILL.md`

##### `golang-testing`

- **Purpose:** Go testing patterns including table-driven tests, subtests, benchmarks, fuzzing, and test coverage. Follows TDD methodology with idiomatic Go practices.
- **When to use:** - Writing new Go functions or methods - Adding test coverage to existing code - Creating benchmarks for performance-critical code - Implementing fuzz tests for input validation - Following TDD workflow in Go projects
- **Workflow sections:** When to Activate / TDD Workflow for Go / Table-Driven Tests / Subtests and Sub-benchmarks / Test Helpers / Golden Files / Mocking with Interfaces / Benchmarks
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:golang-testing`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\golang-testing\SKILL.md`

##### `iterative-retrieval`

- **Purpose:** Pattern for progressively refining context retrieval to solve the subagent context problem
- **When to use:** - Spawning subagents that need codebase context they cannot predict upfront - Building multi-agent workflows where context is progressively refined - Encountering "context too large" or "missing context" failures in agent tasks - Designing RAG-like retrieval p ...
- **Workflow sections:** When to Activate / The Problem / The Solution: Iterative Retrieval / Practical Examples / Integration with Agents / Best Practices / Related
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:iterative-retrieval`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\iterative-retrieval\SKILL.md`

##### `kotlin-testing`

- **Purpose:** Kotlin testing patterns with Kotest, MockK, coroutine testing, property-based testing, and Kover coverage. Follows TDD methodology with idiomatic Kotlin practices.
- **When to use:** - Writing new Kotlin functions or classes - Adding test coverage to existing Kotlin code - Implementing property-based tests - Following TDD workflow in Kotlin projects - Configuring Kover for code coverage
- **Workflow sections:** When to Use / How It Works / Examples
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:kotlin-testing`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\kotlin-testing\SKILL.md`

##### `laravel-tdd`

- **Purpose:** Laravel testing strategies with PHPUnit, Pest, model factories, HTTP tests, Sanctum authentication testing, mocking, and coverage.
- **When to use:** - Writing new Laravel applications or features - Implementing API endpoints with Sanctum or Passport authentication - Testing Eloquent models, relationships, scopes, and accessors - Setting up testing infrastructure for Laravel projects - Writing feature tests ...
- **Workflow sections:** When to Activate / TDD Workflow for Laravel / Setup / Model Factories / Model Testing / Feature / HTTP Testing / JSON API Testing / Sanctum API Auth Testing
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:laravel-tdd`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\laravel-tdd\SKILL.md`

##### `laravel-verification`

- **Purpose:** Verification loop for Laravel projects: env checks, linting, static analysis, tests with coverage, security scans, and deployment readiness.
- **When to use:** - Before opening a pull request for a Laravel project - After major refactors or dependency upgrades - Pre-deployment verification for staging or production - Running full lint -> test -> security -> deploy readiness pipeline
- **Workflow sections:** When to Use / How It Works / Phase 1: Environment Checks / Phase 1.5: Composer and Autoload / Phase 2: Linting and Static Analysis / Phase 3: Tests and Coverage / Phase 4: Security and Dependency Checks / Phase 5: Database and Migrations
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:laravel-verification`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\laravel-verification\SKILL.md`

##### `mle-workflow`

- **Purpose:** Production machine-learning engineering workflow for data contracts, reproducible training, model evaluation, deployment, monitoring, and rollback. Use when building, reviewing, or hardening ML systems beyond one-off notebooks.
- **When to use:** Use when building, reviewing, or hardening ML systems beyond one-off notebooks.
- **Workflow sections:** When to Activate / Scope Calibration / Related Skills / Reuse the SWE Surface / Ten MLE Task Simulations / Iteration Compact / Decision Brain / Metric and Mistake Economics
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:mle-workflow`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\mle-workflow\SKILL.md`

##### `perl-testing`

- **Purpose:** Perl testing patterns using Test2::V0, Test::More, prove runner, mocking, coverage with Devel::Cover, and TDD methodology.
- **When to use:** - Writing new Perl code (follow TDD: red, green, refactor) - Designing test suites for Perl modules or applications - Reviewing Perl test coverage - Setting up Perl testing infrastructure - Migrating tests from Test::More to Test2::V0 - Debugging failing Perl ...
- **Workflow sections:** When to Activate / TDD Workflow / Test::More Fundamentals / Test2::V0 Modern Framework / Test Organization and prove / Fixtures and Setup/Teardown / Mocking / Coverage with Devel::Cover
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:perl-testing`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\perl-testing\SKILL.md`

##### `product-lens`

- **Purpose:** Use this skill to validate the "why" before building, run product diagnostics, and pressure-test product direction before the request becomes an implementation contract.
- **When to use:** - Before starting any feature — validate the "why" - Weekly product review — are we building the right thing? - When stuck choosing between features - Before a launch — sanity check the user journey - When converting a vague idea into a product brief before en ...
- **Workflow sections:** When to Use / How It Works / Output / Integration
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:product-lens`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\product-lens\SKILL.md`

##### `python-testing`

- **Purpose:** Python testing strategies using pytest, TDD methodology, fixtures, mocking, parametrization, and coverage requirements.
- **When to use:** - Writing new Python code (follow TDD: red, green, refactor) - Designing test suites for Python projects - Reviewing Python test coverage - Setting up testing infrastructure
- **Workflow sections:** When to Activate / Core Testing Philosophy / pytest Fundamentals / Fixtures / Parametrization / Markers and Test Selection / Mocking and Patching / Testing Async Code
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:python-testing`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\python-testing\SKILL.md`

##### `quarkus-tdd`

- **Purpose:** Test-driven development for Quarkus 3.x LTS using JUnit 5, Mockito, REST Assured, Camel testing, and JaCoCo. Use when adding features, fixing bugs, or refactoring event-driven services.
- **When to use:** Use when adding features, fixing bugs, or refactoring event-driven services.
- **Workflow sections:** When to Use / Workflow / Unit Tests with @Nested Organization / Testing Camel Routes / Testing Event Services / Testing CompletableFuture / Resource Layer Tests (REST Assured) / Integration Tests with Real Database
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:quarkus-tdd`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\quarkus-tdd\SKILL.md`

##### `quarkus-verification`

- **Purpose:** Verification loop for Quarkus projects: build, static analysis, tests with coverage, security scans, native compilation, and diff review before release or PR.
- **When to use:** - Before opening a pull request for a Quarkus service - After major refactoring or dependency upgrades - Pre-deployment verification for staging or production - Running full build → lint → test → security scan → native compilation pipeline - Validating test co ...
- **Workflow sections:** When to Activate / Phase 1: Build / Phase 2: Static Analysis / Phase 3: Tests + Coverage / Phase 4: Security Scanning / Phase 5: Native Compilation / Phase 6: Performance Testing / Phase 7: Health Checks
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:quarkus-verification`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\quarkus-verification\SKILL.md`

##### `react-testing`

- **Purpose:** React component testing with React Testing Library, Vitest/Jest, MSW for network mocking, accessibility assertions with axe, and the decision boundary between component tests and Playwright/Cypress end-to-end runs. Use when writing or fixing tests for React components, hooks, or pages.
- **When to use:** Use when writing or fixing tests for React components, hooks, or pages.
- **Workflow sections:** When to Activate / Core Principle / Library Choice / Query Priority / User Interaction with `userEvent` / Async Patterns / Network Mocking with MSW / Provider Wrapping
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:react-testing`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\react-testing\SKILL.md`

##### `rust-testing`

- **Purpose:** Rust testing patterns including unit tests, integration tests, async testing, property-based testing, mocking, and coverage. Follows TDD methodology.
- **When to use:** - Writing new Rust functions, methods, or traits - Adding test coverage to existing code - Creating benchmarks for performance-critical code - Implementing property-based tests for input validation - Following TDD workflow in Rust projects
- **Workflow sections:** When to Use / How It Works / TDD Workflow for Rust / Unit Tests / Error and Panic Testing / Integration Tests / Async Tests / Test Organization Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:rust-testing`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\rust-testing\SKILL.md`

##### `scholar-evaluation`

- **Purpose:** Structured scholarly-work evaluation for papers, proposals, literature reviews, methods sections, evidence quality, citation support, and research-writing feedback.
- **When to use:** - Reviewing a research paper, proposal, thesis chapter, or literature review. - Checking whether claims are supported by cited evidence. - Evaluating methodology, study design, analysis, or limitations. - Comparing two or more papers for quality or relevance. ...
- **Workflow sections:** When to Use / Evaluation Scope / Rubric / Review Process / Output Template / Overall Assessment / Dimension Scores / Critical Issues
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:scholar-evaluation`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\scientific-thinking-scholar-evaluation\SKILL.md`

##### `springboot-tdd`

- **Purpose:** Test-driven development for Spring Boot using JUnit 5, Mockito, MockMvc, Testcontainers, and JaCoCo. Use when adding features, fixing bugs, or refactoring.
- **When to use:** Use when adding features, fixing bugs, or refactoring.
- **Workflow sections:** When to Use / Workflow / Unit Tests (JUnit 5 + Mockito) / Web Layer Tests (MockMvc) / Integration Tests (SpringBootTest) / Persistence Tests (DataJpaTest) / Testcontainers / Coverage (JaCoCo)
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:springboot-tdd`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\springboot-tdd\SKILL.md`

##### `springboot-verification`

- **Purpose:** Verification loop for Spring Boot projects: build, static analysis, tests with coverage, security scans, and diff review before release or PR.
- **When to use:** - Before opening a pull request for a Spring Boot service - After major refactoring or dependency upgrades - Pre-deployment verification for staging or production - Running full build → lint → test → security scan pipeline - Validating test coverage meets thre ...
- **Workflow sections:** When to Activate / Phase 1: Build / Phase 2: Static Analysis / Phase 3: Tests + Coverage / Phase 4: Security Scan / Phase 5: Lint/Format (optional gate) / Phase 6: Diff Review / Output Template
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:springboot-verification`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\springboot-verification\SKILL.md`

##### `swift-protocol-di-testing`

- **Purpose:** Protocol-based dependency injection for testable Swift code — mock file system, network, and external APIs using focused protocols and Swift Testing.
- **When to use:** - Writing Swift code that accesses file system, network, or external APIs - Need to test error handling paths without triggering real failures - Building modules that work across environments (app, test, SwiftUI preview) - Designing testable architecture with ...
- **Workflow sections:** When to Activate / Core Pattern / Best Practices / Anti-Patterns to Avoid / When to Use
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:swift-protocol-di-testing`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\swift-protocol-di-testing\SKILL.md`

##### `tdd-workflow`

- **Purpose:** Use this skill when writing new features, fixing bugs, or refactoring code. Enforces test-driven development with 80%+ coverage including unit, integration, and E2E tests.
- **When to use:** Use this skill when writing new features, fixing bugs, or refactoring code.
- **Workflow sections:** When to Activate / Plan Handoff / Core Principles / TDD Workflow Steps / Testing Patterns / Test File Organization / Mocking External Services / Test Coverage Verification
- **Dependencies / tools:** files: `.orphaned_at`; argument-hint: `<path/to/*.plan.md>`
- **Invocation:** `/ecc:tdd-workflow`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\tdd-workflow\SKILL.md`

##### `windows-desktop-e2e`

- **Purpose:** E2E testing for Windows native desktop apps (WPF, WinForms, Win32/MFC, Qt) using pywinauto and Windows UI Automation.
- **When to use:** - Writing or running E2E tests for a Windows native desktop application - Setting up a desktop GUI test suite from scratch - Diagnosing flaky or failing desktop automation tests - Adding testability (AutomationId, accessible names) to an existing app - Integra ...
- **Workflow sections:** When to Activate / Core Concepts / Setup & Prerequisites / Testability Setup (by Framework) / Page Object Model / Locator Strategy / Wait Patterns / Artifact Management
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:windows-desktop-e2e`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\windows-desktop-e2e\SKILL.md`

#### Frontend, design & media (26)

##### `accessibility`

- **Purpose:** Design, implement, and audit inclusive digital products using WCAG 2.2 Level AA | standards. Use this skill to generate semantic ARIA for Web and accessibility traits for Web and Native platforms (iOS/Android).
- **When to use:** - Defining UI component specifications for Web, iOS, or Android. - Auditing existing code for accessibility barriers or compliance gaps. - Implementing new WCAG 2.2 standards like Target Size (Minimum) and Focus Appearance. - Mapping high-level design requirem ...
- **Workflow sections:** When to Use / Core Concepts / How It Works / Accessibility Architecture Diagram / Cross-Platform Mapping / Examples / Anti-Patterns to Avoid / Best Practices Checklist
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:accessibility`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\accessibility\SKILL.md`

##### `api-connector-builder`

- **Purpose:** Build a new API connector or provider by matching the target repo's existing integration pattern exactly. Use when adding one more integration without inventing a second architecture.
- **When to use:** Use when adding one more integration without inventing a second architecture.
- **Workflow sections:** When to Use / Guardrails / Workflow / Reference Shapes / Quality Checklist / Related Skills
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:api-connector-builder`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\api-connector-builder\SKILL.md`

##### `api-design`

- **Purpose:** REST API design patterns including resource naming, status codes, pagination, filtering, error responses, versioning, and rate limiting for production APIs.
- **When to use:** - Designing new API endpoints - Reviewing existing API contracts - Adding pagination, filtering, or sorting - Implementing error handling for APIs - Planning API versioning strategy - Building public or partner-facing APIs
- **Workflow sections:** When to Activate / Resource Design / HTTP Methods and Status Codes / Response Format / Pagination / Filtering, Sorting, and Search / Authentication and Authorization / Rate Limiting
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:api-design`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\api-design\SKILL.md`

##### `blender-motion-state-inspection`

- **Purpose:** Use this skill when inspecting Blender characters, rigs, poses, animation retargeting, ground contact, facing direction, or model-vs-motion alignment where screenshots alone are not enough.
- **When to use:** Use this skill when inspecting Blender characters, rigs, poses, animation retargeting, ground contact, facing direction, or model-vs-motion alignment where screenshots alone are not enough.
- **Workflow sections:** When to Use / Core Principle / How It Works / Inspection Workflow / Recommended Report Shape / Blender Motion Inspection / Examples / Practical Thresholds
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:blender-motion-state-inspection`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\blender-motion-state-inspection\SKILL.md`

##### `brand-discovery`

- **Purpose:** >- | Use when a brand needs to discover or articulate its identity through | structured multi-session interviews. Covers purpose, positioning, audience, | personality, voice, narrative, and founder-brand tension across 8 modules | using laddering, 5 Whys, and projective techniques. Produces a resumable | session with disk-persisted state and a master brandbook (90_SYNTHESIS.md).
- **When to use:** Use when a brand needs to discover or articulate its identity through | structured multi-session interviews.
- **Workflow sections:** When to Activate / Session start protocol / Interview discipline / Module sequence / State write protocol / Multi-founder mode / Anti-Patterns / Related Skills
- **Dependencies / tools:** bundled: `references/`; files: `.orphaned_at`
- **Invocation:** `/ecc:brand-discovery`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\brand-discovery\SKILL.md`

##### `brand-voice`

- **Purpose:** Build a source-derived writing style profile from real posts, essays, launch notes, docs, or site copy, then reuse that profile across content, outreach, and social workflows. Use when the user wants voice consistency without generic AI writing tropes.
- **When to use:** Use when the user wants voice consistency without generic AI writing tropes.
- **Workflow sections:** When to Activate / Source Priority / Collection Workflow / What to Extract / Output Contract / Affaan / ECC Defaults / Hard Bans / Persistence Rules
- **Dependencies / tools:** bundled: `references/`; files: `.orphaned_at`
- **Invocation:** `/ecc:brand-voice`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\brand-voice\SKILL.md`

##### `dashboard-builder`

- **Purpose:** Build monitoring dashboards that answer real operator questions for Grafana, SigNoz, and similar platforms. Use when turning metrics into a working dashboard instead of a vanity board.
- **When to use:** Use when turning metrics into a working dashboard instead of a vanity board.
- **Workflow sections:** When to Use / Guardrails / Workflow / Example Panel Sets / Quality Checklist / Related Skills
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:dashboard-builder`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\dashboard-builder\SKILL.md`

##### `design-system`

- **Purpose:** Use this skill to generate or audit design systems, check visual consistency, and review PRs that touch styling.
- **When to use:** - Starting a new project that needs a design system - Auditing an existing codebase for visual consistency - Before a redesign — understand what you have - When the UI looks "off" but you can't pinpoint why - Reviewing PRs that touch styling
- **Workflow sections:** When to Use / How It Works / Examples
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:design-system`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\design-system\SKILL.md`

##### `ecc-guide`

- **Purpose:** Guide users through ECC's current agents, skills, commands, hooks, rules, install profiles, and project onboarding by reading the live repository surface before answering.
- **Workflow sections:** When To Use / Core Principle / Repository Map / Response Style / Common Tasks / Output Templates / Related Surfaces
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:ecc-guide`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ecc-guide\SKILL.md`

##### `fal-ai-media`

- **Purpose:** Unified media generation via fal.ai MCP — image, video, and audio. Covers text-to-image (Nano Banana), text/image-to-video (Seedance, Kling, Veo 3), text-to-speech (CSM-1B), and video-to-audio (ThinkSound). Use when the user wants to generate images, videos, or audio with AI.
- **When to use:** Use when the user wants to generate images, videos, or audio with AI.
- **Workflow sections:** When to Activate / MCP Requirement / MCP Tools / Image Generation / Video Generation / Audio Generation / Cost Estimation / Model Discovery
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:fal-ai-media`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\fal-ai-media\SKILL.md`

##### `foundation-models-on-device`

- **Purpose:** Apple FoundationModels framework for on-device LLM — text generation, guided generation with @Generable, tool calling, and snapshot streaming in iOS 26+.
- **When to use:** - Building AI-powered features using Apple Intelligence on-device - Generating or summarizing text without cloud dependency - Extracting structured data from natural language input - Implementing custom tool calling for domain-specific AI actions - Streaming s ...
- **Workflow sections:** When to Activate / Core Pattern — Availability Check / Core Pattern — Basic Session / Core Pattern — Guided Generation with @Generable / Core Pattern — Tool Calling / Core Pattern — Snapshot Streaming / Key Design Decisions / Best Practices
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:foundation-models-on-device`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\foundation-models-on-device\SKILL.md`

##### `frontend-a11y`

- **Purpose:** > | Accessibility patterns for React and Next.js — semantic HTML, ARIA attributes, | form labeling, keyboard navigation, focus management, and screen reader support. | Use when building any interactive UI component or form.
- **When to use:** Use when building any interactive UI component or form.
- **Workflow sections:** When to Activate / Form Accessibility / Semantic HTML / ARIA Attributes / Keyboard Navigation / Focus Management / Images and Icons / Reduced Motion
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:frontend-a11y`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\frontend-a11y\SKILL.md`

##### `frontend-design-direction`

- **Purpose:** Set an ECC-specific frontend design direction for production UI work. Use when building or improving websites, dashboards, applications, components, landing pages, visual tools, or any web UI that needs stronger product-specific design judgment.
- **When to use:** Use when building or improving websites, dashboards, applications, components, landing pages, visual tools, or any web UI that needs stronger product-specific design judgment.
- **Workflow sections:** When to Use / Design Direction / Implementation Guidance / Anti-Patterns / Review Checklist
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:frontend-design-direction`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\frontend-design-direction\SKILL.md`

##### `frontend-slides`

- **Purpose:** Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. Use when the user wants to build a presentation, convert a PPT/PPTX to web, or create slides for a talk/pitch. Helps non-designers discover their aesthetic through visual exploration rather than abstract choices.
- **When to use:** Use when the user wants to build a presentation, convert a PPT/PPTX to web, or create slides for a talk/pitch.
- **Workflow sections:** When to Activate / Non-Negotiables / Workflow / PPT / PPTX Conversion / Implementation Requirements / Content Density Limits / Anti-Patterns / Related ECC Skills
- **Dependencies / tools:** bundled: `scripts/`; files: `.orphaned_at`, `STYLE_PRESETS.md`, `animation-patterns.md`, `html-template.md`, `viewport-base.css`
- **Invocation:** `/ecc:frontend-slides`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\frontend-slides\SKILL.md`

##### `ios-icon-gen`

- **Purpose:** Generate iOS app icons as PNG imagesets for Xcode asset catalogs from SF Symbols (5000+ Apple-native) or Iconify API (275k+ open source icons from 200+ collections). Use when generating icons, creating icon assets, adding icons to asset catalog, or searching for icons for iOS projects.
- **When to use:** Use when generating icons, creating icon assets, adding icons to asset catalog, or searching for icons for iOS projects.
- **Workflow sections:** When to Activate / Core Principles / Examples / Popular Iconify Collections / Scripts Reference / Best Practices / Anti-Patterns
- **Dependencies / tools:** bundled: `scripts/`; files: `.orphaned_at`
- **Invocation:** `/ecc:ios-icon-gen`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ios-icon-gen\SKILL.md`

##### `liquid-glass-design`

- **Purpose:** iOS 26 Liquid Glass design system — dynamic glass material with blur, reflection, and interactive morphing for SwiftUI, UIKit, and WidgetKit.
- **When to use:** - Building or updating apps for iOS 26+ with the new design language - Implementing glass-style buttons, cards, toolbars, or containers - Creating morphing transitions between glass elements - Applying Liquid Glass effects to widgets - Migrating existing blur/ ...
- **Workflow sections:** When to Activate / Core Pattern — SwiftUI / Core Pattern — UIKit / Core Pattern — WidgetKit / Key Design Decisions / Best Practices / Anti-Patterns to Avoid / When to Use
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:liquid-glass-design`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\liquid-glass-design\SKILL.md`

##### `make-interfaces-feel-better`

- **Purpose:** Apply concrete design-engineering details that make interfaces feel polished. Use when reviewing or improving UI spacing, typography, borders, shadows, motion, hit areas, icons, text wrapping, and interaction states.
- **When to use:** Use when reviewing or improving UI spacing, typography, borders, shadows, motion, hit areas, icons, text wrapping, and interaction states.
- **Workflow sections:** When to Use / Core Principles / Review Output / Checklist
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:make-interfaces-feel-better`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\make-interfaces-feel-better\SKILL.md`

##### `manim-video`

- **Purpose:** Build reusable Manim explainers for technical concepts, graphs, system diagrams, and product walkthroughs, then hand off to the wider ECC video stack if needed. Use when the user wants a clean animated explainer rather than a generic talking-head script.
- **When to use:** Use when the user wants a clean animated explainer rather than a generic talking-head script.
- **Workflow sections:** When to Activate / Tool Requirements / Default Output / Workflow / Scene Planning Rules / Network Graph Default / Render Conventions / Reusable Starter
- **Dependencies / tools:** bundled: `assets/`; files: `.orphaned_at`
- **Invocation:** `/ecc:manim-video`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\manim-video\SKILL.md`

##### `motion-ui`

- **Purpose:** Production-ready UI motion system for React/Next.js. Use when implementing animations, transitions, or motion patterns.
- **When to use:** Use when implementing animations, transitions, or motion patterns.
- **Workflow sections:** When to Use / How It Works / Examples
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:motion-ui`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\motion-ui\SKILL.md`

##### `orch-build-mvp`

- **Purpose:** Orchestrate bootstrapping a working MVP from a design or spec document — ingest the doc, plan thin vertical slices, scaffold the first end-to-end slice, then TDD-implement, review, and gated commit. Use to turn an SDD/PRD into a running starting point.
- **When to use:** - The user has a **design / spec document** (SDD, PRD, system_design) and wants a working vertical slice bootstrapped from it. - Takes a doc path as its argument, e.g. `civicpulse/docs/SDD-v0.6.md`.
- **Workflow sections:** When to Use / Operation settings / How It Works / Example
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:orch-build-mvp`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\orch-build-mvp\SKILL.md`

##### `remotion-video-creation`

- **Purpose:** Best practices for Remotion - Video creation in React. 29 domain-specific rules covering 3D, animations, audio, captions, charts, transitions, and more.
- **When to use:** Use this skills whenever you are dealing with Remotion code to obtain the domain-specific knowledge.
- **Workflow sections:** When to use / How to use
- **Dependencies / tools:** files: `.orphaned_at`, `rules/`
- **Invocation:** `/ecc:remotion-video-creation`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\remotion-video-creation\SKILL.md`

##### `skill-scout`

- **Purpose:** Search existing local, marketplace, GitHub, and web skill sources before creating a new skill. Use when the user wants to create, build, fork, or find a skill for a workflow.
- **When to use:** Use when the user wants to create, build, fork, or find a skill for a workflow.
- **Workflow sections:** When to Use / How It Works / Examples / Anti-Patterns / Related
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:skill-scout`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\skill-scout\SKILL.md`

##### `team-builder`

- **Purpose:** Interactive agent picker for composing and dispatching parallel teams
- **When to use:** - You have multiple agent personas (markdown files) and want to pick which ones to use for a task - You want to compose an ad-hoc team from different domains (e.g., Security + SEO + Architecture) - You want to browse what agents are available before deciding
- **Workflow sections:** When to Use / Prerequisites / Configuration / How It Works / Rules / Examples / Security Engineer Findings / SEO Specialist Findings
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:team-builder`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\team-builder\SKILL.md`

##### `ui-demo`

- **Purpose:** Record polished UI demo videos using Playwright. Use when the user asks to create a demo, walkthrough, screen recording, or tutorial video of a web application. Produces WebM videos with visible cursor, natural pacing, and professional feel.
- **When to use:** Use when the user asks to create a demo, walkthrough, screen recording, or tutorial video of a web application.
- **Workflow sections:** When to Use / Three-Phase Process / Phase 1: Discover / Phase 2: Rehearse / Phase 3: Record / Script Template / Checklist Before Recording / Common Pitfalls
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:ui-demo`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ui-demo\SKILL.md`

##### `video-editing`

- **Purpose:** AI-assisted video editing workflows for cutting, structuring, and augmenting real footage. Covers the full pipeline from raw capture through FFmpeg, Remotion, ElevenLabs, fal.ai, and final polish in Descript or CapCut. Use when the user wants to edit video, cut footage, create vlogs, or build video content.
- **When to use:** Use when the user wants to edit video, cut footage, create vlogs, or build video content.
- **Workflow sections:** When to Activate / Core Thesis / The Pipeline / Layer 1: Capture (Screen Studio / Raw Footage) / Layer 2: Organization (Claude / Codex) / Layer 3: Deterministic Cuts (FFmpeg) / Layer 4: Programmable Composition (Remotion) / Layer 5: Generated Assets (ElevenLabs / fal.ai)
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:video-editing`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\video-editing\SKILL.md`

##### `videodb`

- **Purpose:** See, Understand, Act on video and audio. See- ingest from local files, URLs, RTSP/live feeds, or live record desktop; return realtime context and playable stream links. Understand- extract frames, build visual/semantic/temporal indexes, and search moments with timestamps and auto-clips. Act- transcode and normalize (codec, fps, resolution, aspect ratio), perform timeline edits (subtitles, text/ima ...
- **When to use:** ### Desktop Perception - Start/stop a **desktop session** capturing **screen, mic, and system audio** - Stream **live context** and store **episodic session memory** - Run **real-time alerts/triggers** on what's spoken and what's happening on screen - Produce ...
- **Workflow sections:** When to use / How it works / Error handling / Examples / Additional docs / Provenance
- **Dependencies / tools:** allowed-tools: `Read Grep Glob Bash(python:*)`; bundled: `reference/`, `scripts/`; files: `.orphaned_at`; argument-hint: `[task description]`
- **Invocation:** `/ecc:videodb`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\videodb\SKILL.md`

#### Security & compliance (24)

##### `automation-audit-ops`

- **Purpose:** Evidence-first automation inventory and overlap audit workflow for ECC. Use when the user wants to know which jobs, hooks, connectors, MCP servers, or wrappers are live, broken, redundant, or missing before fixing anything.
- **When to use:** Use when the user wants to know which jobs, hooks, connectors, MCP servers, or wrappers are live, broken, redundant, or missing before fixing anything.
- **Workflow sections:** Skill Stack / When to Use / Guardrails / Workflow / Output Format / Pitfalls / Verification
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:automation-audit-ops`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\automation-audit-ops\SKILL.md`

##### `click-path-audit`

- **Purpose:** Trace every user-facing button/touchpoint through its full state change sequence to find bugs where functions individually work but cancel each other out, produce wrong final state, or leave the UI in an inconsistent state. Use when: systematic debugging found no bugs but users report broken buttons, or after any major refactor touching shared state stores.
- **When to use:** Use when: systematic debugging found no bugs but users report broken buttons, or after any major refactor touching shared state stores.
- **Workflow sections:** The Problem This Solves / How It Works / Execution Steps / Scope Control / When to Use / When NOT to Use / Integration with Other Skills / Example: The Bug That Inspired This Skill
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:click-path-audit`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\click-path-audit\SKILL.md`

##### `config-gc`

- **Purpose:** Garbage collection for your Claude Code configuration. Periodically scans ~/.claude (skills, memory, hooks, permissions, MCP servers, caches) for redundant, stale, orphaned, or low-value items, then walks the user through a confirm-each-deletion cleanup. Use when the user says "clean up my config", "config GC", "too many skills", "audit my setup", "my .claude is bloated", or asks for a periodic co ...
- **When to use:** Use when the user says "clean up my config", "config GC", "too many skills", "audit my setup", "my .
- **Workflow sections:** When to Activate / Design Philosophy / Scan Channels / Workflow / Example Scan Commands / Anti-Patterns / Best Practices / Related Skills
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:config-gc`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\config-gc\SKILL.md`

##### `customs-trade-compliance`

- **Purpose:** > | Codified expertise for customs documentation, tariff classification, duty | optimization, restricted party screening, and regulatory compliance across | multiple jurisdictions. Informed by trade compliance specialists with 15+ | years experience. Includes HS classification logic, Incoterms application, | FTA utilization, and penalty mitigation. Use when handling customs clearance, | tariff cla ...
- **When to use:** Use when handling customs clearance, | tariff classification, trade compliance, import/export documentation, or | duty optimization.
- **Workflow sections:** Role and Context / When to Use / How It Works / Examples / Core Knowledge / Decision Frameworks / Key Edge Cases / Communication Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:customs-trade-compliance`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\customs-trade-compliance\SKILL.md`

##### `defi-amm-security`

- **Purpose:** Security checklist for Solidity AMM contracts, liquidity pools, and swap flows. Covers reentrancy, CEI ordering, donation or inflation attacks, oracle manipulation, slippage, admin controls, and integer math.
- **When to use:** - Writing or auditing a Solidity AMM or liquidity-pool contract - Implementing swap, deposit, withdraw, mint, or burn flows that hold token balances - Reviewing any contract that uses `token.balanceOf(address(this))` in share or reserve math - Adding fee sette ...
- **Workflow sections:** When to Use / How It Works / Execution Safety / Examples / Security Checklist / Audit Tools
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:defi-amm-security`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\defi-amm-security\SKILL.md`

##### `delivery-gate`

- **Purpose:** Stop hook that blocks Claude from finishing until quality checks pass. Detects rationalization patterns (surface text heuristics), stale learning logs (filesystem mtime), and low disk space. Complements self-audit by mechanically enforcing learning capture habits.
- **Workflow sections:** What It Checks / Why / Install / Learning Libraries / Configuration / Examples / Limitations / Compatibility
- **Dependencies / tools:** files: `.orphaned_at`, `hooks/`
- **Invocation:** `/ecc:delivery-gate`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\delivery-gate\SKILL.md`

##### `django-security`

- **Purpose:** Django security best practices, authentication, authorization, CSRF protection, SQL injection prevention, XSS prevention, and secure deployment configurations.
- **When to use:** - Setting up Django authentication and authorization - Implementing user permissions and roles - Configuring production security settings - Reviewing Django application for security issues - Deploying Django applications to production
- **Workflow sections:** When to Activate / Core Security Settings / Authentication / Authorization / SQL Injection Prevention / XSS Prevention / CSRF Protection / File Upload Security
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:django-security`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\django-security\SKILL.md`

##### `ecc-tools-cost-audit`

- **Purpose:** Evidence-first ECC Tools burn and billing audit workflow. Use when investigating runaway PR creation, quota bypass, premium-model leakage, duplicate jobs, or GitHub App cost spikes in the ECC Tools repo.
- **When to use:** Use when investigating runaway PR creation, quota bypass, premium-model leakage, duplicate jobs, or GitHub App cost spikes in the ECC Tools repo.
- **Workflow sections:** Skill Stack / When To Use / Scope Guardrails / Workflow / High-Signal Failure Patterns / Pitfalls / Verification
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:ecc-tools-cost-audit`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ecc-tools-cost-audit\SKILL.md`

##### `healthcare-phi-compliance`

- **Purpose:** Protected Health Information (PHI) and Personally Identifiable Information (PII) compliance patterns for healthcare applications. Covers data classification, access control, audit trails, encryption, and common leak vectors.
- **When to use:** - Building any feature that touches patient records - Implementing access control or authentication for clinical systems - Designing database schemas for healthcare data - Building APIs that return patient or clinician data - Implementing audit trails or loggi ...
- **Workflow sections:** When to Use / How It Works / Examples
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:healthcare-phi-compliance`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\healthcare-phi-compliance\SKILL.md`

##### `hipaa-compliance`

- **Purpose:** HIPAA-specific entrypoint for healthcare privacy and security work. Use when a task is explicitly framed around HIPAA, PHI handling, covered entities, BAAs, breach posture, or US healthcare compliance requirements.
- **When to use:** Use when a task is explicitly framed around HIPAA, PHI handling, covered entities, BAAs, breach posture, or US healthcare compliance requirements.
- **Workflow sections:** When to Use / How It Works / HIPAA-Specific Guardrails / Examples / Related Skills
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:hipaa-compliance`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\hipaa-compliance\SKILL.md`

##### `ito-compute`

- **Purpose:** Query live GPU inventory, submit an authenticated Itô fixed-rate RFQ, inspect RFQ or procurement status, revoke device credentials, and run explicitly gated node qualification through the separately installed canonical CLI. Use when a user asks to find H100/H200 capacity, request a fixed compute rate, check Itô compute status, validate GPU nodes, revoke Itô access, or rent or purchase GPU compute ...
- **When to use:** Use when a user asks to find H100/H200 capacity, request a fixed compute rate, check Itô compute status, validate GPU nodes, revoke Itô access, or rent or purchase GPU compute and needs the supported boundary explained.
- **Workflow sections:** Install the canonical local package / CLI workflow / Live node qualification / MCP workflow / Rent or purchase semantics / Unsupported operations
- **Dependencies / tools:** files: `.orphaned_at`, `agents/`
- **Invocation:** `/ecc:ito-compute`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ito-compute\SKILL.md`

##### `laravel-security`

- **Purpose:** Laravel security best practices — authentication, authorization, Eloquent safety, CSRF, XSS prevention, API security, and secure deployment configurations.
- **When to use:** - Setting up Laravel authentication and authorization (Sanctum, Passport, Jetstream, Breeze) - Implementing user roles, permissions, and policies - Configuring production security settings and environment variables - Reviewing Laravel applications for security ...
- **Workflow sections:** When to Activate / Production Configuration / Authentication / Authorization / Eloquent Security / CSRF Protection / XSS Prevention / Input Validation
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:laravel-security`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\laravel-security\SKILL.md`

##### `perl-security`

- **Purpose:** Comprehensive Perl security covering taint mode, input validation, safe process execution, DBI parameterized queries, web security (XSS/SQLi/CSRF), and perlcritic security policies.
- **When to use:** - Handling user input in Perl applications - Building Perl web applications (CGI, Mojolicious, Dancer2, Catalyst) - Reviewing Perl code for security vulnerabilities - Performing file operations with user-supplied paths - Executing system commands from Perl - W ...
- **Workflow sections:** When to Activate / How It Works / Taint Mode / Input Validation / Safe Regular Expressions / Safe File Operations / Safe Process Execution / SQL Injection Prevention
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:perl-security`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\perl-security\SKILL.md`

##### `production-audit`

- **Purpose:** Local-evidence production readiness audit for shipped apps, pre-launch reviews, post-merge checks, and "what breaks in prod?" questions without sending repo data to an external audit service.
- **Workflow sections:** When to Use / When Not to Use / How It Works / Evidence Checklist / Risk Lenses / Scoring / Output Format / Example
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:production-audit`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\production-audit\SKILL.md`

##### `quality-nonconformance`

- **Purpose:** > | Codified expertise for quality control, non-conformance investigation, root | cause analysis, corrective action, and supplier quality management in | regulated manufacturing. Informed by quality engineers with 15+ years | experience across FDA, IATF 16949, and AS9100 environments. Includes NCR | lifecycle management, CAPA systems, SPC interpretation, and audit methodology. | Use when investiga ...
- **When to use:** Use when investigating non-conformances, performing root cause analysis, | managing CAPAs, interpreting SPC data, or handling supplier quality issues.
- **Workflow sections:** Role and Context / When to Use / How It Works / Examples / Core Knowledge / Decision Frameworks / Key Edge Cases / Communication Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:quality-nonconformance`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\quality-nonconformance\SKILL.md`

##### `quarkus-security`

- **Purpose:** Quarkus Security best practices for authentication, authorization, JWT/OIDC, RBAC, input validation, CSRF, secrets management, and dependency security.
- **Workflow sections:** When to Activate / Authentication / Authorization / Input Validation / SQL Injection Prevention / Password Hashing / CORS Configuration / Secrets Management
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:quarkus-security`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\quarkus-security\SKILL.md`

##### `repo-scan`

- **Purpose:** Cross-stack source code asset audit — classifies every file, detects embedded third-party libraries, and delivers actionable four-level verdicts per module with interactive HTML reports.
- **When to use:** - Taking over a large legacy codebase and need a structural overview - Before major refactoring — identify what's core, what's duplicate, what's dead - Auditing third-party dependencies embedded directly in source (not declared in package managers) - Preparing ...
- **Workflow sections:** When to Use / Installation / Core Capabilities / Analysis Depth Levels / How It Works / Examples / Best Practices / Links
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:repo-scan`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\repo-scan\SKILL.md`

##### `returns-reverse-logistics`

- **Purpose:** > | Codified expertise for returns authorization, receipt and inspection, | disposition decisions, refund processing, fraud detection, and warranty | claims management. Informed by returns operations managers with 15+ years | experience. Includes grading frameworks, disposition economics, fraud | pattern recognition, and vendor recovery processes. Use when handling | product returns, reverse logis ...
- **When to use:** Use when handling | product returns, reverse logistics, refund decisions, return fraud | detection, or warranty claims.
- **Workflow sections:** Role and Context / When to Use / How It Works / Examples / Core Knowledge / Decision Frameworks / Key Edge Cases / Communication Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:returns-reverse-logistics`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\returns-reverse-logistics\SKILL.md`

##### `security-bounty-hunter`

- **Purpose:** Hunt for exploitable, bounty-worthy security issues in repositories. Focuses on remotely reachable vulnerabilities that qualify for real reports instead of noisy local-only findings.
- **When to use:** - Scanning a repository for exploitable vulnerabilities - Preparing a Huntr, HackerOne, or similar bounty submission - Triage where the question is "does this actually pay?" rather than "is this theoretically unsafe?"
- **Workflow sections:** When to Use / How It Works / In-Scope Patterns / Skip These / Workflow / Example Triage Loop / Report Structure / Description
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:security-bounty-hunter`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\security-bounty-hunter\SKILL.md`

##### `security-review`

- **Purpose:** Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints, or implementing payment/sensitive features. Provides comprehensive security checklist and patterns.
- **When to use:** Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints, or implementing payment/sensitive features.
- **Workflow sections:** When to Activate / Security Checklist / Security Testing / Pre-Deployment Security Checklist / Resources
- **Dependencies / tools:** files: `.orphaned_at`, `cloud-infrastructure-security.md`
- **Invocation:** `/ecc:security-review`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\security-review\SKILL.md`

##### `security-scan`

- **Purpose:** Scan your Claude Code configuration (.claude/ directory) for security vulnerabilities, misconfigurations, and injection risks using AgentShield. Checks CLAUDE.md, settings.json, MCP servers, hooks, and agent definitions.
- **When to use:** - Setting up a new Claude Code project - After modifying `.claude/settings.json`, `CLAUDE.md`, or MCP configs - Before committing configuration changes - When onboarding to a new repository with existing Claude Code configs - Periodic security hygiene checks
- **Workflow sections:** When to Activate / What It Scans / Prerequisites / Usage / Severity Levels / Interpreting Results / Links
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:security-scan`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\security-scan\SKILL.md`

##### `seo`

- **Purpose:** Audit, plan, and implement SEO improvements across technical SEO, on-page optimization, structured data, Core Web Vitals, and content strategy. Use when the user wants better search visibility, SEO remediation, schema markup, sitemap/robots work, or keyword mapping.
- **When to use:** Use when the user wants better search visibility, SEO remediation, schema markup, sitemap/robots work, or keyword mapping.
- **Workflow sections:** When to Use / How It Works / Examples / Anti-Patterns / Related Skills
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:seo`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\seo\SKILL.md`

##### `springboot-security`

- **Purpose:** Spring Security best practices for authn/authz, validation, CSRF, secrets, headers, rate limiting, and dependency security in Java Spring Boot services.
- **When to use:** - Adding authentication (JWT, OAuth2, session-based) - Implementing authorization (@PreAuthorize, role-based access) - Validating user input (Bean Validation, custom validators) - Configuring CORS, CSRF, or security headers - Managing secrets (Vault, environme ...
- **Workflow sections:** When to Activate / Authentication / Authorization / Input Validation / SQL Injection Prevention / Password Encoding / CSRF Protection / Secrets Management
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:springboot-security`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\springboot-security\SKILL.md`

##### `workspace-surface-audit`

- **Purpose:** Audit the active repo, MCP servers, plugins, connectors, env surfaces, and harness setup, then recommend the highest-value ECC-native skills, hooks, agents, and operator workflows. Use when the user wants help setting up Claude Code or understanding what capabilities are actually available in their environment.
- **When to use:** Use when the user wants help setting up Claude Code or understanding what capabilities are actually available in their environment.
- **Workflow sections:** When to Use / Non-Negotiable Rules / Audit Inputs / Audit Process / Output Format / Recommendation Rules / Good Outcomes
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:workspace-surface-audit`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\workspace-surface-audit\SKILL.md`

#### Workflow, context & memory (19)

##### `architecture-decision-records`

- **Purpose:** Capture architectural decisions made during Claude Code sessions as structured ADRs. Auto-detects decision moments, records context, alternatives considered, and rationale. Maintains an ADR log so future developers understand why the codebase is shaped the way it is.
- **When to use:** - User explicitly says "let's record this decision" or "ADR this" - User chooses between significant alternatives (framework, library, pattern, database, API design) - User says "we decided to..." or "the reason we're doing X instead of Y is..." - User asks "w ...
- **Workflow sections:** When to Activate / ADR Format / Context / Decision / Alternatives Considered / Consequences / Workflow / Decision Detection Signals
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:architecture-decision-records`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\architecture-decision-records\SKILL.md`

##### `blueprint`

- **Purpose:** >- | Turn a one-line objective into a step-by-step construction plan for | multi-session, multi-agent engineering projects. Each step has a | self-contained context brief so a fresh agent can execute it cold. | Includes adversarial review gate, dependency graph, parallel step | detection, anti-pattern catalog, and plan mutation protocol. | TRIGGER when: user requests a plan, blueprint, or roadmap ...
- **When to use:** TRIGGER when: user requests a plan, blueprint, or roadmap for a | complex multi-PR task, or describes work that needs multiple sessions.
- **Workflow sections:** When to Use / How It Works / Examples / Key Features / Installation / Requirements / Source
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:blueprint`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\blueprint\SKILL.md`

##### `context-budget`

- **Purpose:** Audits Claude Code context window consumption across agents, skills, MCP servers, and rules. Identifies bloat, redundant components, and produces prioritized token-savings recommendations.
- **When to use:** - Session performance feels sluggish or output quality is degrading - You've recently added many skills, agents, or MCP servers - You want to know how much context headroom you actually have - Planning to add more components and need to know if there's room - ...
- **Workflow sections:** When to Use / How It Works / Examples / Best Practices
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:context-budget`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\context-budget\SKILL.md`

##### `continuous-learning`

- **Purpose:** [DEPRECATED - use continuous-learning-v2] Legacy v1 stop-hook skill extractor. v2 is a strict superset with instinct-based, project-scoped, hook-reliable learning. Do not invoke v1; route continuous learning, session learning, and pattern extraction requests to continuous-learning-v2.
- **When to use:** - Setting up automatic pattern extraction from Claude Code sessions - Configuring the Stop hook for session evaluation - Reviewing or curating learned skills in `~/.claude/skills/learned/` - Adjusting extraction thresholds or pattern categories - Comparing v1 ...
- **Workflow sections:** Original v1 Documentation (archival) / When to Activate / Status / How It Works / Configuration / Pattern Types / Hook Setup / Why Stop Hook?
- **Dependencies / tools:** files: `.orphaned_at`, `config.json`, `evaluate-session.sh`
- **Invocation:** `/ecc:continuous-learning`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\continuous-learning\SKILL.md`

##### `cost-tracking`

- **Purpose:** Track and report Claude Code token usage, spending, and budgets from the local ECC cost-tracker metrics log. Use when the user asks about costs, spending, usage, tokens, budgets, or cost breakdowns by model, session, or date.
- **When to use:** Use when the user asks about costs, spending, usage, tokens, budgets, or cost breakdowns by model, session, or date.
- **Workflow sections:** Where the data lives / When to Use / How It Works / Example — summary, by model, last 7 days / Reporting Guidance / Anti-Patterns / Related
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:cost-tracking`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\cost-tracking\SKILL.md`

##### `evm-token-decimals`

- **Purpose:** Prevent silent decimal mismatch bugs across EVM chains. Covers runtime decimal lookup, chain-aware caching, bridged-token precision drift, and safe normalization for bots, dashboards, and DeFi tools.
- **When to use:** - Reading ERC-20 balances in Python, TypeScript, or Solidity - Calculating fiat values from on-chain balances - Comparing token amounts across multiple EVM chains - Handling bridged assets - Building portfolio trackers, bots, or aggregators
- **Workflow sections:** When to Use / How It Works / Examples / Rules
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:evm-token-decimals`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\evm-token-decimals\SKILL.md`

##### `exa-search`

- **Purpose:** Neural search via Exa MCP for web, code, and company research. Use when the user needs web search, code examples, company intel, people lookup, or AI-powered deep research with Exa's neural search engine.
- **When to use:** Use when the user needs web search, code examples, company intel, people lookup, or AI-powered deep research with Exa's neural search engine.
- **Workflow sections:** When to Activate / MCP Requirement / Core Tools / Usage Patterns / Tips / Related Skills
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:exa-search`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\exa-search\SKILL.md`

##### `git-workflow`

- **Purpose:** Git workflow patterns including branching strategies, commit conventions, merge vs rebase, conflict resolution, and collaborative development best practices for teams of all sizes.
- **When to use:** - Setting up Git workflow for a new project - Deciding on branching strategy (GitFlow, trunk-based, GitHub flow) - Writing commit messages and PR descriptions - Resolving merge conflicts - Managing releases and version tags - Onboarding new team members to Git ...
- **Workflow sections:** When to Activate / Branching Strategies / Commit Messages / Merge vs Rebase / Pull Request Workflow / What / Why / How
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:git-workflow`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\git-workflow\SKILL.md`

##### `inventory-demand-planning`

- **Purpose:** > | Codified expertise for demand forecasting, safety stock optimization, | replenishment planning, and promotional lift estimation at multi-location | retailers. Informed by demand planners with 15+ years experience managing | hundreds of SKUs. Includes forecasting method selection, ABC/XYZ analysis, | seasonal transition management, and vendor negotiation frameworks. | Use when forecasting deman ...
- **When to use:** Use when forecasting demand, setting safety stock, planning replenishment, | managing promotions, or optimizing inventory levels.
- **Workflow sections:** Role and Context / When to Use / How It Works / Examples / Core Knowledge / Decision Frameworks / Key Edge Cases / Communication Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:inventory-demand-planning`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\inventory-demand-planning\SKILL.md`

##### `ito-trade-planner`

- **Purpose:** Build a non-advisory prediction-market trade planning worksheet for Itô or venue workflows. Use to inspect venues, underliers, constraints, order prerequisites, and manual execution steps without placing trades or recommending positions.
- **Workflow sections:** Guardrails / Read-Only API And Authentication Boundary / Planning Workflow / Recovery And Failure States / Allowed Language / Structured Output Contract
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:ito-trade-planner`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ito-trade-planner\SKILL.md`

##### `literature-review`

- **Purpose:** Systematic literature-review workflow for academic, biomedical, technical, and scientific topics, including search planning, source screening, synthesis, citation checks, and evidence logging.
- **When to use:** - Building a systematic, scoping, or narrative literature review. - Synthesizing the state of the art for a research question. - Finding gaps, contradictions, or future-work directions. - Preparing citation-backed background sections for papers or reports. - C ...
- **Workflow sections:** When to Use / Review Types / Workflow / Output Template / Research Question / Search Strategy / Inclusion and Exclusion Criteria / Evidence Summary
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:literature-review`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\scientific-thinking-literature-review\SKILL.md`

##### `plan-canvas`

- **Purpose:** Open plans and HTML artifacts in a local browser canvas where the human annotates elements, chats, and approves or requests changes without leaving the page. Use when presenting a plan for review, or when feedback like "move this, change that" is easier pointed at than typed.
- **When to use:** Use when presenting a plan for review, or when feedback like "move this, change that" is easier pointed at than typed.
- **Workflow sections:** When to Use / How It Works / Diagrams (Mermaid) / Rules / Examples / Anti-Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:plan-canvas`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\plan-canvas\SKILL.md`

##### `plankton-code-quality`

- **Purpose:** Write-time code quality enforcement using Plankton — auto-formatting, linting, and Claude-powered fixes on every file edit via hooks.
- **When to use:** - You want automatic formatting and linting on every file edit (not just at commit time) - You need defense against agents modifying linter configs to pass instead of fixing code - You want tiered model routing for fixes (Haiku for simple style, Sonnet for log ...
- **Workflow sections:** When to Use / How It Works / Setup / Pairing with ECC / Configuration Reference / Environment Overrides / References / ECC v1.8 Additions
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:plankton-code-quality`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\plankton-code-quality\SKILL.md`

##### `product-capability`

- **Purpose:** Translate PRD intent, roadmap asks, or product discussions into an implementation-ready capability plan that exposes constraints, invariants, interfaces, and unresolved decisions before multi-service work starts. Use when the user needs an ECC-native PRD-to-SRS lane instead of vague planning prose.
- **When to use:** Use when the user needs an ECC-native PRD-to-SRS lane instead of vague planning prose.
- **Workflow sections:** When to Use / Canonical Artifact / Non-Negotiable Rules / Inputs / Core Workflow / Output Format / Good Outcomes
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:product-capability`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\product-capability\SKILL.md`

##### `search-first`

- **Purpose:** Research-before-coding workflow. Search for existing tools, libraries, and patterns before writing custom code. Invokes the researcher agent.
- **Workflow sections:** Trigger / Workflow / Decision Matrix / How to Use / Search Shortcuts by Category / Integration Points / Examples / Anti-Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:search-first`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\search-first\SKILL.md`

##### `strategic-compact`

- **Purpose:** Suggests manual context compaction at logical intervals to preserve context through task phases rather than arbitrary auto-compaction.
- **When to use:** - Running long sessions that approach context limits (200K+ tokens) - Working on multi-phase tasks (research → plan → implement → test) - Switching between unrelated tasks within the same session - After completing a major milestone and starting new work - Whe ...
- **Workflow sections:** When to Activate / Why Strategic Compaction? / How It Works / Hook Setup / Configuration / Compaction Decision Guide / What Survives Compaction / Best Practices
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:strategic-compact`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\strategic-compact\SKILL.md`

##### `terminal-opener`

- **Purpose:** Open an executable and its argument array in a visible terminal window through a reusable, shell-free launch plan with dry-run, JSON, capability detection, detached fallback, and standalone recovery modes. Use when Codex needs to open an interactive CLI, SSH session, local development process, sandbox, or other argv-based command in a new host terminal; diagnose whether a supported terminal is ava ...
- **When to use:** Use when Codex needs to open an interactive CLI, SSH session, local development process, sandbox, or other argv-based command in a new host terminal; diagnose whether a supported terminal is available; or provide an actionable plan when the requested terminal ...
- **Workflow sections:** Launch a command / Recover from terminal configuration / Inspect before launch
- **Dependencies / tools:** bundled: `scripts/`; files: `.orphaned_at`, `agents/`
- **Invocation:** `/ecc:terminal-opener`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\terminal-opener\SKILL.md`

##### `token-budget-advisor`

- **Purpose:** >- | Offers the user an informed choice about how much response depth to | consume before answering. Use this skill when the user explicitly | wants to control response length, depth, or token budget. | TRIGGER when: "token budget", "token count", "token usage", "token limit", | "response length", "answer depth", "short version", "brief answer", | "detailed answer", "exhaustive answer", "respuesta ...
- **When to use:** Use this skill when the user explicitly | wants to control response length, depth, or token budget.
- **Workflow sections:** When to Use / How It Works / Shortcuts — skip the question / Precision note / Examples / Source
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:token-budget-advisor`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\token-budget-advisor\SKILL.md`

##### `unified-memory`

- **Purpose:** Share durable, inspectable context and handoffs between Claude, Codex, Hermes, Cursor, OpenCode, and other agents through the local ECC Memory Vault. Use when an agent must save work state, transfer context, resume another agent's task, or search shared project knowledge.
- **When to use:** Use when an agent must save work state, transfer context, resume another agent's task, or search shared project knowledge.
- **Workflow sections:** Runtime Prerequisite / When To Use / Vault Scopes / Workflow / Trust And Data Boundaries / MCP Setup
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:unified-memory`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\unified-memory\SKILL.md`

#### Docs, writing & content (10)

##### `article-writing`

- **Purpose:** Write articles, guides, blog posts, tutorials, newsletter issues, and other long-form content in a distinctive voice derived from supplied examples or brand guidance. Use when the user wants polished written content longer than a paragraph, especially when voice consistency, structure, and credibility matter.
- **When to use:** Use when the user wants polished written content longer than a paragraph, especially when voice consistency, structure, and credibility matter.
- **Workflow sections:** When to Activate / Core Rules / Voice Handling / Banned Patterns / Writing Process / Structure Guidance / Quality Gate
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:article-writing`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\article-writing\SKILL.md`

##### `code-tour`

- **Purpose:** Create CodeTour `.tour` files — persona-targeted, step-by-step walkthroughs with real file and line anchors. Use for onboarding tours, architecture walkthroughs, PR tours, RCA tours, and structured "explain how this works" requests.
- **Workflow sections:** When to Use / When NOT to Use / Workflow / The `ref` Field / Step Types / Writing Rule: SMIG / Narrative Shape / Example
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:code-tour`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\code-tour\SKILL.md`

##### `codebase-onboarding`

- **Purpose:** Analyze an unfamiliar codebase and generate a structured onboarding guide with architecture map, key entry points, conventions, and a starter CLAUDE.md. Use when joining a new project or setting up Claude Code for the first time in a repo.
- **When to use:** Use when joining a new project or setting up Claude Code for the first time in a repo.
- **Workflow sections:** When to Use / How It Works / Overview / Tech Stack / Architecture / Key Entry Points / Directory Map / Request Lifecycle
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:codebase-onboarding`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\codebase-onboarding\SKILL.md`

##### `content-engine`

- **Purpose:** Create platform-native content systems for X, LinkedIn, TikTok, YouTube, newsletters, and repurposed multi-platform campaigns. Use when the user wants social posts, threads, scripts, content calendars, or one source asset adapted cleanly across platforms.
- **When to use:** Use when the user wants social posts, threads, scripts, content calendars, or one source asset adapted cleanly across platforms.
- **Workflow sections:** When to Activate / Non-Negotiables / Source-First Workflow / Voice Handling / Hard Bans / Platform Adaptation Rules / Repurposing Flow / Deliverables
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:content-engine`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\content-engine\SKILL.md`

##### `content-hash-cache-pattern`

- **Purpose:** Cache expensive file processing results using SHA-256 content hashes — path-independent, auto-invalidating, with service layer separation.
- **When to use:** - Building file processing pipelines (PDF, images, text extraction) - Processing cost is high and same files are processed repeatedly - Need a `--cache/--no-cache` CLI option - Want to add caching to existing pure functions without modifying them
- **Workflow sections:** When to Activate / Core Pattern / Key Design Decisions / Best Practices / Anti-Patterns to Avoid / When to Use / When NOT to Use
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:content-hash-cache-pattern`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\content-hash-cache-pattern\SKILL.md`

##### `crosspost`

- **Purpose:** Multi-platform content distribution across X, LinkedIn, Threads, and Bluesky. Adapts content per platform using content-engine patterns. Never posts identical content cross-platform. Use when the user wants to distribute content across social platforms.
- **When to use:** Use when the user wants to distribute content across social platforms.
- **Workflow sections:** When to Activate / Core Rules / Workflow / Posting Order / Banned Patterns / Output Format / Quality Gate / Related Skills
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:crosspost`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\crosspost\SKILL.md`

##### `documentation-lookup`

- **Purpose:** Use up-to-date library and framework docs via Context7 MCP instead of training data. Activates for setup questions, API references, code examples, or when the user names a framework (e.g. React, Next.js, Prisma).
- **Workflow sections:** Core Concepts / When to use / How it works / Examples / Best Practices
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:documentation-lookup`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\documentation-lookup\SKILL.md`

##### `ito-basket-compare`

- **Purpose:** Compare Itô prediction-market baskets against a user's knowledge base, portfolio notes, financial context, watchlist, or research thesis. Use for read-only basket comparison and gap analysis without investment advice or live trading.
- **Workflow sections:** Non-negotiable boundaries / Inputs and access / First-run authentication handoff / Deterministic normalization and comparison / Recovery and safe failure / Output contract
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:ito-basket-compare`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ito-basket-compare\SKILL.md`

##### `nutrient-document-processing`

- **Purpose:** Process, convert, OCR, extract, redact, sign, and fill documents using the Nutrient DWS API. Works with PDFs, DOCX, XLSX, PPTX, HTML, and images.
- **When to use:** - Converting documents between formats (PDF, DOCX, XLSX, PPTX, HTML, images) - Extracting text, tables, or key-value pairs from PDFs - OCR on scanned documents or images - Redacting PII before sharing documents - Adding watermarks to drafts or confidential doc ...
- **Workflow sections:** Setup / Operations / MCP Server (Alternative) / When to Use / Links
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:nutrient-document-processing`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\nutrient-document-processing\SKILL.md`

##### `visa-doc-translate`

- **Purpose:** Translate visa application documents (images) to English and create a bilingual PDF with original and translation
- **Workflow sections:** Instructions / Supported Documents / Technical Implementation / Important Guidelines / Example Usage / Output Example
- **Dependencies / tools:** files: `.orphaned_at`, `README.md`
- **Invocation:** `/ecc:visa-doc-translate`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\visa-doc-translate\SKILL.md`

#### Research & analysis (10)

##### `competitive-platform-analysis`

- **Purpose:** >- | Use when scoping a competitive landscape — identifying, categorising, and | score-filtering a competitor set before any benchmarking begins. Decides who | counts as a competitor, which tier they belong to, and which sources to mine. | First step in the three-skill competitive pipeline; precedes | benchmark-methodology.
- **When to use:** Use when scoping a competitive landscape — identifying, categorising, and | score-filtering a competitor set before any benchmarking begins.
- **Workflow sections:** When to Activate / Client positioning brief (establish first) / Selection criteria / Player taxonomy — axes to populate across / Competitive tiers (how the set resolves) / Data sources (where to look) / Scoring matrix template (selection stage) / Output of this stage
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:competitive-platform-analysis`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\competitive-platform-analysis\SKILL.md`

##### `competitive-report-structure`

- **Purpose:** >- | Use after benchmark-methodology has produced scored competitor profile cards. | Assembles findings into a decision-grade report: landscape map, competitor | profiles, benchmarking matrix, white-space analysis, strategic recommendations, | and team alignment trigger questions. Final step in the three-skill competitive | pipeline.
- **When to use:** - All competitor profile cards from benchmark-methodology are complete and ready to assemble. - Need to present competitive findings to a founder, leadership team, or board. - The report must drive decisions (who to compete with, how, where the moat is) — not ...
- **Workflow sections:** When to Activate / Client positioning brief (establish first) / Framing principle / Report sections / How to present data / Decision framework (the report must resolve these) / Trigger questions for the team alignment session / Anti-Patterns
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:competitive-report-structure`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\competitive-report-structure\SKILL.md`

##### `deep-research`

- **Purpose:** Multi-source deep research using firecrawl and exa MCPs. Searches the web, synthesizes findings, and delivers cited reports with source attribution. Use when the user wants thorough research on any topic with evidence and citations.
- **When to use:** Use when the user wants thorough research on any topic with evidence and citations.
- **Workflow sections:** When to Activate / MCP Requirements / Workflow / Executive Summary / 1. [First Major Theme] / 2. [Second Major Theme] / 3. [Third Major Theme] / Key Takeaways
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:deep-research`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\deep-research\SKILL.md`

##### `investor-materials`

- **Purpose:** Create and update pitch decks, one-pagers, investor memos, accelerator applications, financial models, and fundraising materials. Use when the user needs investor-facing documents, projections, use-of-funds tables, milestone plans, or materials that must stay internally consistent across multiple fundraising assets.
- **When to use:** Use when the user needs investor-facing documents, projections, use-of-funds tables, milestone plans, or materials that must stay internally consistent across multiple fundraising assets.
- **Workflow sections:** When to Activate / Golden Rule / Core Workflow / Asset Guidance / Red Flags to Avoid / Quality Gate
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:investor-materials`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\investor-materials\SKILL.md`

##### `investor-outreach`

- **Purpose:** Draft cold emails, warm intro blurbs, follow-ups, update emails, and investor communications for fundraising. Use when the user wants outreach to angels, VCs, strategic investors, or accelerators and needs concise, personalized, investor-facing messaging.
- **When to use:** Use when the user wants outreach to angels, VCs, strategic investors, or accelerators and needs concise, personalized, investor-facing messaging.
- **Workflow sections:** When to Activate / Core Rules / Voice Handling / Hard Bans / Cold Email Structure / Personalization Sources / Follow-Up Cadence / Warm Intro Requests
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:investor-outreach`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\investor-outreach\SKILL.md`

##### `ito-market-intelligence`

- **Purpose:** Research prediction-market events, venues, underliers, liquidity, and news context for Itô basket workflows. Use for read-only market intelligence, API-gated Itô exploration, and source-grounded prediction-market briefings without investment advice or live trading.
- **Workflow sections:** Guardrails / Workflow / Authentication and recovery / Useful Skill Chains / Output Contract
- **Dependencies / tools:** bundled: `scripts/`; files: `.orphaned_at`, `agents/`
- **Invocation:** `/ecc:ito-market-intelligence`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ito-market-intelligence\SKILL.md`

##### `market-research`

- **Purpose:** Conduct market research, competitive analysis, investor due diligence, and industry intelligence with source attribution and decision-oriented summaries. Use when the user wants market sizing, competitor comparisons, fund research, technology scans, or research that informs business decisions.
- **When to use:** Use when the user wants market sizing, competitor comparisons, fund research, technology scans, or research that informs business decisions.
- **Workflow sections:** When to Activate / Research Standards / Common Research Modes / Output Format / Quality Gate
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:market-research`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\market-research\SKILL.md`

##### `marketing-campaign`

- **Purpose:** End-to-end marketing campaign planning and execution. Covers audience research, positioning, campaign angle definition, landing page copy, email sequences, social posts, ad copy, short-form video scripts, and content calendars. Use as the orchestration layer for multi-channel product launches.
- **When to use:** - planning a product or feature launch - building a full content suite from a single product brief - defining positioning and campaign angle before writing any copy - orchestrating multiple content types across channels - reviewing copy for conversion quality ...
- **Workflow sections:** When to Activate / Non-Negotiables / Campaign Workflow / Output Contract / Quality Gate / Hard Bans / Related Skills
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:marketing-campaign`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\marketing-campaign\SKILL.md`

##### `prediction-market-oracle-research`

- **Purpose:** Research prediction markets as data sources or oracle signals for products, agents, dashboards, and corporate decision intelligence. Use for source-grounded analysis of market-implied probabilities, caveats, and integration patterns without investment advice.
- **Workflow sections:** Guardrails / Research Workflow / Integration Patterns / Output Contract
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:prediction-market-oracle-research`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\prediction-market-oracle-research\SKILL.md`

##### `prediction-market-risk-review`

- **Purpose:** Review prediction-market, basket, oracle, and trading-agent workflows for compliance, safety, data-quality, privacy, and execution risk. Use before any workflow handles venue auth, user portfolio data, API keys, or trade planning.
- **Workflow sections:** Review Gates / Output Contract
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:prediction-market-risk-review`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\prediction-market-risk-review\SKILL.md`

#### Platform & integrations (6)

##### `codehealth-mcp`

- **Purpose:** Real-time structural Code Health via CodeScene MCP — review before edits, verify score deltas after changes, gate commits and PRs. Use when reviewing code quality, refactoring, checking if AI changes degraded a file, or before commit/PR.
- **When to use:** Use when reviewing code quality, refactoring, checking if AI changes degraded a file, or before commit/PR.
- **Workflow sections:** Security and boundaries / When to Use / When to Activate / How It Works / Examples / Code Health (CodeScene MCP) / Pairing with ECC / Related Skills
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:codehealth-mcp`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\codehealth-mcp\SKILL.md`

##### `contract-first`

- **Purpose:** Use when multiple consumers and providers must evolve an API or event schema without field drift, integration surprises, or one side silently redefining the interface.
- **When to use:** Use when multiple consumers and providers must evolve an API or event schema without field drift, integration surprises, or one side silently redefining the interface.
- **Workflow sections:** When to Activate / The Boundary Artifact / Consumer-First Workflow / Contract Change Protocol / Anti-Patterns / Best Practices / Completion Checklist / Related Skills
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:contract-first`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\contract-first\SKILL.md`

##### `hexagonal-architecture`

- **Purpose:** Design, implement, and refactor Ports & Adapters systems with clear domain boundaries, dependency inversion, and testable use-case orchestration across TypeScript, Java, Kotlin, and Go services.
- **Workflow sections:** When to Use / Core Concepts / How It Works / Architecture Diagram / Suggested Module Layout / TypeScript Example / Multi-Language Mapping / Anti-Patterns to Avoid
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:hexagonal-architecture`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\hexagonal-architecture\SKILL.md`

##### `jira-integration`

- **Purpose:** Use this skill when retrieving Jira tickets, analyzing requirements, updating ticket status, adding comments, or transitioning issues. Provides Jira API patterns via MCP or direct REST calls.
- **When to use:** Use this skill when retrieving Jira tickets, analyzing requirements, updating ticket status, adding comments, or transitioning issues.
- **Workflow sections:** When to Activate / Prerequisites / MCP Tools Reference / Direct REST API Reference / Analyzing a Ticket / Updating Tickets / Security Guidelines / Troubleshooting
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:jira-integration`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\jira-integration\SKILL.md`

##### `mailtrap-email-integration`

- **Purpose:** Guides agents through integrating transactional email sending via Mailtrap's Email API, including sandbox testing, domain verification, and API authentication. Use when implementing email-sending features, debugging delivery issues, or setting up safe dev/staging email testing.
- **When to use:** Use when implementing email-sending features, debugging delivery issues, or setting up safe dev/staging email testing.
- **Workflow sections:** When to Activate / Core Concepts / Code Examples / Anti-Patterns / Best Practices / Related Skills
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:mailtrap-email-integration`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\mailtrap-email-integration\SKILL.md`

##### `x-api`

- **Purpose:** X/Twitter API integration for posting tweets, threads, reading timelines, search, and analytics. Covers OAuth auth patterns, rate limits, and platform-native content posting. Use when the user wants to interact with X programmatically.
- **When to use:** Use when the user wants to interact with X programmatically.
- **Workflow sections:** When to Activate / Authentication / Core Operations / Rate Limits / Error Handling / Security / Integration with Content Engine / Related Skills
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/ecc:x-api`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\x-api\SKILL.md`

#### Data & databases (5)

##### `clickhouse-io`

- **Purpose:** ClickHouse database patterns, query optimization, analytics, and data engineering best practices for high-performance analytical workloads.
- **Workflow sections:** When to Activate / Overview / Table Design Patterns / Query Optimization Patterns / Data Insertion Patterns / Materialized Views / Performance Monitoring / Common Analytics Queries
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:clickhouse-io`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\clickhouse-io\SKILL.md`

##### `data-throughput-accelerator`

- **Purpose:** Use when large data ingestion, backfill, export, ETL, warehouse loading, manifest catch-up, or table synchronization needs to become much faster while preserving data correctness.
- **When to use:** Use when large data ingestion, backfill, export, ETL, warehouse loading, manifest catch-up, or table synchronization needs to become much faster while preserving data correctness.
- **Workflow sections:** First Distinction / Fast Path Heuristics / Workflow / Accounting Output / Guardrails
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:data-throughput-accelerator`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\data-throughput-accelerator\SKILL.md`

##### `database-migrations`

- **Purpose:** Database migration best practices for schema changes, data migrations, rollbacks, and zero-downtime deployments across PostgreSQL, MySQL, and common ORMs (Prisma, Drizzle, Kysely, Django, TypeORM, golang-migrate).
- **When to use:** - Creating or altering database tables - Adding/removing columns or indexes - Running data migrations (backfill, transform) - Planning zero-downtime schema changes - Setting up migration tooling for a new project
- **Workflow sections:** When to Activate / Core Principles / Migration Safety Checklist / PostgreSQL Patterns / Prisma (TypeScript/Node.js) / Drizzle (TypeScript/Node.js) / Kysely (TypeScript/Node.js) / Django (Python)
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:database-migrations`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\database-migrations\SKILL.md`

##### `pubmed-database`

- **Purpose:** Direct PubMed and NCBI E-utilities search workflows for biomedical literature, MeSH queries, PMID lookup, citation retrieval, and API-backed literature monitoring.
- **When to use:** - Searching MEDLINE or life-sciences literature. - Building PubMed queries with MeSH terms, field tags, dates, or article types. - Looking up PMIDs, abstracts, publication metadata, or related citations. - Running systematic-review search passes that need repe ...
- **Workflow sections:** When to Use / Query Construction / MeSH and Subheadings / Filters / E-utilities Workflow / Output Discipline / Review Checklist / References
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:pubmed-database`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\scientific-db-pubmed-database\SKILL.md`

##### `uspto-database`

- **Purpose:** USPTO patent and trademark data workflow for official record lookup, PatentSearch queries, TSDR checks, assignment data, and reproducible IP research logs.
- **Workflow sections:** When to Use / Source Selection / Authentication and Secrets / PatentSearch Workflow / Trademark/TSDR Workflow / File Wrapper and Prosecution History / Assignment Workflow / Reproducible Output
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:uspto-database`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\scientific-db-uspto-database\SKILL.md`

#### Other / general engineering (2)

##### `regex-vs-llm-structured-text`

- **Purpose:** Decision framework for choosing between regex and LLM when parsing structured text — start with regex, add LLM only for low-confidence edge cases.
- **When to use:** - Parsing structured text with repeating patterns (questions, forms, tables) - Deciding between regex and LLM for text extraction - Building hybrid pipelines that combine both approaches - Optimizing cost/accuracy tradeoffs in text processing
- **Workflow sections:** When to Activate / Decision Framework / Architecture Pattern / Implementation / Real-World Metrics / Best Practices / Anti-Patterns to Avoid / When to Use
- **Dependencies / tools:** files: `.orphaned_at`
- **Invocation:** `/ecc:regex-vs-llm-structured-text`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\regex-vs-llm-structured-text\SKILL.md`

##### `rules-distill`

- **Purpose:** Scan skills to extract cross-cutting principles and distill them into rules — append, revise, or create new rule files
- **When to use:** - Periodic rules maintenance (monthly or after installing new skills) - After a skill-stocktake reveals patterns that should be rules - When rules feel incomplete relative to the skills being used
- **Workflow sections:** When to Use / How It Works / Input / Extraction Criteria / Matching & Verdict / Output Format (per candidate) / Exclude / Summary
- **Dependencies / tools:** bundled: `scripts/`; files: `.orphaned_at`
- **Invocation:** `/ecc:rules-distill`
- **Source:** `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\rules-distill\SKILL.md`

---

### Synced plugin `financial-analysis`

*13 skills.*

#### `3-statement-model`

- **Purpose:** Complete, populate and fill out 3-statement financial model templates (Income Statement, Balance Sheet, Cash Flow Statement) . Use when asked to fill out model templates, complete existing model frameworks, populate financial models with data, complete a partially filled IS/BS/CF framework, or link integrated financial statements within an existing template structure. Triggers include requests to fill in, complete, or populate a 3-statement model template
- **When to use:** Use when asked to fill out model templates, complete existing model frameworks, populate financial models with data, complete a partially filled IS/BS/CF framework, or link integrated financial statements within an existing template structure.
- **Workflow sections:** ⚠️ CRITICAL PRINCIPLES — Read Before Populating Any Template / Formatting — Professional Blue/Grey Palette (Default unless template/user specifies otherwise) / Model Structure / Margin Analysis / Credit Metrics / Scenario Analysis (Base / Upside / Downside) / SEC Filings Data Extraction / Completing Model Templates
- **Dependencies / tools:** bundled: `references/`
- **Invocation:** `/financial-analysis:3-statement-model`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\3-statement-model\SKILL.md`

#### `audit-xls`

- **Purpose:** Audit a spreadsheet for formula accuracy, errors, and common mistakes. Scopes to a selected range, a single sheet, or the entire model (including financial-model integrity checks like BS balance, cash tie-out, and logic sanity). Triggers on "audit this sheet", "check my formulas", "find formula errors", "QA this spreadsheet", "sanity check this", "debug model", "model check", "model won't balance", "something's off in my model", "model review".
- **Workflow sections:** Step 1: Determine scope / Step 2: Formula-level checks (ALL scopes) / Step 3: Model-integrity checks (MODEL scope only) / Step 4: Report / Notes
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/financial-analysis:audit-xls`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\audit-xls\SKILL.md`

#### `clean-data-xls`

- **Purpose:** Clean up messy spreadsheet data — trim whitespace, fix inconsistent casing, convert numbers-stored-as-text, standardize dates, remove duplicates, and flag mixed-type columns. Use when data is messy, inconsistent, or needs prep before analysis. Triggers on "clean this data", "clean up this sheet", "normalize this data", "fix formatting", "dedupe", "standardize this column", "this data is messy".
- **When to use:** Use when data is messy, inconsistent, or needs prep before analysis.
- **Workflow sections:** Environment / Workflow
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/financial-analysis:clean-data-xls`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\clean-data-xls\SKILL.md`

#### `competitive-analysis`

- **Purpose:** Framework for building competitive landscape decks — market positioning, competitor deep-dives, comparative analysis, strategic synthesis. Use when the user asks for a competitive landscape, competitor analysis, peer comparison, market positioning assessment, strategic review, or investment memo deck. Also triggers on "who are the competitors to X", "benchmark X against peers", "build a market map", or any request to systematically evaluate competitive dynamics across an industry.
- **When to use:** Use when the user asks for a competitive landscape, competitor analysis, peer comparison, market positioning assessment, strategic review, or investment memo deck.
- **Workflow sections:** Environment check / Phase 1 — Scope the analysis / Phase 2 — Outline, approve, then build / Standards — apply throughout / Analysis workflow / Quality checklist
- **Dependencies / tools:** bundled: `references/`
- **Invocation:** `/financial-analysis:competitive-analysis`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\competitive-analysis\SKILL.md`

#### `comps-analysis`

- **Purpose:** | | Build institutional-grade comparable company analyses with operating metrics, valuation multiples, and statistical benchmarking in Excel/spreadsheet format. | **Perfect for:** | - Public company valuation (M&A, investment analysis) | - Benchmarking performance vs. industry peers | - Pricing IPOs or funding rounds | - Identifying valuation outliers (over/under-valued) | - Supporting investment committee presentations | - Creating sector overview reports | **Not ideal for:** | - Private compan ...
- **Workflow sections:** ⚠️ CRITICAL: Data Source Priority (READ FIRST) / Overview / Core Philosophy / ⚠️ CRITICAL: Formulas Over Hardcodes + Step-by-Step Verification / Section 1: Document Structure & Setup / Section 2: Operating Statistics & Financial Metrics / Section 3: Valuation Multiples & Investment Metrics / Section 4: Notes & Methodology Documentation
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/financial-analysis:comps-analysis`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\comps-analysis\SKILL.md`

#### `dcf-model`

- **Purpose:** Real DCF (Discounted Cash Flow) model creation for equity valuation. Retrieves financial data from SEC filings and analyst reports, builds comprehensive cash flow projections with proper WACC calculations, performs sensitivity analysis, and outputs professional Excel models with executive summaries. Use when users need to value a company using DCF methodology, request intrinsic value analysis, or ask for detailed financial modeling with growth projections and terminal value calculations.
- **When to use:** Use when users need to value a company using DCF methodology, request intrinsic value analysis, or ask for detailed financial modeling with growth projections and terminal value calculations.
- **Workflow sections:** Overview / Tools / Critical Constraints - Read These First / DCF Process Workflow / Excel File Creation / Quality Rubric / Input Requirements / Excel Model Structure
- **Dependencies / tools:** bundled: `scripts/`; files: `TROUBLESHOOTING.md`, `requirements.txt`
- **Invocation:** `/financial-analysis:dcf-model`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\dcf-model\SKILL.md`

#### `deck-refresh`

- **Purpose:** Updates a presentation with new numbers — quarterly refreshes, earnings updates, comp rolls, rebased market data. Use whenever the user asks to "update the deck with Q4 numbers", "refresh the comps", "roll this forward", "swap in the new earnings", "change all the $485M to $512M", or any request to swap figures across an existing deck without rebuilding it.
- **When to use:** Use whenever the user asks to "update the deck with Q4 numbers", "refresh the comps", "roll this forward", "swap in the new earnings", "change all the $485M to $512M", or any request to swap figures across an existing deck without rebuilding it.
- **Workflow sections:** Environment check / Phase 1 — Get the data / Phase 2 — Read everything, find everything / Phase 3 — Present the plan, get approval / Phase 4 — Execute, preserve, report / What you're not doing
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/financial-analysis:deck-refresh`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\deck-refresh\SKILL.md`

#### `ib-check-deck`

- **Purpose:** Investment banking presentation quality checker. Reviews a pitch deck or client-ready presentation for (1) number consistency across slides, (2) data-narrative alignment, (3) language polish against IB standards, (4) visual and formatting QC. Use whenever the user asks to review, check, QC, proof, or do a final pass on a deck, pitch, or client materials — including requests like "check my numbers", "reconcile figures across slides", "is this client-ready", or "what am I missing before I send thi ...
- **When to use:** Use whenever the user asks to review, check, QC, proof, or do a final pass on a deck, pitch, or client materials — including requests like "check my numbers", "reconcile figures across slides", "is this client-ready", or "what am I missing before I send this out".
- **Workflow sections:** Environment check / Workflow / Slide 1 / Slide 2 / Output
- **Dependencies / tools:** bundled: `references/`, `scripts/`
- **Invocation:** `/financial-analysis:ib-check-deck`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\ib-check-deck\SKILL.md`

#### `lbo-model`

- **Purpose:** This skill should be used when completing LBO (Leveraged Buyout) model templates in Excel for private equity transactions, deal materials, or investment committee presentations. The skill fills in formulas, validates calculations, and ensures professional formatting standards that adapt to any template structure.
- **Workflow sections:** TEMPLATE REQUIREMENT / CRITICAL INSTRUCTIONS FOR CLAUDE - READ FIRST / TEMPLATE ANALYSIS PHASE - DO THIS FIRST / FILLING FORMULAS - GENERAL APPROACH / COMMON PROBLEM AREAS / VERIFICATION CHECKLIST - RUN AFTER COMPLETION / COMMON ERRORS TO AVOID / WORKING WITH THE USER — SECTION-BY-SECTION CHECKPOINTS
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/financial-analysis:lbo-model`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\lbo-model\SKILL.md`

#### `ppt-template-creator`

- **Purpose:** Creates self-contained PPT template SKILLS (not presentations) from user-provided PowerPoint templates. Use ONLY when a user wants to create a reusable skill from their template. For creating actual presentations, use the pptx skill instead.
- **Workflow sections:** Workflow / Step 2: Analyze Template / Step 5: Write SKILL.md / Creating Presentations / Key Layouts / Placeholder Mapping / Filling Content / Example: Cover Slide
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/financial-analysis:ppt-template-creator`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\ppt-template-creator\SKILL.md`

#### `pptx-author`

- **Purpose:** Produce a .pptx file on disk (headless) instead of driving a live PowerPoint document — for managed-agent sessions with no open Office app.
- **Workflow sections:** Output contract / How to build the deck / Conventions (mirror the live-Office `pitch-deck` skill) / When NOT to use
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/financial-analysis:pptx-author`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\pptx-author\SKILL.md`

#### `skill-creator`

- **Purpose:** Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
- **Workflow sections:** About Skills / Core Principles / Quick start / Advanced features / Creating documents / Editing documents / Skill Creation Process
- **Dependencies / tools:** bundled: `references/`, `scripts/`; files: `LICENSE.txt`
- **Invocation:** `/financial-analysis:skill-creator`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\skill-creator\SKILL.md`

#### `xlsx-author`

- **Purpose:** Produce a .xlsx file on disk (headless) instead of driving a live Excel workbook — for managed-agent sessions with no open Office app.
- **Workflow sections:** Output contract / How to build the workbook / Conventions (mirror `audit-xls`) / When NOT to use
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/financial-analysis:xlsx-author`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\xlsx-author\SKILL.md`

---

### Synced plugin `investment-banking`

*9 skills.*

#### `buyer-list`

- **Purpose:** Build and organize a universe of potential acquirers for sell-side M&A processes. Identifies strategic and financial buyers, assesses fit, and prioritizes outreach. Use when preparing for a sell-side mandate, building a buyer universe, or evaluating potential partners. Triggers on "buyer list", "buyer universe", "potential acquirers", "who would buy this", "strategic buyers", or "financial sponsors".
- **When to use:** Use when preparing for a sell-side mandate, building a buyer universe, or evaluating potential partners.
- **Workflow sections:** Workflow / Important Notes
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/investment-banking:buyer-list`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\skills\buyer-list\SKILL.md`

#### `cim-builder`

- **Purpose:** Structure and draft a Confidential Information Memorandum for sell-side M&A processes. Organizes company information into a professional, investor-ready document with consistent formatting and narrative flow. Use when preparing sell-side materials, drafting a CIM, or organizing company data for a sale process. Triggers on "CIM", "confidential information memorandum", "offering memorandum", "info memo", "draft CIM", or "sell-side materials".
- **When to use:** Use when preparing sell-side materials, drafting a CIM, or organizing company data for a sale process.
- **Workflow sections:** Workflow / Important Notes
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/investment-banking:cim-builder`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\skills\cim-builder\SKILL.md`

#### `datapack-builder`

- **Purpose:** Build professional financial services data packs from various sources including CIMs, offering memorandums, SEC filings, web search, or MCP servers. Extract, normalize, and standardize financial data into investment committee-ready Excel workbooks with consistent structure, proper formatting, and documented assumptions. Use for M&A due diligence, private equity analysis, investment committee materials, and standardizing financial reporting across portfolio companies. Do not use for simple financ ...
- **Workflow sections:** CRITICAL SUCCESS FACTORS / Structural Consistency / STEP-BY-STEP WORKFLOW / NORMALIZATION PATTERNS / INDUSTRY-SPECIFIC ADAPTATIONS / FINAL DELIVERY CHECKLIST
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/investment-banking:datapack-builder`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\skills\datapack-builder\SKILL.md`

#### `deal-tracker`

- **Purpose:** Track multiple live deals with milestones, deadlines, action items, and status updates. Maintains a deal pipeline view and surfaces upcoming deadlines and overdue items. Use when managing a book of business, tracking process milestones, or preparing for weekly deal reviews. Triggers on "deal tracker", "deal status", "where are we on", "process update", "deal pipeline", or "weekly deal review".
- **When to use:** Use when managing a book of business, tracking process milestones, or preparing for weekly deal reviews.
- **Workflow sections:** Workflow / Important Notes
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/investment-banking:deal-tracker`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\skills\deal-tracker\SKILL.md`

#### `fsi-strip-profile`

- **Purpose:** | | Creates professional investment banking strip profiles (company profiles) for pitch books, deal materials, and client presentations. Generates 1-4 information-dense slides with quadrant layouts, charts, and tables.
- **Workflow sections:** Workflow / Slide Format Requirements / First Page Layout / Subsequent Pages: Free-Form Layouts / Charts (Multi-Slide Profiles) / Financial Data Formatting / Quality Checklist
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/investment-banking:fsi-strip-profile`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\skills\strip-profile\SKILL.md`

#### `merger-model`

- **Purpose:** Build accretion/dilution analysis for M&A transactions. Models pro forma EPS impact, synergy sensitivities, and purchase price allocation. Use when evaluating a potential acquisition, preparing merger consequences analysis for a pitch, or advising on deal terms. Triggers on "merger model", "accretion dilution", "M&A model", "pro forma EPS", "merger consequences", or "deal impact analysis".
- **When to use:** Use when evaluating a potential acquisition, preparing merger consequences analysis for a pitch, or advising on deal terms.
- **Workflow sections:** Workflow / Important Notes
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/investment-banking:merger-model`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\skills\merger-model\SKILL.md`

#### `pitch-deck`

- **Purpose:** Populates investment banking pitch deck templates with data from source files. Use when: user provides a PowerPoint template to fill in, user has source data (Excel/CSV) to populate into slides, user mentions populating or filling a pitch deck template, or user needs to transfer data into existing slide layouts. Not for creating presentations from scratch.
- **When to use:** Use when: user provides a PowerPoint template to fill in, user has source data (Excel/CSV) to populate into slides, user mentions populating or filling a pitch deck template, or user needs to transfer data into existing slide layouts.
- **Workflow sections:** Reference Files / Workflow Decision Tree / ⚠️ Critical Rendering Limitation / Template Population Workflow / Quick Reference Tables / MUST Requirements / Critical Anti-Patterns: NEVER DO THESE / Common Failures
- **Dependencies / tools:** bundled: `reference/`
- **Invocation:** `/investment-banking:pitch-deck`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\skills\pitch-deck\SKILL.md`

#### `process-letter`

- **Purpose:** Draft process letters and bid instructions for sell-side M&A processes. Covers initial indication of interest (IOI) instructions, final bid procedures, and management meeting logistics. Triggers on "process letter", "bid instructions", "IOI letter", "bid procedures", "final round letter", or "management meeting invite".
- **Workflow sections:** Workflow / Important Notes
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/investment-banking:process-letter`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\skills\process-letter\SKILL.md`

#### `teaser`

- **Purpose:** Draft anonymous one-page company teasers for sell-side M&A processes. Creates a compelling summary without revealing the company's identity, designed to gauge buyer interest before NDA execution. Triggers on "teaser", "blind teaser", "anonymous profile", "one-pager for process", or "draft teaser for sell-side".
- **Workflow sections:** Workflow / Important Notes
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/investment-banking:teaser`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\skills\teaser\SKILL.md`

---

### Synced plugin `fund-admin`

*6 skills.*

#### `accrual-schedule`

- **Purpose:** Build the period-end accrual schedule — for each accrual, compute the entry, cite the support, and draft the JE. Use during month-end close; the JE is a draft for controller approval, not a posting.
- **Workflow sections:** For each accrual on the policy list / Draft JE / Output
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/fund-admin:accrual-schedule`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\fund-admin\skills\accrual-schedule\SKILL.md`

#### `break-trace`

- **Purpose:** Root-cause a reconciliation break to its source transaction or posting — follow the audit trail from the break row back to the originating entry on each side and state what differs and why. Use after gl-recon has classified a break.
- **Workflow sections:** Trace path / Cause → statement / Output
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/fund-admin:break-trace`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\fund-admin\skills\break-trace\SKILL.md`

#### `gl-recon`

- **Purpose:** Reconcile general ledger to subledger for a trade date or period — match at the position or transaction level, surface breaks, and classify each break by likely cause. Use for daily or month-end recon runs across asset classes.
- **Workflow sections:** Step 1: Normalize both sides / Step 2: Match / Step 3: Classify likely cause / Step 4: Output
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/fund-admin:gl-recon`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\fund-admin\skills\gl-recon\SKILL.md`

#### `nav-tieout`

- **Purpose:** Tie an LP statement to the fund's NAV pack — recompute the LP's capital account from the NAV components and flag any line that doesn't agree. Use before LP statements are distributed.
- **Workflow sections:** Recompute the LP capital account / Compare / Additional checks / Output
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/fund-admin:nav-tieout`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\fund-admin\skills\nav-tieout\SKILL.md`

#### `roll-forward`

- **Purpose:** Build a roll-forward schedule for a balance-sheet account — beginning balance plus activity less reversals equals ending balance, with each component tied to GL. Use for month-end close packages and audit support.
- **Workflow sections:** Structure / Tie each line / Output
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/fund-admin:roll-forward`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\fund-admin\skills\roll-forward\SKILL.md`

#### `variance-commentary`

- **Purpose:** Write flux commentary for every P&L and balance-sheet line over threshold — current vs prior period and vs budget, with the driver explained from underlying activity. Use for the month-end close package and management reporting.
- **Workflow sections:** Threshold / For each flagged line / Sourcing the driver / Output
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/fund-admin:variance-commentary`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\fund-admin\skills\variance-commentary\SKILL.md`

---

### Synced plugin `market-researcher`

*5 skills.*

#### `competitive-analysis`

- **Purpose:** Framework for building competitive landscape decks — market positioning, competitor deep-dives, comparative analysis, strategic synthesis. Use when the user asks for a competitive landscape, competitor analysis, peer comparison, market positioning assessment, strategic review, or investment memo deck. Also triggers on "who are the competitors to X", "benchmark X against peers", "build a market map", or any request to systematically evaluate competitive dynamics across an industry.
- **When to use:** Use when the user asks for a competitive landscape, competitor analysis, peer comparison, market positioning assessment, strategic review, or investment memo deck.
- **Workflow sections:** Environment check / Phase 1 — Scope the analysis / Phase 2 — Outline, approve, then build / Standards — apply throughout / Analysis workflow / Quality checklist
- **Dependencies / tools:** bundled: `references/`
- **Invocation:** `/market-researcher:competitive-analysis`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\market-researcher\skills\competitive-analysis\SKILL.md`

#### `comps-analysis`

- **Purpose:** | | Build institutional-grade comparable company analyses with operating metrics, valuation multiples, and statistical benchmarking in Excel/spreadsheet format. | **Perfect for:** | - Public company valuation (M&A, investment analysis) | - Benchmarking performance vs. industry peers | - Pricing IPOs or funding rounds | - Identifying valuation outliers (over/under-valued) | - Supporting investment committee presentations | - Creating sector overview reports | **Not ideal for:** | - Private compan ...
- **Workflow sections:** ⚠️ CRITICAL: Data Source Priority (READ FIRST) / Overview / Core Philosophy / ⚠️ CRITICAL: Formulas Over Hardcodes + Step-by-Step Verification / Section 1: Document Structure & Setup / Section 2: Operating Statistics & Financial Metrics / Section 3: Valuation Multiples & Investment Metrics / Section 4: Notes & Methodology Documentation
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/market-researcher:comps-analysis`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\market-researcher\skills\comps-analysis\SKILL.md`

#### `idea-generation`

- **Purpose:** Systematic stock screening and investment idea sourcing. Combines quantitative screens, thematic research, and pattern recognition to surface new long and short ideas. Use when looking for new ideas, running screens, or conducting thematic sweeps. Triggers on "idea generation", "stock screen", "find ideas", "what looks interesting", "screen for", "new ideas", or "pitch me something".
- **When to use:** Use when looking for new ideas, running screens, or conducting thematic sweeps.
- **Workflow sections:** Workflow / Important Notes
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/market-researcher:idea-generation`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\market-researcher\skills\idea-generation\SKILL.md`

#### `pptx-author`

- **Purpose:** Produce a .pptx file on disk (headless) instead of driving a live PowerPoint document — for managed-agent sessions with no open Office app.
- **Workflow sections:** Output contract / How to build the deck / Conventions (mirror the live-Office `pitch-deck` skill) / When NOT to use
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/market-researcher:pptx-author`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\market-researcher\skills\pptx-author\SKILL.md`

#### `sector-overview`

- **Purpose:** Create comprehensive industry and sector landscape reports covering market dynamics, competitive positioning, key players, and thematic trends. Use for client requests, sector initiations, thematic research pieces, or internal knowledge building. Triggers on "sector overview", "industry report", "market landscape", "sector analysis", "industry deep dive", or "thematic research".
- **Workflow sections:** Workflow / Important Notes
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/market-researcher:sector-overview`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\market-researcher\skills\sector-overview\SKILL.md`

---

### Synced plugin `meeting-prep-agent`

*4 skills.*

#### `client-report`

- **Purpose:** Generate professional client-facing performance reports with portfolio returns, allocation breakdowns, and market commentary. Suitable for quarterly or annual distribution. Triggers on "client report", "performance report", "quarterly report for [client]", "generate reports", or "client statement".
- **Workflow sections:** Workflow / Important Notes
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/meeting-prep-agent:client-report`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\meeting-prep-agent\skills\client-report\SKILL.md`

#### `client-review`

- **Purpose:** Prepare for client review meetings with portfolio performance summary, allocation analysis, talking points, and action items. Pulls together account data into a concise meeting-ready format. Use before quarterly reviews, annual checkups, or ad-hoc client meetings. Triggers on "client review", "meeting prep for [client]", "quarterly review", "prep for [client name]", or "client meeting".
- **Workflow sections:** Workflow / Important Notes
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/meeting-prep-agent:client-review`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\meeting-prep-agent\skills\client-review\SKILL.md`

#### `investment-proposal`

- **Purpose:** Create professional investment proposals for prospective clients. Covers the firm's approach, proposed allocation, expected outcomes, and fee structure. Use when pitching new clients or presenting a new investment strategy. Triggers on "investment proposal", "prospect presentation", "pitch new client", "proposal for [client]", or "new client presentation".
- **When to use:** Use when pitching new clients or presenting a new investment strategy.
- **Workflow sections:** Workflow / Important Notes
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/meeting-prep-agent:investment-proposal`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\meeting-prep-agent\skills\investment-proposal\SKILL.md`

#### `pptx-author`

- **Purpose:** Produce a .pptx file on disk (headless) instead of driving a live PowerPoint document — for managed-agent sessions with no open Office app.
- **Workflow sections:** Output contract / How to build the deck / Conventions (mirror the live-Office `pitch-deck` skill) / When NOT to use
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/meeting-prep-agent:pptx-author`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\meeting-prep-agent\skills\pptx-author\SKILL.md`

---

### Synced plugin `operations`

*2 skills.*

#### `kyc-doc-parse`

- **Purpose:** Parse an investor or client onboarding packet into structured KYC fields — identity, ownership, control, source of funds, and document inventory. Use as the first step of KYC screening; output feeds the rules engine.
- **Workflow sections:** Step 1: Inventory the packet / Step 2: Extract structured fields / Step 3: Flag obvious gaps
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/operations:kyc-doc-parse`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\operations\skills\kyc-doc-parse\SKILL.md`

#### `kyc-rules`

- **Purpose:** Apply the firm's KYC/AML rules grid to a parsed onboarding record — assign a risk rating, list every rule outcome with the rule cited, and flag what's missing or escalation-worthy. Use after kyc-doc-parse; this skill decides nothing, it scores and routes.
- **Workflow sections:** Step 1: Risk-rate / Step 2: Required-document check / Step 3: Rule outcomes / Step 4: Disposition
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/operations:kyc-rules`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\operations\skills\kyc-rules\SKILL.md`

---

### Synced plugin `claude-for-msft-365-install`

*1 skills.*

#### `verify`

- **Purpose:** Verify changes to the claude-for-msft-365-install admin scripts and commands by driving them against an isolated fake $HOME.
- **Workflow sections:** Lint gate / Drive the scripts against a fake $HOME / Prove storage is retained / Gotchas
- **Dependencies / tools:** none declared in frontmatter
- **Invocation:** `/claude-for-msft-365-install:verify`
- **Source:** `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\claude-for-msft-365-install\.claude\skills\verify\SKILL.md`

---

## 3. Skill Index

Compact table of all 372 skills, grouped by category. For `ecc`, the category is the derived domain described above; for every other bundle the category is the bundle itself.

### Personal (synced) (9)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `docs` | docs (editable docs people share and comment on; the default for any document, named as a doc or not: a docume ... | `C:\Users\tamar\.claude\skills\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\docs\SKILL.md` |
| `docx` | Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx) or Word tem ... | `C:\Users\tamar\.claude\skills\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\docx\SKILL.md` |
| `google-workspace` | Read this before the first Google Drive, Docs, Sheets or Slides connector call whenever the task creates or ch ... | `C:\Users\tamar\.claude\skills\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\google-workspace\SKILL.md` |
| `import-memory` | Import a memory export from another AI assistant into Claude's memory — conversationally, additively, and with ... | `C:\Users\tamar\.claude\skills\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\import-memory\SKILL.md` |
| `morning` | Render the user's morning brief as a styled HTML artifact, or set it up as a recurring weekday task. Use only ... | `C:\Users\tamar\.claude\skills\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\morning\SKILL.md` |
| `pdf` | Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text ... | `C:\Users\tamar\.claude\skills\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\pdf\SKILL.md` |
| `pptx` | Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This include ... | `C:\Users\tamar\.claude\skills\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\pptx\SKILL.md` |
| `skill-creator` | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to c ... | `C:\Users\tamar\.claude\skills\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\skill-creator\SKILL.md` |
| `xlsx` | Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user ... | `C:\Users\tamar\.claude\skills\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\xlsx\SKILL.md` |

### Plugin: caveman (7)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `cavecrew` | > / Decision guide for delegating to caveman-style subagents. Tells the main / thread WHEN to spawn `cavecrew- ... | `C:\Users\tamar\.claude\plugins\cache\caveman\caveman\11ddc0c9813c\skills\cavecrew\SKILL.md` |
| `caveman` | > / Ultra-compressed communication mode. Cuts output tokens 65% (measured) by speaking like caveman / while ke ... | `C:\Users\tamar\.claude\plugins\cache\caveman\caveman\11ddc0c9813c\skills\caveman\SKILL.md` |
| `caveman-commit` | > / Ultra-compressed commit message generator. Cuts noise from commit messages while preserving / intent and r ... | `C:\Users\tamar\.claude\plugins\cache\caveman\caveman\11ddc0c9813c\skills\caveman-commit\SKILL.md` |
| `caveman-compress` | > / Compress natural language memory files (CLAUDE.md, todos, preferences) into caveman format / to save input ... | `C:\Users\tamar\.claude\plugins\cache\caveman\caveman\11ddc0c9813c\skills\caveman-compress\SKILL.md` |
| `caveman-help` | > / Quick-reference card for all caveman modes, skills, and commands. / One-shot display, not a persistent mod ... | `C:\Users\tamar\.claude\plugins\cache\caveman\caveman\11ddc0c9813c\skills\caveman-help\SKILL.md` |
| `caveman-review` | > / Ultra-compressed code review comments. Cuts noise from PR feedback while preserving / the actionable signa ... | `C:\Users\tamar\.claude\plugins\cache\caveman\caveman\11ddc0c9813c\skills\caveman-review\SKILL.md` |
| `caveman-stats` | > / Show real token usage and estimated savings for the current session. / Reads directly from the Claude Code ... | `C:\Users\tamar\.claude\plugins\cache\caveman\caveman\11ddc0c9813c\skills\caveman-stats\SKILL.md` |

### Plugin: claude-mem (19)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `babysit` | Watch a pull request or review cycle until it is ready to merge. Use when asked to babysit, monitor, or keep c ... | `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\babysit\SKILL.md` |
| `cloud-sync` | Set up or check claude-mem cloud sync with cmem.ai Pro. Use when the user says "set up cloud sync", "sync my m ... | `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\cloud-sync\SKILL.md` |
| `design-is` | Audit a design against Dieter Rams' ten "Good design is..." principles, then hand off a /make-plan prompt for ... | `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\design-is\SKILL.md` |
| `do` | Execute a phased implementation plan using subagents. Use when asked to execute, run, or carry out a plan — es ... | `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\do\SKILL.md` |
| `how-it-works` | Explain how claude-mem captures observations, when memory injection kicks in, and where data lives. Use when t ... | `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\how-it-works\SKILL.md` |
| `knowledge-agent` | Build and query AI-powered knowledge bases from claude-mem observations. Use when users want to create focused ... | `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\knowledge-agent\SKILL.md` |
| `learn-codebase` | Prime a codebase by reading every source file in full. Use when starting work on a new or unfamiliar project, ... | `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\learn-codebase\SKILL.md` |
| `make-plan` | Create a detailed, phased implementation plan with documentation discovery. Use when asked to plan a feature, ... | `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\make-plan\SKILL.md` |
| `mem-search` | Search claude-mem's persistent cross-session memory database. Use when user asks "did we already solve this?", ... | `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\mem-search\SKILL.md` |
| `mode-creator` | Interactively create, install, activate, and verify custom claude-mem modes, including domain-specific observa ... | `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\mode-creator\SKILL.md` |
| `oh-my-issues` | Cluster a GitHub issue backlog by root cause into a small set of plan-master issues, redirect children with a ... | `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\oh-my-issues\SKILL.md` |
| `pathfinder` | Map a codebase into feature-grouped flowcharts, identify duplicated concerns across features, and propose a un ... | `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\pathfinder\SKILL.md` |
| `smart-explore` | Token-optimized structural code search using tree-sitter AST parsing. Use instead of reading full files when y ... | `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\smart-explore\SKILL.md` |
| `standup` | Facilitate a read-only standup across git worktrees, branches, or PRs to compare changes and produce one conso ... | `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\standup\SKILL.md` |
| `timeline-report` | Generate a "Journey Into [Project]" narrative report analyzing a project's entire development history from cla ... | `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\timeline-report\SKILL.md` |
| `version-bump` | Automated semantic versioning and release workflow for Claude Code plugins. Handles version increments across ... | `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\version-bump\SKILL.md` |
| `weekly-digests` | Generate a serial week-by-week narrative digest of a project's full claude-mem timeline. Splits the timeline i ... | `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\weekly-digests\SKILL.md` |
| `what-the` | What the? Use when the user wants a plain-English breakdown of something technical — the who, what, where, why ... | `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\what-the\SKILL.md` |
| `wowerpoint` | Turn one document into a kawaii NotebookLM slide-deck PDF. Use for "wowerpoint this", "make a deck about <file ... | `C:\Users\tamar\.claude\plugins\cache\thedotmack\claude-mem\13.14.0\skills\wowerpoint\SKILL.md` |

### Plugin: ponytail (6)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `ponytail` | > / Forces the laziest solution that actually works, simplest, shortest, most / minimal. Channels a senior dev ... | `C:\Users\tamar\.claude\plugins\cache\ponytail\ponytail\4.9.0\skills\ponytail\SKILL.md` |
| `ponytail-audit` | > / Whole-repo audit for over-engineering. Like ponytail-review, but scans the / entire codebase instead of a ... | `C:\Users\tamar\.claude\plugins\cache\ponytail\ponytail\4.9.0\skills\ponytail-audit\SKILL.md` |
| `ponytail-debt` | > / Harvest every `ponytail:` comment in the codebase into a debt ledger, so the / deliberate shortcuts and de ... | `C:\Users\tamar\.claude\plugins\cache\ponytail\ponytail\4.9.0\skills\ponytail-debt\SKILL.md` |
| `ponytail-gain` | > / Show ponytail's measured impact as a compact scoreboard: less code, less / cost, more speed, from the benc ... | `C:\Users\tamar\.claude\plugins\cache\ponytail\ponytail\4.9.0\skills\ponytail-gain\SKILL.md` |
| `ponytail-help` | > / Quick-reference card for all ponytail modes, skills, and commands. / One-shot display, not a persistent mo ... | `C:\Users\tamar\.claude\plugins\cache\ponytail\ponytail\4.9.0\skills\ponytail-help\SKILL.md` |
| `ponytail-review` | > / Code review focused exclusively on over-engineering. Finds what to delete: / reinvented standard library, ... | `C:\Users\tamar\.claude\plugins\cache\ponytail\ponytail\4.9.0\skills\ponytail-review\SKILL.md` |

### Plugin: ui-ux-pro-max (7)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `banner-design` | Design banners for social media, ads, website heroes, creative assets, and print. Multiple art direction optio ... | `C:\Users\tamar\.claude\plugins\cache\ui-ux-pro-max-skill\ui-ux-pro-max\2.13.0\.claude\skills\banner-design\SKILL.md` |
| `brand` | Brand voice, visual identity, messaging frameworks, asset management, brand consistency. Activate for branded ... | `C:\Users\tamar\.claude\plugins\cache\ui-ux-pro-max-skill\ui-ux-pro-max\2.13.0\.claude\skills\brand\SKILL.md` |
| `design` | Comprehensive design skill: brand identity, design tokens, UI styling, logo generation (55 styles, Gemini AI), ... | `C:\Users\tamar\.claude\plugins\cache\ui-ux-pro-max-skill\ui-ux-pro-max\2.13.0\.claude\skills\design\SKILL.md` |
| `design-system` | Token architecture, component specifications, and slide generation. Three-layer tokens (primitive→semantic→com ... | `C:\Users\tamar\.claude\plugins\cache\ui-ux-pro-max-skill\ui-ux-pro-max\2.13.0\.claude\skills\design-system\SKILL.md` |
| `slides` | Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas, an ... | `C:\Users\tamar\.claude\plugins\cache\ui-ux-pro-max-skill\ui-ux-pro-max\2.13.0\.claude\skills\slides\SKILL.md` |
| `ui-styling` | Create beautiful, accessible user interfaces with shadcn/ui components (built on Radix UI + Tailwind), Tailwin ... | `C:\Users\tamar\.claude\plugins\cache\ui-ux-pro-max-skill\ui-ux-pro-max\2.13.0\.claude\skills\ui-styling\SKILL.md` |
| `ui-ux-pro-max` | UI/UX design intelligence for web and mobile. Searchable local database with 84 styles, 192 color palettes, 74 ... | `C:\Users\tamar\.claude\plugins\cache\ui-ux-pro-max-skill\ui-ux-pro-max\2.13.0\.claude\skills\ui-ux-pro-max\SKILL.md` |

### Synced plugin: claude-for-msft-365-install (1)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `verify` | Verify changes to the claude-for-msft-365-install admin scripts and commands by driving them against an isolat ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\claude-for-msft-365-install\.claude\skills\verify\SKILL.md` |

### Synced plugin: financial-analysis (13)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `3-statement-model` | Complete, populate and fill out 3-statement financial model templates (Income Statement, Balance Sheet, Cash F ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\3-statement-model\SKILL.md` |
| `audit-xls` | Audit a spreadsheet for formula accuracy, errors, and common mistakes. Scopes to a selected range, a single sh ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\audit-xls\SKILL.md` |
| `clean-data-xls` | Clean up messy spreadsheet data — trim whitespace, fix inconsistent casing, convert numbers-stored-as-text, st ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\clean-data-xls\SKILL.md` |
| `competitive-analysis` | Framework for building competitive landscape decks — market positioning, competitor deep-dives, comparative an ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\competitive-analysis\SKILL.md` |
| `comps-analysis` | / / Build institutional-grade comparable company analyses with operating metrics, valuation multiples, and sta ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\comps-analysis\SKILL.md` |
| `dcf-model` | Real DCF (Discounted Cash Flow) model creation for equity valuation. Retrieves financial data from SEC filings ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\dcf-model\SKILL.md` |
| `deck-refresh` | Updates a presentation with new numbers — quarterly refreshes, earnings updates, comp rolls, rebased market da ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\deck-refresh\SKILL.md` |
| `ib-check-deck` | Investment banking presentation quality checker. Reviews a pitch deck or client-ready presentation for (1) num ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\ib-check-deck\SKILL.md` |
| `lbo-model` | This skill should be used when completing LBO (Leveraged Buyout) model templates in Excel for private equity t ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\lbo-model\SKILL.md` |
| `ppt-template-creator` | Creates self-contained PPT template SKILLS (not presentations) from user-provided PowerPoint templates. Use ON ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\ppt-template-creator\SKILL.md` |
| `pptx-author` | Produce a .pptx file on disk (headless) instead of driving a live PowerPoint document — for managed-agent sess ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\pptx-author\SKILL.md` |
| `skill-creator` | Guide for creating effective skills. This skill should be used when users want to create a new skill (or updat ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\skill-creator\SKILL.md` |
| `xlsx-author` | Produce a .xlsx file on disk (headless) instead of driving a live Excel workbook — for managed-agent sessions ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\skills\xlsx-author\SKILL.md` |

### Synced plugin: fund-admin (6)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `accrual-schedule` | Build the period-end accrual schedule — for each accrual, compute the entry, cite the support, and draft the J ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\fund-admin\skills\accrual-schedule\SKILL.md` |
| `break-trace` | Root-cause a reconciliation break to its source transaction or posting — follow the audit trail from the break ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\fund-admin\skills\break-trace\SKILL.md` |
| `gl-recon` | Reconcile general ledger to subledger for a trade date or period — match at the position or transaction level, ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\fund-admin\skills\gl-recon\SKILL.md` |
| `nav-tieout` | Tie an LP statement to the fund's NAV pack — recompute the LP's capital account from the NAV components and fl ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\fund-admin\skills\nav-tieout\SKILL.md` |
| `roll-forward` | Build a roll-forward schedule for a balance-sheet account — beginning balance plus activity less reversals equ ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\fund-admin\skills\roll-forward\SKILL.md` |
| `variance-commentary` | Write flux commentary for every P&L and balance-sheet line over threshold — current vs prior period and vs bud ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\fund-admin\skills\variance-commentary\SKILL.md` |

### Synced plugin: investment-banking (9)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `buyer-list` | Build and organize a universe of potential acquirers for sell-side M&A processes. Identifies strategic and fin ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\skills\buyer-list\SKILL.md` |
| `cim-builder` | Structure and draft a Confidential Information Memorandum for sell-side M&A processes. Organizes company infor ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\skills\cim-builder\SKILL.md` |
| `datapack-builder` | Build professional financial services data packs from various sources including CIMs, offering memorandums, SE ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\skills\datapack-builder\SKILL.md` |
| `deal-tracker` | Track multiple live deals with milestones, deadlines, action items, and status updates. Maintains a deal pipel ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\skills\deal-tracker\SKILL.md` |
| `fsi-strip-profile` | / / Creates professional investment banking strip profiles (company profiles) for pitch books, deal materials, ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\skills\strip-profile\SKILL.md` |
| `merger-model` | Build accretion/dilution analysis for M&A transactions. Models pro forma EPS impact, synergy sensitivities, an ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\skills\merger-model\SKILL.md` |
| `pitch-deck` | Populates investment banking pitch deck templates with data from source files. Use when: user provides a Power ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\skills\pitch-deck\SKILL.md` |
| `process-letter` | Draft process letters and bid instructions for sell-side M&A processes. Covers initial indication of interest ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\skills\process-letter\SKILL.md` |
| `teaser` | Draft anonymous one-page company teasers for sell-side M&A processes. Creates a compelling summary without rev ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\skills\teaser\SKILL.md` |

### Synced plugin: market-researcher (5)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `competitive-analysis` | Framework for building competitive landscape decks — market positioning, competitor deep-dives, comparative an ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\market-researcher\skills\competitive-analysis\SKILL.md` |
| `comps-analysis` | / / Build institutional-grade comparable company analyses with operating metrics, valuation multiples, and sta ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\market-researcher\skills\comps-analysis\SKILL.md` |
| `idea-generation` | Systematic stock screening and investment idea sourcing. Combines quantitative screens, thematic research, and ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\market-researcher\skills\idea-generation\SKILL.md` |
| `pptx-author` | Produce a .pptx file on disk (headless) instead of driving a live PowerPoint document — for managed-agent sess ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\market-researcher\skills\pptx-author\SKILL.md` |
| `sector-overview` | Create comprehensive industry and sector landscape reports covering market dynamics, competitive positioning, ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\market-researcher\skills\sector-overview\SKILL.md` |

### Synced plugin: meeting-prep-agent (4)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `client-report` | Generate professional client-facing performance reports with portfolio returns, allocation breakdowns, and mar ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\meeting-prep-agent\skills\client-report\SKILL.md` |
| `client-review` | Prepare for client review meetings with portfolio performance summary, allocation analysis, talking points, an ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\meeting-prep-agent\skills\client-review\SKILL.md` |
| `investment-proposal` | Create professional investment proposals for prospective clients. Covers the firm's approach, proposed allocat ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\meeting-prep-agent\skills\investment-proposal\SKILL.md` |
| `pptx-author` | Produce a .pptx file on disk (headless) instead of driving a live PowerPoint document — for managed-agent sess ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\meeting-prep-agent\skills\pptx-author\SKILL.md` |

### Synced plugin: operations (2)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `kyc-doc-parse` | Parse an investor or client onboarding packet into structured KYC fields — identity, ownership, control, sourc ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\operations\skills\kyc-doc-parse\SKILL.md` |
| `kyc-rules` | Apply the firm's KYC/AML rules grid to a parsed onboarding record — assign a risk rating, list every rule outc ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\operations\skills\kyc-rules\SKILL.md` |

### ecc - Agents & orchestration (51)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `agent-architecture-audit` | Full-stack diagnostic for agent and LLM applications. Audits the 12-layer agent stack for wrapper regression, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\agent-architecture-audit\SKILL.md` |
| `agent-eval` | Head-to-head comparison of coding agents (Claude Code, Aider, Codex, etc.) on custom tasks with pass rate, cos ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\agent-eval\SKILL.md` |
| `agent-harness-construction` | Design and optimize AI agent action spaces, tool definitions, and observation formatting for higher completion ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\agent-harness-construction\SKILL.md` |
| `agent-introspection-debugging` | Structured self-debugging workflow for AI agent failures using capture, diagnosis, contained recovery, and int ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\agent-introspection-debugging\SKILL.md` |
| `agent-payment-x402` | Add x402 payment execution to AI agents with per-task budgets, spending controls, and non-custodial wallets. S ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\agent-payment-x402\SKILL.md` |
| `agent-self-evaluation` | Use after completing any non-trivial task. The agent self-rates its output on 5 axes — accuracy, completeness, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\agent-self-evaluation\SKILL.md` |
| `agent-sort` | Build an evidence-backed ECC install plan for a specific repo by sorting skills, commands, rules, hooks, and e ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\agent-sort\SKILL.md` |
| `agentic-engineering` | Operate as an agentic engineer using eval-first execution, decomposition, and cost-aware model routing. | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\agentic-engineering\SKILL.md` |
| `agentic-os` | Build persistent multi-agent operating systems on Claude Code. Covers kernel architecture, specialist agents, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\agentic-os\SKILL.md` |
| `ai-first-engineering` | Engineering operating model for teams where AI agents generate a large share of implementation output. | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ai-first-engineering\SKILL.md` |
| `autonomous-agent-harness` | Transform Claude Code into a fully autonomous agent system with persistent memory, scheduled operations, compu ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\autonomous-agent-harness\SKILL.md` |
| `autonomous-loops` | Patterns and architectures for autonomous Claude Code loops — from simple sequential pipelines to RFC-driven m ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\autonomous-loops\SKILL.md` |
| `benchmark-optimization-loop` | Use when the user asks to make something faster, try many variants, run recursive optimization, benchmark late ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\benchmark-optimization-loop\SKILL.md` |
| `claude-devfleet` | Orchestrate multi-agent coding tasks via Claude DevFleet — plan projects, dispatch parallel agents in isolated ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\claude-devfleet\SKILL.md` |
| `configure-ecc` | Guide ECC installation, update, or reconfiguration from inside Claude Code, Codex, or Kimi while respecting ea ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\configure-ecc\SKILL.md` |
| `continuous-agent-loop` | Patterns for continuous autonomous agent loops with quality gates, evals, and recovery controls. | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\continuous-agent-loop\SKILL.md` |
| `continuous-learning-v2` | Instinct-based learning system that observes sessions via hooks, creates atomic instincts with confidence scor ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\continuous-learning-v2\SKILL.md` |
| `council` | Convene a four-voice council for ambiguous decisions, tradeoffs, and go/no-go calls. Use when multiple valid p ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\council\SKILL.md` |
| `data-scraper-agent` | Build a fully automated AI-powered data collection agent for any public source — job boards, prices, news, Git ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\data-scraper-agent\SKILL.md` |
| `dmux-workflows` | Multi-agent orchestration using dmux (tmux pane manager for AI agents). Patterns for parallel agent workflows ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\dmux-workflows\SKILL.md` |
| `dynamic-workflow-mode` | Design task-local harnesses, eval gates, and reusable skill extraction for Claude dynamic workflow mode and ot ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\dynamic-workflow-mode\SKILL.md` |
| `enterprise-agent-ops` | Operate long-lived agent workloads with observability, security boundaries, and lifecycle management. | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\enterprise-agent-ops\SKILL.md` |
| `eval-harness` | Formal evaluation framework for Claude Code sessions implementing eval-driven development (EDD) principles | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\eval-harness\SKILL.md` |
| `flox-environments` | Create reproducible, cross-platform (macOS/Linux) development environments with Flox, a declarative Nix-based ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\flox-environments\SKILL.md` |
| `gan-style-harness` | GAN-inspired Generator-Evaluator agent harness for building high-quality applications autonomously. Based on A ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\gan-style-harness\SKILL.md` |
| `gateguard` | Fact-forcing gate that blocks Edit/Write/Bash (including MultiEdit) and demands concrete investigation (import ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\gateguard\SKILL.md` |
| `healthcare-eval-harness` | Patient safety evaluation harness for healthcare application deployments. Automated test suites for CDSS accur ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\healthcare-eval-harness\SKILL.md` |
| `inherit-legacy-style` | Legacy-project style inheritance skill. Use when the user types /inherit-legacy-style, or when onboarding an A ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\inherit-legacy-style\SKILL.md` |
| `intent-driven-development` | Turn ambiguous or high-impact product and engineering changes into scoped, verifiable acceptance criteria befo ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\intent-driven-development\SKILL.md` |
| `ito-data-atlas-agent` | Design source-grounded Data Atlas style agents for Itô basket research, market discovery, parameter drafting, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ito-data-atlas-agent\SKILL.md` |
| `latency-critical-systems` | Use for latency-sensitive systems such as realtime dashboards, market data, streaming agents, execution gatewa ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\latency-critical-systems\SKILL.md` |
| `lead-intelligence` | AI-native lead intelligence and outreach pipeline. Replaces Apollo, Clay, and ZoomInfo with agent-powered sign ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\lead-intelligence\SKILL.md` |
| `llm-trading-agent-security` | Security patterns for autonomous trading agents with wallet or transaction authority. Covers prompt injection, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\llm-trading-agent-security\SKILL.md` |
| `loop-design-check` | Design a goal-oriented agent loop, and review it for the ways loops go wrong — spinning and burning tokens, Go ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\loop-design-check\SKILL.md` |
| `ml-adoption-playbook` | End-to-end methodology for AI agents and software engineers to add machine learning algorithms to existing non ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ml-adoption-playbook\SKILL.md` |
| `nanoclaw-repl` | Operate and extend NanoClaw v2, ECC's zero-dependency session-aware REPL built on claude -p. | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\nanoclaw-repl\SKILL.md` |
| `openclaw-persona-forge` | 为 OpenClaw AI Agent 锻造完整的龙虾灵魂方案。根据用户偏好或随机抽卡， 输出身份定位、灵魂描述(SOUL.md)、角色化底线规则、名字和头像生图提示词。 如当前环境提供已审核的生图 skill，可自动生 ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\openclaw-persona-forge\SKILL.md` |
| `orch-add-feature` | Orchestrate building a brand-new feature end to end — research, plan, TDD implementation, review, and gated co ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\orch-add-feature\SKILL.md` |
| `orch-change-feature` | Orchestrate altering an existing, working feature to new desired behavior — update its tests to the new spec, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\orch-change-feature\SKILL.md` |
| `orch-fix-defect` | Orchestrate fixing a bug — reproduce it as a failing regression test, fix to green, review, and gated commit — ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\orch-fix-defect\SKILL.md` |
| `orch-refine-code` | Orchestrate a behavior-preserving refactor — confirm tests are green, restructure without changing behavior, k ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\orch-refine-code\SKILL.md` |
| `parallel-execution-optimizer` | Use when the user wants a task done much faster through parallel work, concurrent agents, batched tool calls, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\parallel-execution-optimizer\SKILL.md` |
| `plan-orchestrate` | Read a plan document, decompose it into steps, design a per-step agent chain from the ECC catalogue, and emit ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\plan-orchestrate\SKILL.md` |
| `prompt-optimizer` | >- / Analyze raw prompts, identify intent and gaps, match ECC components / (skills/commands/agents/hooks), and ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\prompt-optimizer\SKILL.md` |
| `safety-guard` | Use this skill to prevent destructive operations when working on production systems or running agents autonomo ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\safety-guard\SKILL.md` |
| `santa-method` | Multi-agent adversarial verification with convergence loop. Two independent review agents must both pass befor ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\santa-method\SKILL.md` |
| `skill-comply` | Visualize whether skills, rules, and agent definitions are actually followed — auto-generates scenarios at 3 p ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\skill-comply\SKILL.md` |
| `skill-stocktake` | Use when auditing Claude skills and commands for quality. Supports Quick Scan (changed skills only) and Full S ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\skill-stocktake\SKILL.md` |
| `social-publisher` | Agent-driven scheduling and publishing of social media posts across 13 platforms via SocialClaw. Use when the ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\social-publisher\SKILL.md` |
| `team-agent-orchestration` | Run team-based orchestration for agent squads using work items, ownership, agent Kanban, merge gates, and cont ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\team-agent-orchestration\SKILL.md` |
| `verification-loop` | A comprehensive verification system for Claude Code sessions. | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\verification-loop\SKILL.md` |

### ecc - Data & databases (5)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `clickhouse-io` | ClickHouse database patterns, query optimization, analytics, and data engineering best practices for high-perf ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\clickhouse-io\SKILL.md` |
| `data-throughput-accelerator` | Use when large data ingestion, backfill, export, ETL, warehouse loading, manifest catch-up, or table synchroni ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\data-throughput-accelerator\SKILL.md` |
| `database-migrations` | Database migration best practices for schema changes, data migrations, rollbacks, and zero-downtime deployment ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\database-migrations\SKILL.md` |
| `pubmed-database` | Direct PubMed and NCBI E-utilities search workflows for biomedical literature, MeSH queries, PMID lookup, cita ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\scientific-db-pubmed-database\SKILL.md` |
| `uspto-database` | USPTO patent and trademark data workflow for official record lookup, PatentSearch queries, TSDR checks, assign ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\scientific-db-uspto-database\SKILL.md` |

### ecc - Docs, writing & content (10)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `article-writing` | Write articles, guides, blog posts, tutorials, newsletter issues, and other long-form content in a distinctive ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\article-writing\SKILL.md` |
| `code-tour` | Create CodeTour `.tour` files — persona-targeted, step-by-step walkthroughs with real file and line anchors. U ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\code-tour\SKILL.md` |
| `codebase-onboarding` | Analyze an unfamiliar codebase and generate a structured onboarding guide with architecture map, key entry poi ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\codebase-onboarding\SKILL.md` |
| `content-engine` | Create platform-native content systems for X, LinkedIn, TikTok, YouTube, newsletters, and repurposed multi-pla ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\content-engine\SKILL.md` |
| `content-hash-cache-pattern` | Cache expensive file processing results using SHA-256 content hashes — path-independent, auto-invalidating, wi ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\content-hash-cache-pattern\SKILL.md` |
| `crosspost` | Multi-platform content distribution across X, LinkedIn, Threads, and Bluesky. Adapts content per platform usin ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\crosspost\SKILL.md` |
| `documentation-lookup` | Use up-to-date library and framework docs via Context7 MCP instead of training data. Activates for setup quest ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\documentation-lookup\SKILL.md` |
| `ito-basket-compare` | Compare Itô prediction-market baskets against a user's knowledge base, portfolio notes, financial context, wat ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ito-basket-compare\SKILL.md` |
| `nutrient-document-processing` | Process, convert, OCR, extract, redact, sign, and fill documents using the Nutrient DWS API. Works with PDFs, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\nutrient-document-processing\SKILL.md` |
| `visa-doc-translate` | Translate visa application documents (images) to English and create a bilingual PDF with original and translat ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\visa-doc-translate\SKILL.md` |

### ecc - Frontend, design & media (26)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `accessibility` | Design, implement, and audit inclusive digital products using WCAG 2.2 Level AA / standards. Use this skill to ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\accessibility\SKILL.md` |
| `api-connector-builder` | Build a new API connector or provider by matching the target repo's existing integration pattern exactly. Use ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\api-connector-builder\SKILL.md` |
| `api-design` | REST API design patterns including resource naming, status codes, pagination, filtering, error responses, vers ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\api-design\SKILL.md` |
| `blender-motion-state-inspection` | Use this skill when inspecting Blender characters, rigs, poses, animation retargeting, ground contact, facing ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\blender-motion-state-inspection\SKILL.md` |
| `brand-discovery` | >- / Use when a brand needs to discover or articulate its identity through / structured multi-session intervie ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\brand-discovery\SKILL.md` |
| `brand-voice` | Build a source-derived writing style profile from real posts, essays, launch notes, docs, or site copy, then r ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\brand-voice\SKILL.md` |
| `dashboard-builder` | Build monitoring dashboards that answer real operator questions for Grafana, SigNoz, and similar platforms. Us ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\dashboard-builder\SKILL.md` |
| `design-system` | Use this skill to generate or audit design systems, check visual consistency, and review PRs that touch stylin ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\design-system\SKILL.md` |
| `ecc-guide` | Guide users through ECC's current agents, skills, commands, hooks, rules, install profiles, and project onboar ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ecc-guide\SKILL.md` |
| `fal-ai-media` | Unified media generation via fal.ai MCP — image, video, and audio. Covers text-to-image (Nano Banana), text/im ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\fal-ai-media\SKILL.md` |
| `foundation-models-on-device` | Apple FoundationModels framework for on-device LLM — text generation, guided generation with @Generable, tool ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\foundation-models-on-device\SKILL.md` |
| `frontend-a11y` | > / Accessibility patterns for React and Next.js — semantic HTML, ARIA attributes, / form labeling, keyboard n ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\frontend-a11y\SKILL.md` |
| `frontend-design-direction` | Set an ECC-specific frontend design direction for production UI work. Use when building or improving websites, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\frontend-design-direction\SKILL.md` |
| `frontend-slides` | Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. Use when th ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\frontend-slides\SKILL.md` |
| `ios-icon-gen` | Generate iOS app icons as PNG imagesets for Xcode asset catalogs from SF Symbols (5000+ Apple-native) or Iconi ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ios-icon-gen\SKILL.md` |
| `liquid-glass-design` | iOS 26 Liquid Glass design system — dynamic glass material with blur, reflection, and interactive morphing for ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\liquid-glass-design\SKILL.md` |
| `make-interfaces-feel-better` | Apply concrete design-engineering details that make interfaces feel polished. Use when reviewing or improving ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\make-interfaces-feel-better\SKILL.md` |
| `manim-video` | Build reusable Manim explainers for technical concepts, graphs, system diagrams, and product walkthroughs, the ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\manim-video\SKILL.md` |
| `motion-ui` | Production-ready UI motion system for React/Next.js. Use when implementing animations, transitions, or motion ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\motion-ui\SKILL.md` |
| `orch-build-mvp` | Orchestrate bootstrapping a working MVP from a design or spec document — ingest the doc, plan thin vertical sl ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\orch-build-mvp\SKILL.md` |
| `remotion-video-creation` | Best practices for Remotion - Video creation in React. 29 domain-specific rules covering 3D, animations, audio ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\remotion-video-creation\SKILL.md` |
| `skill-scout` | Search existing local, marketplace, GitHub, and web skill sources before creating a new skill. Use when the us ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\skill-scout\SKILL.md` |
| `team-builder` | Interactive agent picker for composing and dispatching parallel teams | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\team-builder\SKILL.md` |
| `ui-demo` | Record polished UI demo videos using Playwright. Use when the user asks to create a demo, walkthrough, screen ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ui-demo\SKILL.md` |
| `video-editing` | AI-assisted video editing workflows for cutting, structuring, and augmenting real footage. Covers the full pip ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\video-editing\SKILL.md` |
| `videodb` | See, Understand, Act on video and audio. See- ingest from local files, URLs, RTSP/live feeds, or live record d ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\videodb\SKILL.md` |

### ecc - Infra, deploy & ops (31)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `canary-watch` | Use this skill to monitor and verify a deployed URL after releases — checks HTTP endpoints, SSE streams, stati ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\canary-watch\SKILL.md` |
| `connections-optimizer` | Reorganize the user's X and LinkedIn network with review-first pruning, add/follow recommendations, and channe ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\connections-optimizer\SKILL.md` |
| `cost-aware-llm-pipeline` | Cost optimization patterns for LLM API usage — model routing by task complexity, budget tracking, retry logic, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\cost-aware-llm-pipeline\SKILL.md` |
| `customer-billing-ops` | Operate customer billing workflows such as subscriptions, refunds, churn triage, billing-portal recovery, and ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\customer-billing-ops\SKILL.md` |
| `ecc-recipes` | Map a described workflow to the right ECC command-GROUP with run-order and stop condition, and browse all comm ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ecc-recipes\SKILL.md` |
| `email-ops` | Evidence-first mailbox triage, drafting, send verification, and sent-mail-safe follow-up workflow for ECC. Use ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\email-ops\SKILL.md` |
| `finance-billing-ops` | Evidence-first revenue, pricing, refunds, team-billing, and billing-model truth workflow for ECC. Use when the ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\finance-billing-ops\SKILL.md` |
| `github-ops` | GitHub repository operations, automation, and management. Issue triage, PR management, CI/CD operations, relea ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\github-ops\SKILL.md` |
| `google-workspace-ops` | Operate across Google Drive, Docs, Sheets, and Slides as one workflow surface for plans, trackers, decks, and ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\google-workspace-ops\SKILL.md` |
| `hermes-imports` | Convert local Hermes operator workflows into sanitized ECC skills and release-pack artifacts. Use when prepari ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\hermes-imports\SKILL.md` |
| `homelab-network-readiness` | Readiness checklist for homelab VLAN segmentation, local DNS filtering, and WireGuard-style remote access befo ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\homelab-network-readiness\SKILL.md` |
| `homelab-network-setup` | Practical home and homelab network planning for gateways, switches, access points, IP ranges, DHCP reservation ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\homelab-network-setup\SKILL.md` |
| `homelab-pihole-dns` | Pi-hole installation, blocklist management, DNS-over-HTTPS setup, DHCP integration, local DNS records, and tro ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\homelab-pihole-dns\SKILL.md` |
| `homelab-wireguard-vpn` | WireGuard VPN server setup, peer configuration, key generation, split tunneling vs full tunnel routing, and re ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\homelab-wireguard-vpn\SKILL.md` |
| `knowledge-ops` | Knowledge base management, ingestion, sync, and retrieval across multiple storage layers (local files, MCP mem ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\knowledge-ops\SKILL.md` |
| `messages-ops` | Evidence-first live messaging workflow for ECC. Use when the user wants to read texts or DMs, recover a recent ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\messages-ops\SKILL.md` |
| `network-bgp-diagnostics` | Diagnostics-only BGP troubleshooting patterns for neighbor state, route exchange, prefix policy, AS path inspe ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\network-bgp-diagnostics\SKILL.md` |
| `network-config-validation` | Pre-deployment checks for router and switch configuration, including dangerous commands, duplicate addresses, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\network-config-validation\SKILL.md` |
| `network-interface-health` | Diagnose interface errors, drops, CRCs, duplex mismatches, flapping, speed negotiation issues, and counter tre ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\network-interface-health\SKILL.md` |
| `opensource-pipeline` | Open-source pipeline: fork, sanitize, and package private projects for safe public release. Chains 3 agents (f ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\opensource-pipeline\SKILL.md` |
| `orch-pipeline` | Shared orchestration engine for the orch-* skill family. Defines the gated Research-Plan-TDD-Review-Commit pip ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\orch-pipeline\SKILL.md` |
| `project-flow-ops` | Operate execution flow across GitHub and Linear by triaging issues and pull requests, linking active work, and ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\project-flow-ops\SKILL.md` |
| `ralphinho-rfc-pipeline` | RFC-driven multi-agent DAG execution pattern with quality gates, merge queues, and work unit orchestration. | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ralphinho-rfc-pipeline\SKILL.md` |
| `recsys-pipeline-architect` | Design composable recommendation, ranking, and feed pipelines using the six-stage Source→Hydrator→Filter→Score ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\recsys-pipeline-architect\SKILL.md` |
| `recursive-decision-ledger` | Use when the user asks for repeated rollouts, marked decision processes, high-dimensional search, stochastic o ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\recursive-decision-ledger\SKILL.md` |
| `research-ops` | Evidence-first current-state research workflow for ECC. Use when the user wants fresh facts, comparisons, enri ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\research-ops\SKILL.md` |
| `social-graph-ranker` | Weighted social-graph ranking for warm intro discovery, bridge scoring, and network gap analysis across X and ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\social-graph-ranker\SKILL.md` |
| `taste` | A creative-direction (taste) layer for music videos and short-form edits in the angelcore / cloud-trance / hyp ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\taste\SKILL.md` |
| `terminal-ops` | Evidence-first repo execution workflow for ECC. Use when the user wants a command run, a repo checked, a CI fa ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\terminal-ops\SKILL.md` |
| `uncloud` | Use when managing an Uncloud cluster — deploying services, configuring Caddy ingress, adding static proxy rout ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\uncloud\SKILL.md` |
| `unified-notifications-ops` | Operate notifications as one ECC-native workflow across GitHub, Linear, desktop alerts, hooks, and connected c ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\unified-notifications-ops\SKILL.md` |

### ecc - Language & framework patterns (69)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `android-clean-architecture` | Clean Architecture patterns for Android and Kotlin Multiplatform projects — module structure, dependency rules ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\android-clean-architecture\SKILL.md` |
| `angular-developer` | Generates Angular code and provides architectural guidance. Trigger when creating projects, components, or ser ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\angular-developer\SKILL.md` |
| `backend-patterns` | Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\backend-patterns\SKILL.md` |
| `bun-runtime` | Bun as runtime, package manager, bundler, and test runner. When to choose Bun vs Node, migration notes, and Ve ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\bun-runtime\SKILL.md` |
| `cisco-ios-patterns` | Cisco IOS and IOS-XE review patterns for show commands, config hierarchy, wildcard masks, ACL placement, inter ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\cisco-ios-patterns\SKILL.md` |
| `ck` | Persistent per-project memory for Claude Code. Auto-loads project context on session start, tracks sessions wi ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ck\SKILL.md` |
| `coding-standards` | Baseline cross-project coding conventions for naming, readability, immutability, and code-quality review. Use ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\coding-standards\SKILL.md` |
| `compose-multiplatform-patterns` | Compose Multiplatform and Jetpack Compose patterns for KMP projects — state management, navigation, theming, p ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\compose-multiplatform-patterns\SKILL.md` |
| `cpp-coding-standards` | C++ coding standards based on the C++ Core Guidelines (isocpp.github.io). Use when writing, reviewing, or refa ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\cpp-coding-standards\SKILL.md` |
| `dart-flutter-patterns` | Production-ready Dart and Flutter patterns covering null safety, immutable state, async composition, widget ar ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\dart-flutter-patterns\SKILL.md` |
| `deployment-patterns` | Deployment workflows, CI/CD pipeline patterns, Docker containerization, health checks, rollback strategies, an ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\deployment-patterns\SKILL.md` |
| `django-celery` | Django + Celery async task patterns — configuration, task design, beat scheduling, retries, canvas workflows, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\django-celery\SKILL.md` |
| `django-patterns` | Django architecture patterns, REST API design with DRF, ORM best practices, caching, signals, middleware, and ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\django-patterns\SKILL.md` |
| `docker-patterns` | Docker and Docker Compose patterns for local development, hardened CLI installer harnesses, container security ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\docker-patterns\SKILL.md` |
| `dotnet-patterns` | Idiomatic C# and .NET patterns, conventions, dependency injection, async/await, and best practices for buildin ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\dotnet-patterns\SKILL.md` |
| `error-handling` | Patterns for robust error handling across TypeScript, Python, and Go. Covers typed errors, error boundaries, r ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\error-handling\SKILL.md` |
| `fastapi-patterns` | FastAPI best practices covering project structure, Pydantic v2 schemas, dependency injection, async handlers, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\fastapi-patterns\SKILL.md` |
| `flutter-dart-code-review` | Library-agnostic Flutter/Dart code review checklist covering widget best practices, state management patterns ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\flutter-dart-code-review\SKILL.md` |
| `frontend-patterns` | Frontend development patterns for React, Next.js, state management, performance optimization, and UI best prac ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\frontend-patterns\SKILL.md` |
| `generating-python-installer` | Commercial-grade Python installer expert for Windows: Nuitka extreme compilation, dist slimming, DLL footprint ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\generating-python-installer\SKILL.md` |
| `gget` | gget CLI and Python workflow for quick genomic database queries, sequence lookup, BLAST-style searches, enrich ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\scientific-pkg-gget\SKILL.md` |
| `golang-patterns` | Idiomatic Go patterns, best practices, and conventions for building robust, efficient, and maintainable Go app ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\golang-patterns\SKILL.md` |
| `growth-log` | Use after a complex task, failure, or when reviewing what was learned. Teaches how to write growth logs that e ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\growth-log\SKILL.md` |
| `healthcare-cdss-patterns` | Clinical Decision Support System (CDSS) development patterns. Drug interaction checking, dose validation, clin ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\healthcare-cdss-patterns\SKILL.md` |
| `healthcare-emr-patterns` | EMR/EHR development patterns for healthcare applications. Clinical safety, encounter workflows, prescription g ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\healthcare-emr-patterns\SKILL.md` |
| `homelab-vlan-segmentation` | Segmenting home networks into VLANs for IoT, guest, trusted, and server traffic using UniFi, pfSense/OPNsense, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\homelab-vlan-segmentation\SKILL.md` |
| `hookify-rules` | This skill should be used when the user asks to create a hookify rule, write a hook rule, configure hookify, a ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\hookify-rules\SKILL.md` |
| `ito-inference` | Inspect the availability of model serving on a completed Itô compute booking and, when the canonical backend b ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ito-inference\SKILL.md` |
| `ito-training` | Run an ML training job on a completed Itô compute booking through the canonical Itô backend. Use after ito-com ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ito-training\SKILL.md` |
| `java-coding-standards` | Java coding standards for Spring Boot and Quarkus services: naming, immutability, Optional usage, streams, exc ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\java-coding-standards\SKILL.md` |
| `jpa-patterns` | JPA/Hibernate patterns for entity design, relationships, query optimization, transactions, auditing, indexing, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\jpa-patterns\SKILL.md` |
| `kotlin-coroutines-flows` | Kotlin Coroutines and Flow patterns for Android and KMP — structured concurrency, Flow operators, StateFlow, e ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\kotlin-coroutines-flows\SKILL.md` |
| `kotlin-exposed-patterns` | JetBrains Exposed ORM patterns including DSL queries, DAO pattern, transactions, HikariCP connection pooling, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\kotlin-exposed-patterns\SKILL.md` |
| `kotlin-ktor-patterns` | Ktor server patterns including routing DSL, plugins, authentication, Koin DI, kotlinx.serialization, WebSocket ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\kotlin-ktor-patterns\SKILL.md` |
| `kotlin-patterns` | Idiomatic Kotlin patterns, best practices, and conventions for building robust, efficient, and maintainable Ko ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\kotlin-patterns\SKILL.md` |
| `kubernetes-patterns` | Kubernetes workload patterns, resource management, RBAC, probes, autoscaling, ConfigMap/Secret handling, and k ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\kubernetes-patterns\SKILL.md` |
| `laravel-patterns` | Laravel architecture patterns, routing/controllers, Eloquent ORM, service layers, queues, events, caching, and ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\laravel-patterns\SKILL.md` |
| `laravel-plugin-discovery` | Discover and evaluate Laravel packages via LaraPlugins.io MCP. Use when the user wants to find plugins, check ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\laravel-plugin-discovery\SKILL.md` |
| `logistics-exception-management` | > / Codified expertise for handling freight exceptions, shipment delays, / damages, losses, and carrier disput ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\logistics-exception-management\SKILL.md` |
| `mcp-server-patterns` | Build MCP servers with Node/TypeScript SDK — tools, resources, prompts, Zod validation, stdio vs Streamable HT ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\mcp-server-patterns\SKILL.md` |
| `motion-advanced` | Advanced motion patterns for React / Next.js — drag & drop, gestures, text animations, SVG path drawing, custo ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\motion-advanced\SKILL.md` |
| `motion-foundations` | Motion tokens, spring presets, performance rules, device adaptation, accessibility enforcement, and SSR safety ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\motion-foundations\SKILL.md` |
| `motion-patterns` | Production-ready animation patterns for React / Next.js — button, modal, toast, stagger, page transitions, exi ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\motion-patterns\SKILL.md` |
| `mysql-patterns` | MySQL and MariaDB schema, query, indexing, transaction, replication, and connection-pool patterns for producti ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\mysql-patterns\SKILL.md` |
| `nestjs-patterns` | NestJS architecture patterns for modules, controllers, providers, DTO validation, guards, interceptors, config ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\nestjs-patterns\SKILL.md` |
| `netmiko-ssh-automation` | Safe Python Netmiko patterns for read-only collection, bounded batch SSH, TextFSM parsing, guarded config chan ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\netmiko-ssh-automation\SKILL.md` |
| `nextjs-turbopack` | Next.js 16+ and Turbopack — incremental bundling, FS caching, dev speed, and when to use Turbopack vs webpack. | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\nextjs-turbopack\SKILL.md` |
| `nodejs-keccak256` | Prevent Ethereum hashing bugs in JavaScript and TypeScript. Node's sha3-256 is NIST SHA3, not Ethereum Keccak- ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\nodejs-keccak256\SKILL.md` |
| `nuxt4-patterns` | Nuxt 4 app patterns for hydration safety, performance, route rules, lazy loading, and SSR-safe data fetching w ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\nuxt4-patterns\SKILL.md` |
| `perl-patterns` | Modern Perl 5.36+ idioms, best practices, and conventions for building robust, maintainable Perl applications. | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\perl-patterns\SKILL.md` |
| `postgres-patterns` | PostgreSQL database patterns for query optimization, schema design, indexing, and security. Based on Supabase ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\postgres-patterns\SKILL.md` |
| `prisma-patterns` | Prisma ORM patterns for TypeScript backends — schema design, query optimization, transactions, pagination, and ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\prisma-patterns\SKILL.md` |
| `production-scheduling` | > / Codified expertise for production scheduling, job sequencing, line balancing, / changeover optimization, a ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\production-scheduling\SKILL.md` |
| `python-patterns` | Pythonic idioms, PEP 8 standards, type hints, and best practices for building robust, efficient, and maintaina ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\python-patterns\SKILL.md` |
| `pytorch-patterns` | PyTorch deep learning patterns and best practices for building robust, efficient, and reproducible training pi ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\pytorch-patterns\SKILL.md` |
| `quarkus-patterns` | Quarkus 3.x LTS architecture patterns with Camel for messaging, RESTful API design, CDI services, data access ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\quarkus-patterns\SKILL.md` |
| `react-native-patterns` | React Native and Expo app patterns — Expo Router navigation, state separation (server/client/route/form), TanS ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\react-native-patterns\SKILL.md` |
| `react-patterns` | React 18/19 patterns including hooks discipline, server/client component boundaries, Suspense + error boundari ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\react-patterns\SKILL.md` |
| `react-performance` | React and Next.js performance optimization patterns adapted from Vercel Engineering's React Best Practices (ht ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\react-performance\SKILL.md` |
| `redis-patterns` | Redis data structure patterns, caching strategies, distributed locks, rate limiting, pub/sub, and connection m ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\redis-patterns\SKILL.md` |
| `rust-patterns` | Idiomatic Rust patterns, ownership, error handling, traits, concurrency, and best practices for building safe, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\rust-patterns\SKILL.md` |
| `springboot-patterns` | Spring Boot architecture patterns, REST API design, layered services, data access, caching, async processing, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\springboot-patterns\SKILL.md` |
| `swift-actor-persistence` | Thread-safe data persistence in Swift using actors — in-memory cache with file-backed storage, eliminating dat ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\swift-actor-persistence\SKILL.md` |
| `swift-concurrency-6-2` | Swift 6.2 Approachable Concurrency — single-threaded by default, @concurrent for explicit background offloadin ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\swift-concurrency-6-2\SKILL.md` |
| `swiftui-patterns` | SwiftUI architecture patterns, state management with @Observable, view composition, navigation, performance op ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\swiftui-patterns\SKILL.md` |
| `tinystruct-patterns` | Expert guidance for developing with the tinystruct Java framework. Use when working on the tinystruct codebase ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\tinystruct-patterns\SKILL.md` |
| `ui-to-vue` | Use when the user has UI screenshots or design exports that need batch conversion into Vue 3 components, espec ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ui-to-vue\SKILL.md` |
| `vite-patterns` | Vite build tool patterns including config, plugins, HMR, env variables, proxy setup, SSR, library mode, depend ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\vite-patterns\SKILL.md` |
| `vue-patterns` | Vue.js 3 Composition API patterns, component architecture, reactivity best practices, Pinia state management, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\vue-patterns\SKILL.md` |

### ecc - Other / general engineering (2)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `regex-vs-llm-structured-text` | Decision framework for choosing between regex and LLM when parsing structured text — start with regex, add LLM ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\regex-vs-llm-structured-text\SKILL.md` |
| `rules-distill` | Scan skills to extract cross-cutting principles and distill them into rules — append, revise, or create new ru ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\rules-distill\SKILL.md` |

### ecc - Platform & integrations (6)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `codehealth-mcp` | Real-time structural Code Health via CodeScene MCP — review before edits, verify score deltas after changes, g ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\codehealth-mcp\SKILL.md` |
| `contract-first` | Use when multiple consumers and providers must evolve an API or event schema without field drift, integration ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\contract-first\SKILL.md` |
| `hexagonal-architecture` | Design, implement, and refactor Ports & Adapters systems with clear domain boundaries, dependency inversion, a ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\hexagonal-architecture\SKILL.md` |
| `jira-integration` | Use this skill when retrieving Jira tickets, analyzing requirements, updating ticket status, adding comments, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\jira-integration\SKILL.md` |
| `mailtrap-email-integration` | Guides agents through integrating transactional email sending via Mailtrap's Email API, including sandbox test ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\mailtrap-email-integration\SKILL.md` |
| `x-api` | X/Twitter API integration for posting tweets, threads, reading timelines, search, and analytics. Covers OAuth ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\x-api\SKILL.md` |

### ecc - Research & analysis (10)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `competitive-platform-analysis` | >- / Use when scoping a competitive landscape — identifying, categorising, and / score-filtering a competitor ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\competitive-platform-analysis\SKILL.md` |
| `competitive-report-structure` | >- / Use after benchmark-methodology has produced scored competitor profile cards. / Assembles findings into a ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\competitive-report-structure\SKILL.md` |
| `deep-research` | Multi-source deep research using firecrawl and exa MCPs. Searches the web, synthesizes findings, and delivers ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\deep-research\SKILL.md` |
| `investor-materials` | Create and update pitch decks, one-pagers, investor memos, accelerator applications, financial models, and fun ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\investor-materials\SKILL.md` |
| `investor-outreach` | Draft cold emails, warm intro blurbs, follow-ups, update emails, and investor communications for fundraising. ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\investor-outreach\SKILL.md` |
| `ito-market-intelligence` | Research prediction-market events, venues, underliers, liquidity, and news context for Itô basket workflows. U ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ito-market-intelligence\SKILL.md` |
| `market-research` | Conduct market research, competitive analysis, investor due diligence, and industry intelligence with source a ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\market-research\SKILL.md` |
| `marketing-campaign` | End-to-end marketing campaign planning and execution. Covers audience research, positioning, campaign angle de ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\marketing-campaign\SKILL.md` |
| `prediction-market-oracle-research` | Research prediction markets as data sources or oracle signals for products, agents, dashboards, and corporate ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\prediction-market-oracle-research\SKILL.md` |
| `prediction-market-risk-review` | Review prediction-market, basket, oracle, and trading-agent workflows for compliance, safety, data-quality, pr ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\prediction-market-risk-review\SKILL.md` |

### ecc - Security & compliance (24)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `automation-audit-ops` | Evidence-first automation inventory and overlap audit workflow for ECC. Use when the user wants to know which ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\automation-audit-ops\SKILL.md` |
| `click-path-audit` | Trace every user-facing button/touchpoint through its full state change sequence to find bugs where functions ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\click-path-audit\SKILL.md` |
| `config-gc` | Garbage collection for your Claude Code configuration. Periodically scans ~/.claude (skills, memory, hooks, pe ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\config-gc\SKILL.md` |
| `customs-trade-compliance` | > / Codified expertise for customs documentation, tariff classification, duty / optimization, restricted party ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\customs-trade-compliance\SKILL.md` |
| `defi-amm-security` | Security checklist for Solidity AMM contracts, liquidity pools, and swap flows. Covers reentrancy, CEI orderin ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\defi-amm-security\SKILL.md` |
| `delivery-gate` | Stop hook that blocks Claude from finishing until quality checks pass. Detects rationalization patterns (surfa ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\delivery-gate\SKILL.md` |
| `django-security` | Django security best practices, authentication, authorization, CSRF protection, SQL injection prevention, XSS ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\django-security\SKILL.md` |
| `ecc-tools-cost-audit` | Evidence-first ECC Tools burn and billing audit workflow. Use when investigating runaway PR creation, quota by ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ecc-tools-cost-audit\SKILL.md` |
| `healthcare-phi-compliance` | Protected Health Information (PHI) and Personally Identifiable Information (PII) compliance patterns for healt ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\healthcare-phi-compliance\SKILL.md` |
| `hipaa-compliance` | HIPAA-specific entrypoint for healthcare privacy and security work. Use when a task is explicitly framed aroun ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\hipaa-compliance\SKILL.md` |
| `ito-compute` | Query live GPU inventory, submit an authenticated Itô fixed-rate RFQ, inspect RFQ or procurement status, revok ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ito-compute\SKILL.md` |
| `laravel-security` | Laravel security best practices — authentication, authorization, Eloquent safety, CSRF, XSS prevention, API se ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\laravel-security\SKILL.md` |
| `perl-security` | Comprehensive Perl security covering taint mode, input validation, safe process execution, DBI parameterized q ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\perl-security\SKILL.md` |
| `production-audit` | Local-evidence production readiness audit for shipped apps, pre-launch reviews, post-merge checks, and "what b ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\production-audit\SKILL.md` |
| `quality-nonconformance` | > / Codified expertise for quality control, non-conformance investigation, root / cause analysis, corrective a ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\quality-nonconformance\SKILL.md` |
| `quarkus-security` | Quarkus Security best practices for authentication, authorization, JWT/OIDC, RBAC, input validation, CSRF, sec ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\quarkus-security\SKILL.md` |
| `repo-scan` | Cross-stack source code asset audit — classifies every file, detects embedded third-party libraries, and deliv ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\repo-scan\SKILL.md` |
| `returns-reverse-logistics` | > / Codified expertise for returns authorization, receipt and inspection, / disposition decisions, refund proc ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\returns-reverse-logistics\SKILL.md` |
| `security-bounty-hunter` | Hunt for exploitable, bounty-worthy security issues in repositories. Focuses on remotely reachable vulnerabili ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\security-bounty-hunter\SKILL.md` |
| `security-review` | Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\security-review\SKILL.md` |
| `security-scan` | Scan your Claude Code configuration (.claude/ directory) for security vulnerabilities, misconfigurations, and ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\security-scan\SKILL.md` |
| `seo` | Audit, plan, and implement SEO improvements across technical SEO, on-page optimization, structured data, Core ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\seo\SKILL.md` |
| `springboot-security` | Spring Security best practices for authn/authz, validation, CSRF, secrets, headers, rate limiting, and depende ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\springboot-security\SKILL.md` |
| `workspace-surface-audit` | Audit the active repo, MCP servers, plugins, connectors, env surfaces, and harness setup, then recommend the h ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\workspace-surface-audit\SKILL.md` |

### ecc - Testing & QA (31)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `ai-regression-testing` | Regression testing strategies for AI-assisted development. Sandbox-mode API testing without database dependenc ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ai-regression-testing\SKILL.md` |
| `benchmark` | Use this skill to measure performance baselines, detect regressions before/after PRs, and compare stack altern ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\benchmark\SKILL.md` |
| `benchmark-methodology` | >- / Use after competitive-platform-analysis has produced a tiered competitor set. / Scores each competitor ac ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\benchmark-methodology\SKILL.md` |
| `browser-qa` | Use this skill to automate visual testing and UI interaction verification using browser automation after deplo ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\browser-qa\SKILL.md` |
| `carrier-relationship-management` | > / Codified expertise for managing carrier portfolios, negotiating freight rates, / tracking carrier performa ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\carrier-relationship-management\SKILL.md` |
| `cpp-testing` | Use only when writing/updating/fixing C++ tests, configuring GoogleTest/CTest, diagnosing failing or flaky tes ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\cpp-testing\SKILL.md` |
| `csharp-testing` | C# and .NET testing patterns with xUnit, FluentAssertions, mocking, integration tests, and test organization b ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\csharp-testing\SKILL.md` |
| `django-tdd` | Django testing strategies with pytest-django, TDD methodology, factory_boy, mocking, coverage, and testing Dja ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\django-tdd\SKILL.md` |
| `django-verification` | Verification loop for Django projects: migrations, linting, tests with coverage, security scans, and deploymen ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\django-verification\SKILL.md` |
| `e2e-testing` | Playwright E2E testing patterns, Page Object Model, configuration, CI/CD integration, artifact management, and ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\e2e-testing\SKILL.md` |
| `energy-procurement` | > / Codified expertise for electricity and gas procurement, tariff optimization, / demand charge management, r ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\energy-procurement\SKILL.md` |
| `fsharp-testing` | F# testing patterns with xUnit, FsUnit, Unquote, FsCheck property-based testing, integration tests, and test o ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\fsharp-testing\SKILL.md` |
| `golang-testing` | Go testing patterns including table-driven tests, subtests, benchmarks, fuzzing, and test coverage. Follows TD ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\golang-testing\SKILL.md` |
| `iterative-retrieval` | Pattern for progressively refining context retrieval to solve the subagent context problem | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\iterative-retrieval\SKILL.md` |
| `kotlin-testing` | Kotlin testing patterns with Kotest, MockK, coroutine testing, property-based testing, and Kover coverage. Fol ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\kotlin-testing\SKILL.md` |
| `laravel-tdd` | Laravel testing strategies with PHPUnit, Pest, model factories, HTTP tests, Sanctum authentication testing, mo ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\laravel-tdd\SKILL.md` |
| `laravel-verification` | Verification loop for Laravel projects: env checks, linting, static analysis, tests with coverage, security sc ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\laravel-verification\SKILL.md` |
| `mle-workflow` | Production machine-learning engineering workflow for data contracts, reproducible training, model evaluation, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\mle-workflow\SKILL.md` |
| `perl-testing` | Perl testing patterns using Test2::V0, Test::More, prove runner, mocking, coverage with Devel::Cover, and TDD ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\perl-testing\SKILL.md` |
| `product-lens` | Use this skill to validate the "why" before building, run product diagnostics, and pressure-test product direc ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\product-lens\SKILL.md` |
| `python-testing` | Python testing strategies using pytest, TDD methodology, fixtures, mocking, parametrization, and coverage requ ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\python-testing\SKILL.md` |
| `quarkus-tdd` | Test-driven development for Quarkus 3.x LTS using JUnit 5, Mockito, REST Assured, Camel testing, and JaCoCo. U ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\quarkus-tdd\SKILL.md` |
| `quarkus-verification` | Verification loop for Quarkus projects: build, static analysis, tests with coverage, security scans, native co ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\quarkus-verification\SKILL.md` |
| `react-testing` | React component testing with React Testing Library, Vitest/Jest, MSW for network mocking, accessibility assert ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\react-testing\SKILL.md` |
| `rust-testing` | Rust testing patterns including unit tests, integration tests, async testing, property-based testing, mocking, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\rust-testing\SKILL.md` |
| `scholar-evaluation` | Structured scholarly-work evaluation for papers, proposals, literature reviews, methods sections, evidence qua ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\scientific-thinking-scholar-evaluation\SKILL.md` |
| `springboot-tdd` | Test-driven development for Spring Boot using JUnit 5, Mockito, MockMvc, Testcontainers, and JaCoCo. Use when ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\springboot-tdd\SKILL.md` |
| `springboot-verification` | Verification loop for Spring Boot projects: build, static analysis, tests with coverage, security scans, and d ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\springboot-verification\SKILL.md` |
| `swift-protocol-di-testing` | Protocol-based dependency injection for testable Swift code — mock file system, network, and external APIs usi ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\swift-protocol-di-testing\SKILL.md` |
| `tdd-workflow` | Use this skill when writing new features, fixing bugs, or refactoring code. Enforces test-driven development w ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\tdd-workflow\SKILL.md` |
| `windows-desktop-e2e` | E2E testing for Windows native desktop apps (WPF, WinForms, Win32/MFC, Qt) using pywinauto and Windows UI Auto ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\windows-desktop-e2e\SKILL.md` |

### ecc - Workflow, context & memory (19)

| Skill | One-line purpose | Source `SKILL.md` |
|-------|------------------|-------------------|
| `architecture-decision-records` | Capture architectural decisions made during Claude Code sessions as structured ADRs. Auto-detects decision mom ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\architecture-decision-records\SKILL.md` |
| `blueprint` | >- / Turn a one-line objective into a step-by-step construction plan for / multi-session, multi-agent engineer ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\blueprint\SKILL.md` |
| `context-budget` | Audits Claude Code context window consumption across agents, skills, MCP servers, and rules. Identifies bloat, ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\context-budget\SKILL.md` |
| `continuous-learning` | [DEPRECATED - use continuous-learning-v2] Legacy v1 stop-hook skill extractor. v2 is a strict superset with in ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\continuous-learning\SKILL.md` |
| `cost-tracking` | Track and report Claude Code token usage, spending, and budgets from the local ECC cost-tracker metrics log. U ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\cost-tracking\SKILL.md` |
| `evm-token-decimals` | Prevent silent decimal mismatch bugs across EVM chains. Covers runtime decimal lookup, chain-aware caching, br ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\evm-token-decimals\SKILL.md` |
| `exa-search` | Neural search via Exa MCP for web, code, and company research. Use when the user needs web search, code exampl ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\exa-search\SKILL.md` |
| `git-workflow` | Git workflow patterns including branching strategies, commit conventions, merge vs rebase, conflict resolution ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\git-workflow\SKILL.md` |
| `inventory-demand-planning` | > / Codified expertise for demand forecasting, safety stock optimization, / replenishment planning, and promot ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\inventory-demand-planning\SKILL.md` |
| `ito-trade-planner` | Build a non-advisory prediction-market trade planning worksheet for Itô or venue workflows. Use to inspect ven ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\ito-trade-planner\SKILL.md` |
| `literature-review` | Systematic literature-review workflow for academic, biomedical, technical, and scientific topics, including se ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\scientific-thinking-literature-review\SKILL.md` |
| `plan-canvas` | Open plans and HTML artifacts in a local browser canvas where the human annotates elements, chats, and approve ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\plan-canvas\SKILL.md` |
| `plankton-code-quality` | Write-time code quality enforcement using Plankton — auto-formatting, linting, and Claude-powered fixes on eve ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\plankton-code-quality\SKILL.md` |
| `product-capability` | Translate PRD intent, roadmap asks, or product discussions into an implementation-ready capability plan that e ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\product-capability\SKILL.md` |
| `search-first` | Research-before-coding workflow. Search for existing tools, libraries, and patterns before writing custom code ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\search-first\SKILL.md` |
| `strategic-compact` | Suggests manual context compaction at logical intervals to preserve context through task phases rather than ar ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\strategic-compact\SKILL.md` |
| `terminal-opener` | Open an executable and its argument array in a visible terminal window through a reusable, shell-free launch p ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\terminal-opener\SKILL.md` |
| `token-budget-advisor` | >- / Offers the user an informed choice about how much response depth to / consume before answering. Use this ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\token-budget-advisor\SKILL.md` |
| `unified-memory` | Share durable, inspectable context and handoffs between Claude, Codex, Hermes, Cursor, OpenCode, and other age ... | `C:\Users\tamar\.claude\plugins\cache\ecc\ecc\2.2.0\skills\unified-memory\SKILL.md` |

---

## 4. Command Reference

Two different things get typed with a leading slash in Claude Code. They are separated here.

### 4a. Real slash commands (`commands/*.md` files that Claude Code loads)

| Command | Owner | Purpose | Source file |
|---------|-------|---------|-------------|
| `/caveman:caveman-commit` | caveman | Generate terse caveman-style commit message | `C:\Users\tamar\.claude\plugins\cache\caveman\caveman\11ddc0c9813c\commands\caveman-commit.md` |
| `/caveman:caveman-init` | caveman | Drop the always-on caveman activation rule into the current repo for every IDE agent | `C:\Users\tamar\.claude\plugins\cache\caveman\caveman\11ddc0c9813c\commands\caveman-init.md` |
| `/caveman:caveman-review` | caveman | One-line code review comments | `C:\Users\tamar\.claude\plugins\cache\caveman\caveman\11ddc0c9813c\commands\caveman-review.md` |
| `/caveman:caveman-stats` | caveman | Real session token usage + lifetime savings + USD. Tweetable line via --share. | `C:\Users\tamar\.claude\plugins\cache\caveman\caveman\11ddc0c9813c\commands\caveman-stats.md` |
| `/caveman:caveman` | caveman | Switch caveman intensity level (lite/full/ultra/wenyan) | `C:\Users\tamar\.claude\plugins\cache\caveman\caveman\11ddc0c9813c\commands\caveman.md` |
| `/claude-for-msft-365-install:access-policies` | claude-for-msft-365-install | Build the access_policies value — the granular, IAM-shaped way to allow or deny add-in features | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\claude-for-msft-365-install\commands\access-policies.md` |
| `/claude-for-msft-365-install:bootstrap` | claude-for-msft-365-install | Build the bootstrap endpoint — per-user MCP servers, skills, dynamic config | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\claude-for-msft-365-install\commands\bootstrap.md` |
| `/claude-for-msft-365-install:consent` | claude-for-msft-365-install | Azure admin consent URLs — one-time tenant approval for Entra SSO and Outlook Graph access | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\claude-for-msft-365-install\commands\consent.md` |
| `/claude-for-msft-365-install:debug` | claude-for-msft-365-install | Diagnose deployment issues (stale config, connect failures, missing add-in) | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\claude-for-msft-365-install\commands\debug.md` |
| `/claude-for-msft-365-install:entra-app` | claude-for-msft-365-install | (no description in frontmatter) | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\claude-for-msft-365-install\commands\entra-app.md` |
| `/claude-for-msft-365-install:export-data` | claude-for-msft-365-install | Export a copy of a user's add-in chat history, skills, MCP registrations, and settings before a machine is reb ... | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\claude-for-msft-365-install\commands\export-data.md` |
| `/claude-for-msft-365-install:manifest` | claude-for-msft-365-install | Generate the add-in manifest XML with your cloud config baked in | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\claude-for-msft-365-install\commands\manifest.md` |
| `/claude-for-msft-365-install:setup` | claude-for-msft-365-install | Setup wizard — provision Vertex/Bedrock/Foundry/gateway, admin consent, generate manifest(s) | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\claude-for-msft-365-install\commands\setup.md` |
| `/claude-for-msft-365-install:update-user-attrs` | claude-for-msft-365-install | Set per-user config (tokens, region overrides) via Azure AD extension attributes | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\claude-for-msft-365-install\commands\update-user-attrs.md` |
| `/financial-analysis:3-statement-model` | financial-analysis | Fill out a 3-statement financial model template | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\commands\3-statement-model.md` |
| `/financial-analysis:competitive-analysis` | financial-analysis | Create a competitive landscape analysis | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\commands\competitive-analysis.md` |
| `/financial-analysis:comps` | financial-analysis | Build a comparable company analysis with trading multiples | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\commands\comps.md` |
| `/financial-analysis:dcf` | financial-analysis | Build a DCF valuation model with comps-informed terminal multiples | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\commands\dcf.md` |
| `/financial-analysis:debug-model` | financial-analysis | Debug and audit a financial model for errors | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\commands\debug-model.md` |
| `/financial-analysis:lbo` | financial-analysis | Build an LBO model for a PE acquisition | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\commands\lbo.md` |
| `/financial-analysis:ppt-template` | financial-analysis | Create a reusable PPT template skill from a PowerPoint template file | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\financial-analysis\commands\ppt-template.md` |
| `/investment-banking:buyer-list` | investment-banking | Build a buyer universe for a sell-side process | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\commands\buyer-list.md` |
| `/investment-banking:cim` | investment-banking | Draft a Confidential Information Memorandum | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\commands\cim.md` |
| `/investment-banking:deal-tracker` | investment-banking | Track and review live deal pipeline | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\commands\deal-tracker.md` |
| `/investment-banking:merger-model` | investment-banking | Build an accretion/dilution merger model | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\commands\merger-model.md` |
| `/investment-banking:one-pager` | investment-banking | Create a one-page company strip profile using branded PPT template | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\commands\one-pager.md` |
| `/investment-banking:process-letter` | investment-banking | Draft a process letter or bid instructions | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\commands\process-letter.md` |
| `/investment-banking:teaser` | investment-banking | Draft an anonymous one-page teaser | `C:\Users\tamar\.claude\plugins\synced\a0c24174-d71f-4bfc-885d-ff5cbe3c3b7d_2942d01a-c053-461c-9cc1-49fa330aeb71\investment-banking\commands\teaser.md` |

That is **28** verified command files. Namespacing follows the plugin name; if a command name is unambiguous the bare form (for example `/caveman`) also resolves.

### 4b. Command files on disk that are NOT loaded as Claude Code slash commands

| Files | Why not loaded |
|-------|----------------|
| `ponytail`: 6 x `commands/*.toml` (`ponytail`, `ponytail-audit`, `ponytail-debt`, `ponytail-gain`, `ponytail-help`, `ponytail-review`) | TOML command format used by other harnesses (OpenCode / Codex). Claude Code loads `commands/*.md` only. The same behaviour is reachable through the plugin's six skills. |
| `ecc`: 12 x `legacy-command-shims/commands/*.md` (`agent-sort`, `claw`, `context-budget`, `devfleet`, `docs`, `e2e`, `eval`, `orchestrate`, `prompt-optimize`, `rules-distill`, `tdd`, `verify`) | Outside the plugin's registered `commands/` path. The files themselves state they are legacy shims and that the skill should be preferred. |
| `ecc`: 3 x `.claude/commands/*.md` (`add-language-rules`, `database-migration`, `feature-development`) | Repo-internal `.claude/` directory inside the plugin source, not the plugin's registered command path. |

`ecc` ships **no** `commands/` directory at its plugin root, so despite 284 skills it contributes **zero** real slash commands. `claude-mem` and `ui-ux-pro-max` likewise ship no command files.

### 4c. Skill invocations (a naming convention, not command files)

A skill is invoked as `/<plugin>:<skill-name>` - for example `/caveman:caveman`, `/ponytail:ponytail`, `/ecc:tdd-workflow`, `/claude-mem:mem-search`, `/ui-ux-pro-max:design`, `/financial-analysis:dcf-model`. These are **not** command files; they are the skill-invocation convention, and every one of the 372 skills in section 2 is reachable this way. Personal synced skills (`docs`, `docx`, `google-workspace`, `import-memory`, `morning`, `pdf`, `pptx`, `skill-creator`, `xlsx`) carry no plugin namespace and are normally model-invoked by name.

Mode arguments documented inside skills - for example `/caveman lite|full|ultra|wenyan` and `/ponytail lite|full|ultra` - are argument conventions of those skills. For caveman the argument is backed by a real command file (`caveman.md`, `argument-hint: [lite|full|ultra|wenyan]`); for ponytail it is backed only by the skill text, since its command files are TOML.

---

## 5. Overlaps and Relationships

### Exact name collisions across bundles

| Skill name | Appears in | Which to prefer |
|------------|-----------|-----------------|
| `competitive-analysis` | Synced plugin: financial-analysis, Synced plugin: market-researcher | The `financial-analysis` copy is valuation-oriented; the `market-researcher` copy feeds a sector research note. |
| `comps-analysis` | Synced plugin: financial-analysis, Synced plugin: market-researcher | The same trading-comps routine vendored into both finance bundles. |
| `design-system` | Plugin: ecc, Plugin: ui-ux-pro-max | The `ui-ux-pro-max` version is backed by its local style/palette/typography database; the `ecc` version is an audit and PR-review checklist for design-token changes. |
| `pptx-author` | Synced plugin: financial-analysis, Synced plugin: market-researcher, Synced plugin: meeting-prep-agent | Vendored into three synced finance bundles. Same role (author PowerPoint decks); pick the copy whose plugin owns the surrounding workflow. |
| `skill-creator` | Personal (synced), Synced plugin: financial-analysis | The personal Anthropic-managed copy is the general-purpose one; the `financial-analysis` copy is scoped to that plugin's conventions. |

### Functional overlaps worth knowing

- **`caveman` vs `ponytail`** - complementary, not competing. `caveman` compresses *prose output*; `ponytail` constrains *what gets built* (YAGNI, stdlib first, shortest working diff). Both are active in this environment via SessionStart hooks and are designed to be paired.
- **Memory: `claude-mem` (19 skills) vs `ecc:unified-memory` vs `ecc:strategic-compact` vs personal `import-memory`** - `claude-mem` is a full persistence system with its own hooks, SQLite store and MCP search tools; prefer it for cross-session recall, since its hooks are already installed here. `ecc:unified-memory` targets sharing context across *different* harnesses (Codex, Cursor, OpenCode). `ecc:strategic-compact` only decides *when* to compact. `import-memory` is a one-off import of external memory data.
- **Design and UI: `ui-ux-pro-max` (7 skills) vs ECC's frontend/design skills (~26)** - `ui-ux-pro-max` is data-backed (84 styles, 192 palettes, 74 font pairings, 25 chart types, 22 stacks) and is the better default for concrete visual decisions. ECC's design skills are review- and direction-oriented (`design-system` audit, `frontend-design-direction`, `liquid-glass-design`).
- **Document authoring: personal `docx`/`pptx`/`xlsx`/`pdf`/`docs` vs the finance bundles' `pptx-author`/`xlsx-author`** - the personal Anthropic-managed skills are the general-purpose file engines. The `*-author` skills wrap them with domain templates and house style; use those only inside their own workflow.
- **Research: `ecc:deep-research` vs `ecc:research-ops` vs `ecc:market-research` vs `ecc:literature-review` vs the synced `market-researcher` bundle** - `deep-research` needs the firecrawl and exa MCP servers; `research-ops` is an evidence-first current-state workflow; `literature-review` is academic and biomedical; `market-researcher` produces a packaged sector note with comps and slides. Choose by deliverable, not by topic.
- **Testing: `ecc:tdd-workflow` vs `ecc:verification-loop` vs `ecc:e2e-testing` vs the per-language `*-testing` skills** - `tdd-workflow` drives feature work red-green-refactor; `verification-loop` is the post-change check; `e2e-testing` is browser and flow level; the per-language skills carry idiom and tooling for one stack. They stack rather than replace each other.
- **Review: `caveman:caveman-review` vs `ecc:security-review` and ECC's per-language review skills** - `caveman-review` only changes the *format* of review output (one line per finding). The ECC review skills carry the actual checklists. They can be combined.
- **Python work in this project** - for `D:\MultimodalRAG` (a Python project), the directly relevant skills are `ecc:python-patterns`, `ecc:python-testing`, `ecc:pytorch-patterns`, `ecc:mle-workflow`, `ecc:tdd-workflow` and `ecc:verification-loop`. No project-level skill overrides them, so the plugin versions apply unchanged.
- **Finance bundles form one family** - modelling (`financial-analysis`), sell-side deal execution (`investment-banking`), fund accounting (`fund-admin`), sector research (`market-researcher`), client meetings (`meeting-prep-agent`), KYC (`operations`). Several depend on MCP servers (`capiq`, `factset`, `crm`) that are not authenticated in this session.

---

## 6. Discovery Limitations

What this audit did not, or could not, cover:

1. **No project-level skills exist.** `D:\MultimodalRAG\.claude` does not exist at all, so there are no project-scoped skills or commands. The project is a Python project and is not a git repository.
2. **`C:\Users\tamar\.claude\skills\learned\` is empty.** The directory exists but holds no skill, so nothing was extracted from it.
3. **Skills were read from the plugin *cache*, not from live marketplaces.** Every path here is the installed copy under `~/.claude/plugins/cache/...`. If a marketplace has since published a newer version, that difference is not visible. Versions recorded: caveman `11ddc0c9813c`, ponytail `4.9.0`, claude-mem `13.14.0`, ui-ux-pro-max `2.13.0`, ecc `2.2.0`.
4. **Three registered marketplaces have no installed plugin** (`dev-skills`, `watermarks-remover`, `academic-research-skills`). Their marketplace manifests are on disk, but no plugin from them appears in `installed_plugins.json` or `enabledPlugins`, so their skills are absent from this inventory by fact rather than by omission.
5. **Non-Claude-Code skill copies were deliberately excluded.** The `ecc` repository also vendors skill sets for other harnesses under `.agents/skills/`, `.cursor/skills/`, `.kiro/skills/`, `.codex/` and `.opencode/`, plus translated copies under `docs/es/skills/` and `docs/ja-JP/skills/`. Those are not loaded by Claude Code and would have inflated the count by several hundred duplicates. Likewise `caveman` vendors a nested copy under `plugins/caveman/skills/` (4 files), and `ui-ux-pro-max` ships an installer payload under `cli/assets/skills/` that is byte-identical to its registered copies. Only registered roots are counted.
6. **Per-skill detail is frontmatter plus section headings, not full body text.** Purpose, trigger, declared tools, bundled resources and the procedure outline were extracted from each file; the body prose was not reproduced. The exact path is given for every skill.
7. **Activation was not tested.** This audit confirms that each skill exists and is readable at a registered path. It does not prove the skill runs: several declare external dependencies (MCP servers such as `capiq`, `factset`, `crm`, `firecrawl`, `exa`; CLI tools; API keys) that are unavailable or unauthenticated here.
8. **MCP-dependent skills are degraded in this session.** The claude.ai connectors (Asana, Atlassian, Box, Canva, Figma, Gmail, Google Calendar, Google Drive, HubSpot, Intercom, Linear, Microsoft 365, Notion, monday.com) need authorization that cannot be completed in a non-interactive session, so skills routing through them - notably `google-workspace` and the finance bundles - cannot be exercised.
9. **No live skill-menu cross-check.** The inventory is built from the filesystem plus `settings.json` and `installed_plugins.json`. It was not diffed against the running session's own skill menu, so a skill that Claude Code loads but hides from the menu, or vice versa, would not surface as a discrepancy here.
10. **Enablement of the synced bundles is inferred, not read from a config flag.** The seven bundles under `~/.claude/plugins/synced/` carry `.in_use` markers and two expose agents in this session; no per-bundle enable flag was found in `settings.json`.
11. **Nothing was modified.** No skill was installed, renamed, edited or removed during this audit. All access was read-only.

