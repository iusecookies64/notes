# Note Writing & Skeleton Index Guidelines

Follow these formatting and writing standards strictly when creating study notes or active-recall indexes, alongside `Agents/GeneralGuidelines.md`.

---

## 1. Note Writing Guidelines

### 1.1 Scope & Theoretical Rigor
- **Complete Coverage:** Cover all theory in the source material—every definition, theorem (with proof if present), corollary, and remark.
- **Source-Bound:** Only include concepts, definitions, theorems, and proofs from the provided source. Do not import external facts unless asked, though conversational phrasing, motivating questions, and intuitive explanations are encouraged.
- **New Notes (Initial Generation):**
  - Focus **100% on theory and principles**.
  - **Exclude** in-text numerical examples, practice problems, and arithmetic exercises unless asked otherwise.
  - Selected problems added later must be preserved and indexed.
- **Updating / Refactoring Existing Notes:**
  - **Preserve All Content:** Keep all existing theory, in-text examples, curated problems, and images. Never drop previously included examples or problems.
  - **Standardize Examples:** Wrap worked example prompts in `> [!example] Example: [Relevant Title]` callouts, with `**Solution:**` in regular text directly below (ending with `$\blacksquare$`).
  - **Standardize Problems:** Wrap curated exercise prompts in self-contained `> [!abstract] Problem Statement` callouts (expanding shared stems if needed), with `**Solution:**` in regular text below.
  - **Fix Formatting:** Repair skipped heading levels, legacy callout tags (e.g., `[!info] Definition` $\to$ `[!abstract] Definition: ...`, `[!abstract] Theorem` $\to$ `[!theorem] ...`), broken LaTeX delimiters, and misplaced subsections.
- **Sync Skeleton Index:** Always add or update the `# Skeleton Index` at the end of the file whenever notes are created or modified.

### 1.2 Conversational Style & Flow
- **Tutor-Like Voice:** Write in an engaging, 1-on-1 conversational style rather than dry, robotic, encyclopedia-style prose.
- **Motivate & Unpack:**
  - Lead into definitions and theorems with motivating context or questions (e.g., *"Why do we need this condition?"*).
  - Unpack formal definitions, equations, and theorems in plain language afterward (e.g., *"In other words, this guarantees that..."*).
- **Prose Over Bullet Dumps:** Default to connected paragraphs for explanations, intuition, and derivations. Reserve lists for discrete items (e.g., assumptions, cases, or component properties).

### 1.3 LaTeX & Math Formatting
1. **Inline Math (`$...$`):**
   - Use for all variables, symbols, constants, signals, bounds, and parameters (e.g., `$x$`, `$V_{DD}$`, `$t_{pd}$`, `$\mathbb{R}^n$`).
   - Do not put spaces inside the `$` delimiters (`$formula$`, never `$ formula $`). Never write naked math symbols in plain text.
2. **Display Math (`$$`):**
   - Opening and closing `$$` **must always be on their own lines** (never `$$formula$$`):
   ```markdown
   $$
   f(x) = \int_1^x \frac{1}{t} \, dt
   $$
   ```
3. **Multi-Step Derivations:**
   - Use `\begin{aligned} ... \end{aligned}` (or `align`) inside display math with `&` alignment and `\\` line breaks:
   ```markdown
   $$
   \begin{aligned}
   F &= \overline{(A + B) \cdot (C + D)} \\
     &= \overline{A + B} + \overline{C + D}
   \end{aligned}
   $$
   ```
4. **Display Math in Lists:** Indent the `$$` block to match the list item's indentation:
   ```markdown
   1. **Setup Time Constraint:**
      $$
      T_{c} \ge t_{pcq} + t_{pd} + t_{setup} + t_{skew}
      $$
   ```
5. **Display Math in Callouts:** Prefix every line with `>`:
   ```markdown
   > [!abstract] Definition: One-to-One Function
   > $$
   > f(x_1) \neq f(x_2) \quad \text{whenever } x_1 \neq x_2
   > $$
   ```

### 1.4 Headings & Section Dividers
- **Strict Heading Hierarchy (Never Skip Levels):**
  - `# X.Y Section Title` (H1) — major top-level sections (including `# Chapter X Additional Exercises` and `# Skeleton Index`).
  - `## Topic Name` (H2) — main subtopics (including `## X.Y Exercises`).
  - `### Concept Name` (H3) — specific subsections, sub-concepts, or proofs.
  - **Problem Headings:** Always place problem headings one level directly below their parent container:
    - Under H1 (`# Chapter X Additional Exercises`) $\to$ `## Problem XY: Title` (or `## Additional Problems` $\to$ `### Problem XY: Title`).
    - Under H2 (`## X.Y Exercises`) $\to$ `### Problem XY: Title`.
    - Under H3 (`### [Category]`) $\to$ `#### Problem XY: Title`.
