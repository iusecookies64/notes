# Note Writing & Skeleton Index Guidelines

This document provides instructions and formatting standards for CLI-based AI agents working within this repository. Follow these guidelines strictly when writing study notes or generating active-recall indexes, alongside the operating rules in `Agents/GeneralGuidelines.md`.

---

## 1. Note Writing Guidelines

These guidelines apply whenever creating or editing academic and technical study notes from textbooks, lecture slides, transcripts, or images.

### 1.1 Scope & Theoretical Rigor
- **Complete Coverage:** Cover all theory present in the material — every definition, theorem (with proof if present), corollary, and remark.
- **Theory-Only on Initial Note Generation:** When generating notes from source material, focus 100% on theory and principles. Exclude in-text numerical examples, practice problems, and arithmetic exercises unless explicitly instructed otherwise. *(Note: Selected problems from dedicated problem sets may be added to the notes later by the user or upon request; once present in the notes, they must be preserved and indexed in the Skeleton Index).*
- **Source-Bound Content:** Only include concepts, definitions, theorems, and proofs present in the provided material. Do not invent or import external facts from outside the source unless asked otherwise. However, you **are** encouraged to use natural conversational phrasing, motivating questions, and intuitive transitions to explain the source material clearly.
- **Sync Skeleton Index:** Always add or update the Skeleton Index at the end of the notes whenever note content (including newly added problems) is created or modified.

### 1.2 Conversational Style & Narrative Flow
- **Tutor-Like Voice:** Write the notes in an engaging, **conversational style**—as if explaining the concepts 1-on-1 to a peer or student. Avoid dry, robotic, or overly terse encyclopedia-style prose.
- **Motivate & Unpack:** Bridge formal theory with intuition:
  - Lead into definitions and theorems with motivating context or questions (e.g., *"Why do we need this condition?"*, *"Notice what happens if we relax this assumption..."*).
  - After stating a formal definition, equation, or theorem, unpack what it actually means in plain language (e.g., *"Let's break down what each term in this equation is doing..."*, *"In other words, this guarantees that..."*).
- **Flowing Prose Over Bullet Dumps:** Default to natural, connected paragraphs for explanations, physical/mathematical intuition, and derivations. Reserve bullet points and numbered lists for genuinely discrete items (e.g., enumerating assumptions, distinct cases, or component properties).

### 1.3 LaTeX & Math Formatting
Formatting must strictly follow these rules:

1. **Inline Math (`$ ... $`):**
   - Use for all individual variables, symbols, constants, logic levels, signals, bounds, and timing parameters (e.g., `$x$`, `$V_{DD}$`, `$t_{pd}$`, `$\mathbb{R}^n$`).
   - Write without spaces immediately inside the dollar signs (e.g., `$formula$`, never `$ formula $`).
   - Never write naked mathematical symbols or plaintext formulas without LaTeX delimiters.

2. **Display Math Delimiters (`$$`):**
   - The opening `$$` and closing `$$` **must always be on their own separate lines**.
   - **Never** place math content on the same line as the delimiters (e.g., avoid `$$formula$$`).
   ```markdown
   $$
   f(x) = \int_1^x \frac{1}{t} \, dt
   $$
   ```

3. **Multi-Step Derivations:**
   - Use `\begin{align} ... \end{align}` or `\begin{aligned} ... \end{aligned}` inside display math blocks, with `&` alignment and `\\` line breaks:
   ```markdown
   $$
   \begin{aligned}
   F &= \overline{(A + B) \cdot (C + D)} \\
     &= \overline{A + B} + \overline{C + D} \\
     &= (\overline{A} \cdot \overline{B}) + (\overline{C} \cdot \overline{D})
   \end{aligned}
   $$
   ```

4. **Display Math Inside Lists:**
   - Indent the `$$` block to match the list item's indentation level so the equation remains part of that list item:
   ```markdown
   1. **Setup Time Constraint:**
      $$
      T_{c} \ge t_{pcq} + t_{pd} + t_{setup} + t_{skew}
      $$
   ```

5. **Display Math Inside Callouts / Blockquotes:**
   - Prefix every line of the display block with `>`:
   ```markdown
   > [!abstract] Definition: One-to-One Function
   > $$
   > f(x_1) \neq f(x_2) \quad \text{whenever } x_1 \neq x_2
   > $$
   ```

### 1.4 Heading Structure & Section Dividers
- **Heading Hierarchy:**
  - `# X.Y Section Title` (H1) for major top-level sections.
  - `## Topic Name` (H2) for main subtopics.
  - `### Concept Name` (H3) for subsections and specific concepts.
  - `#### Problem XY: Relevant Title` (H4) for selected problems (only when asked specifically).
- **Section Separators (`---`):**
  - Horizontal rules (`---`) are **strictly reserved** for separating major top-level `#` (H1) sections (e.g., between `# Overview`, `# 1.1 ...`, and `# Skeleton Index`).
  - **Do NOT** use `---` within a section (no dividers between subsections, proofs, or callouts).

