# Agent Guidelines

This document provides instructions and standards for CLI-based AI agents working within this repository. Follow these guidelines strictly when writing study notes, or generating active-recall indexes.

---

## 1. General Agent Operating Principles

- **Direct Delivery:** Jump straight into the requested task, frontmatter, or content. Avoid conversational pleasantries, introductory announcements (e.g., "Sure, here are your notes:"), or conversational sign-offs.
- **Obsidian & Quartz Compatibility:** All markdown produced must render cleanly in both Obsidian and Quartz.
- **Documentation Integrity:** Preserve existing structure, references, and frontmatter unless explicitly tasked with modifying them.
- Always jump directly to the task, don't try to explore files you are not asked to use.
- Don't run any scripts, unless asked otherwise. If the task requires you to run scripts, but user not mentioned, then ask first.

---

## 2. Note Writing Guidelines

These guidelines apply whenever creating, synthesizing, or cleaning up academic and technical study notes from textbooks, lecture slides, transcripts, or images.

### 2.1 Scope & Theoretical Rigor
- **Comprehensive Theory:** Focus 100% on theory and fundamental principles. Unless explicitly instructed otherwise, exclude numerical examples, practice problems, and arithmetic exercises.
- **Analytical Proofs & Formalization:** When source material introduces concepts conversationally, relies on examples to justify claims, or defers proofs, supply the standard analytical proofs, derivations, and precise terminology for those concepts.
- **Strict Scope Boundary:** Theoretical formalization must strictly support concepts *already introduced* in the material. Do not import unmentioned advanced topics, future chapters, or external syllabus material.

### 2.2 LaTeX & Math Formatting
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

### 2.3 Heading Structure & Section Dividers
- **Heading Hierarchy:**
  - `# X.Y Section Title` (H1) for major top-level sections.
  - `## Topic Name` (H2) for main subtopics.
  - `### Concept Name` (H3) for subsections and specific concepts.
- **Section Separators (`---`):**
  - Horizontal rules (`---`) are **strictly reserved** for separating major top-level sections (e.g., between `# Overview` and `# 1.1 ...`, or between major chapters/sections).
  - **Do NOT** use `---` within a section (no dividers between subsections, proofs, or callouts).

### 2.4 Obsidian Callouts
Use standard Obsidian callout syntax for key theoretical components:
- `> [!abstract] Definition: [Term]` — for definitions and axioms.
- `> [!theorem] [Theorem / Law Name]` — for theorems, laws, and corollaries.
- `> [!warning] [Caution / Pitfall]` — for common misconceptions or notational cautions.
- `> [!summary] [Summary]` — for section or concept summaries.
- `> [!note] [Theoretical Remark]` — for conceptual remarks, intuitions, and design trade-offs.

### 2.5 Figures, Diagrams & Tables
- **Contextual Placement:** Weave figure references directly into the conceptual flow where the concept is explained—never batch or dump all images at the end of the note.
- **Existing Image References:** If an image filename or reference exists in the source (e.g., `![](image_0.png)` or extracted page figures), place it immediately adjacent to the relevant explanation.
- **Diagram Placeholders:** When a diagram, plot, or waveform is discussed in the source but no image file is present, insert an explicit placeholder:
  ```markdown
  > [!figure] Figure Placeholder: Figure X.Y - [Brief description]
  ```
  or:
  ```markdown
  **[Image Placeholder: Figure X.X - Description]**
  ```
- **Tables & Truth Tables:** Clean up broken OCR tables, truth tables, state transition tables, or comparison grids into properly formatted, aligned Markdown tables.

### 2.6 Source Correction & Jargon Accuracy
- **OCR Flaws:** Repair OCR artifacts, broken line wraps, and garbled symbols using subject matter knowledge.
- **Transcripts / Spoken Audio:** Correct phonetic speech-to-text misinterpretations into standard domain terminology (e.g., convert "sea moss" to "CMOS", "key map" to "K-map", "t p d" to propagation delay $t_{pd}$).

---

## 3. Skeleton Index Guidelines

These guidelines apply when creating an active-recall **Pure Skeleton Index** for revision and study. The skeleton index functions like a closed-book examination paper: forcing complete active recall without providing hints, solutions, formulas, or hand-holding.

### 3.1 Strict 1:1 Sequential Order (No Conceptual Pooling)
- **Sequential Flow:** The skeleton index must strictly follow the exact 1-to-1 sequential, chronological order of headings, subheadings, and topics as they appear in the source notes from top to bottom.
- **No Artificial Pooling:** Do **NOT** group items across sections into artificial buckets (e.g., do not lump all definitions together into a single "Definitions" section or all theorems into a "Theorems" section). Follow the natural narrative flow of the notes.

### 3.2 Heading Hierarchy
Format the skeleton index cleanly using standard Markdown headings and bullet lists:
- `## [Section Number & Title]` for main sections.
- `### [Subsection Title]` for subsections within a section.
- `**[Topic Title]**` for specific topics within a subsection.
- Bullet points (`- ...`) under the topic headings for active-recall prompts and cues.

### 3.3 Zero Spoilers / Exam Conditions (No Hand-Holding)
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

### 3.4 Full Problem & Example Statements (Never Require Memorizing the Question)
- For all exercises, practice problems, and non-trivial worked examples, **state the problem statement completely and in full**.
- Include all premises, specifications, initial conditions, numbers, data points, and the exact question or claim to be solved/proved.
- The student must never be forced to memorize what the question asked—only how to solve, derive, or prove it.
- **Do not include** the solution, intermediate steps, hints, or final answers within the problem statement.

### 3.5 Actionable Test Prompts
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

### 3.6 Strict LaTeX Delimiters
- All mathematical variables, equations, vectors, matrices, bounds, and symbols must use proper LaTeX delimiters:
  - Inline: `$ ... $` (e.g., `$Ax = b$`, `$\mathbb{R}^n$`, `$V^\perp$`).
  - Display math: `$$ ... $$` on separate lines.
- Never write naked mathematical symbols or plaintext formulas.

### 3.7 Exhaustive Conceptual Coverage
- Cover every core definition, governing law/theorem, principle, mechanism, mathematical derivation, model, trade-off, and non-trivial exercise.
- Skip only trivial arithmetic examples.

### Important
- If asked to make notes, then you don't have to make the skeleton index, the request for making skeleton index will be made explicitly.

---

## 4. Present Task

Read pages associated with section 6.3 from @tempp/Linear Algebra/extracted directory using view_file and the section spans from page 246 to 256. Then add the notes in the file @content/Mathematics/Linear Algebra (Strang)/06. Eigenvalues and Eigenvectors.md (end of the file).