- **Section Separators (`---`):** Use `---` **only** between major top-level `#` (H1) sections. Never use `---` within a section.

### 1.5 Obsidian Callouts & Proofs
Use callouts as visual anchors for formal blocks while keeping surrounding explanations in regular prose:
- `> [!abstract] Definition: [Term]` — formal definitions and axioms.
- `> [!theorem] [Theorem / Law Name]` — theorems, laws, lemmas, and corollaries.
- `> [!example] Example: [Relevant Title]` — worked in-text examples.
- `> [!abstract] Problem Statement` — curated problem/exercise prompts.
- `> [!warning] [Caution / Pitfall]` — common misconceptions or cautions.
- `> [!summary] [Summary]` — section or concept summaries.
- `> [!note] [Theoretical Remark]` — key conceptual remarks, intuitions, and trade-offs.
- **Proofs & Solutions:** Place directly **below** the callout in regular text (not inside a callout). Start with `**Proof:**` or `**Solution:**`, explain steps conversationally, and end with `$\blacksquare$`.

### 1.6 Figures, Diagrams & Tables
- **Contextual Placement:** Place images (`![](image_0.png)`) immediately next to the concept they illustrate; never batch images at the end.
- **Diagram Placeholders:** If a source figure is referenced without an image file, insert:
  ```markdown
  > [!figure] Figure Placeholder: Figure X.Y - [Brief description]
  ```
- **Tables:** Format OCR tables, truth tables, and state tables into clean Markdown tables.

### 1.7 Source Correction
- Fix OCR artifacts, broken line wraps, and garbled symbols.
- Correct speech-to-text errors in transcripts into proper domain terminology (e.g., "sea moss" $\to$ "CMOS", "key map" $\to$ "K-map", "t p d" $\to$ `$t_{pd}$`).

---

## 2. Skeleton Index Guidelines

The **Skeleton Index** at the end of a note acts like a closed-book exam: testing exhaustive active recall of every concept and problem without hints, formulas, or solutions.

### 2.1 Structure & Sequential Order
- **Strict 1:1 Chronological Order:** Mirror the exact top-to-bottom sequence of headings, subtopics, and problems in the notes. Never pool items into artificial buckets (e.g., no separate "All Definitions" or "All Theorems" sections).
- **Formatting Hierarchy:**
  - Precede with `---` and `# Skeleton Index` (H1).
  - `## [Section Number & Title]` (H2) for main sections.
  - `### [Subsection Title]` (H3) for subsections.
  - `**[Topic Title]**` for specific topics.
  - Bullet points (`- ...`) for active-recall prompts.
- **Exhaustive Coverage & LaTeX:** Cover every definition, theorem, derivation, mechanism, trade-off, and curated problem, following all LaTeX rules from **Section 1.3**.

### 2.2 Zero Spoilers (Exam Conditions)
1. **No Formulas or Values in Theory Prompts:** State *what* to recall or derive, never the formula, bound, or value itself (e.g., *"Derive the expression for [Metric]"* or *"State the bounds on [Parameter]"*).
2. **No Proof Hints:** Never reveal proof techniques, substitutions, or identities (e.g., *"Prove [Theorem] analytically and conceptually"*).
3. **No Leaked Conclusions:** Do not spoil outcomes in prompts (e.g., *"Analyze the effect of [X] on [Y]"* instead of *"Explain why [X] increases [Y]"*).
4. **No Solutions:** Exclude all answers, hints, parenthetical cues, and intermediate steps.

### 2.3 Curated Problems (Full Statements)
- Include every curated problem from the notes with its **complete, self-contained problem statement** (all premises, initial conditions, data, and questions to solve/prove).
- The reader should never have to memorize the question itself—only how to solve it. Exclude all hints, steps, and final answers.

### 2.4 Actionable Prompt Verbs
Phrase theoretical prompts as direct challenges using strong imperative verbs:
- *"Define..."*, *"State the necessary conditions for..."*, *"State and prove [Theorem]"*, *"Derive the governing equation for..."*, *"Explain the mechanism behind..."*, *"Compare [X] vs [Y] in terms of [Criteria]"*, *"Determine..."*, *"Evaluate and justify..."*.