### 1.5 Obsidian Callouts & Proofs
Use standard Obsidian callout syntax as visual anchors for formal theoretical components, while keeping the surrounding explanation in conversational prose (do not trap the entire note inside callouts):
- `> [!abstract] Definition: [Term]` — for formal definitions and axioms.
- `> [!abstract] Problem Statement` — for selected problem statements.
- `> [!theorem] [Theorem / Law Name]` — for formal theorems, laws, lemmas, and corollaries.
- `> [!warning] [Caution / Pitfall]` — for common misconceptions or notational cautions.
- `> [!summary] [Summary]` — for section or concept summaries.
- `> [!note] [Theoretical Remark]` — for key conceptual remarks, intuitions, and design trade-offs.
- **Proofs/Solutions:** Place proofs/solutions directly **below** the corresponding callout in regular text (not inside a callout). Begin with `**Proof/Solution:**`, walk through the logical and algebraic steps conversationally so the reasoning behind each step is clear, and conclude with `$\blacksquare$`.

### 1.6 Figures, Diagrams & Tables
- **Contextual Placement:** Weave figure references directly into the conceptual flow where the concept is explained—never batch or dump all images at the end of the note.
- **Existing Image References:** If an image filename or reference exists in the source (e.g., `![](image_0.png)` or extracted page figures), place it immediately adjacent to the relevant explanation.
- **Diagram Placeholders:** When a diagram, plot, or waveform is discussed in the source but no image file is present, insert an explicit placeholder using this exact format:
  ```markdown
  > [!figure] Figure Placeholder: Figure X.Y - [Brief description]
  ```
- **Tables & Truth Tables:** Clean up broken OCR tables, truth tables, state transition tables, or comparison grids into properly formatted, aligned Markdown tables.

### 1.7 Source Correction & Jargon Accuracy
- **OCR Flaws:** Repair OCR artifacts, broken line wraps, and garbled symbols using domain terminology.
- **Transcripts / Spoken Audio:** Correct phonetic speech-to-text misinterpretations into standard domain terminology (e.g., convert "sea moss" to "CMOS", "key map" to "K-map", "t p d" to propagation delay `$t_{pd}$`).

---

## 2. Skeleton Index Guidelines

These guidelines apply when creating or updating an active-recall **Pure Skeleton Index** for revision and study. The skeleton index functions like a closed-book examination paper: forcing complete active recall without providing hints, solutions, formulas, or hand-holding.

### 2.1 Strict 1:1 Sequential Order (No Conceptual Pooling)
- **Sequential Flow:** The skeleton index must strictly follow the exact 1-to-1 sequential, chronological order of headings, subheadings, topics, and added problems as they appear in the source notes from top to bottom.
- **No Artificial Pooling:** Do **NOT** group items across sections into artificial buckets (e.g., do not lump all definitions together into a single "Definitions" section or all theorems into a "Theorems" section). Follow the natural narrative flow of the notes.

### 2.2 Placement & Heading Hierarchy
When placed at the end of a note file, precede the index with a horizontal rule (`---`) and a top-level `# Skeleton Index` heading, then format cleanly using standard Markdown headings and bullet lists:
- `# Skeleton Index` (H1) as the top-level container heading at the end of the note.
- `## [Section Number & Title]` (H2) for main sections.
- `### [Subsection Title]` (H3) for subsections within a section.
- `**[Topic Title]**` for specific topics within a subsection.
- Bullet points (`- ...`) under the topic headings for active-recall prompts and cues.

### 2.3 Zero Spoilers / Exam Conditions (No Hand-Holding)
1. **No Formulas, Equations, or Values in Theory Items:**
   - State *what* needs to be recalled, derived, or stated; never reveal the formula, equation, numerical value, bound, or conclusion.
   - *Example:* Write *"Derive the expression for [Metric/Variable]"* instead of writing the formula.
   - *Example:* Write *"State the bounds on [Parameter]"* instead of stating the bounds.
2. **No Proof or Derivation Hints:**
   - Never disclose the proof technique, intermediate algebraic substitution, or shortcut.
   - *Example:* Write *"Prove [Theorem/Law/Property] analytically and conceptually"* rather than hinting at the substitution or identity used.
3. **No Leaked Conclusions:**
   - Do not spoil the outcome when asking to evaluate, compare, or explain behavior.
   - *Example:* Write *"Analyze the effect of [X] on [Y]"* instead of *"Explain why [X] increases [Y]"*.
4. **Strictly No Solutions:** Exclude all answers, derivations, and solution steps from prompts.

### 2.4 Curated Problems in the Notes (Full Problem Statements)
- Whenever the notes contain curated exercises or problems (such as problem-set questions added after reading a section), **include them in the Skeleton Index with the problem statement written completely and in full**.
- Include all premises, specifications, initial conditions, numbers, data points, and the exact question or claim to be solved/proved.
- The student must never be forced to memorize what the question asked—only how to solve, derive, or prove it.
- **Do not include** the solution, intermediate steps, hints, or final answers within the problem statement.

### 2.5 Actionable Test Prompts
- Phrase theoretical prompts as active challenges using strong imperative verbs:
  - *"Define..."*
  - *"State the necessary conditions for..."*
  - *"State and prove [Theorem/Law Name]"*
  - *"Derive the governing equation for..."*
  - *"Explain the mechanism behind..."*
  - *"Compare [X] vs [Y] in terms of [Criteria]"*
  - *"Determine..."*
  - *"Evaluate and justify..."*
- Never include parenthetical answers, hints, or solution steps in the cues.

### 2.6 Strict LaTeX Compliance
- Follow all LaTeX formatting rules from **Section 1.3** (`$ ... $` for inline math and separate-line `$$ ... $$` for display math) for any mathematical symbols or problem statements in the index.

### 2.7 Exhaustive Conceptual Coverage
- Cover every core definition, governing law/theorem, principle, mechanism, mathematical derivation, model, trade-off, and curated problem present in the notes.