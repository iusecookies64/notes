
### Textbook Text To Notes

Act as an expert academic note-taking assistant. I will provide you with raw text copied from a PDF textbook (which may contain OCR errors, broken line wraps, or garbled tables/figure captions). Your task is to generate comprehensive, publication-quality study notes based strictly on the provided text.

Follow these strict rules:

1. **Source Correcting:** If the text has some flaws (due to OCR), use your own knowledge to write the correct definitions, interpretations, formulas etc.
2. **Skip Examples:** Only create the notes of theory and skip examples.
3. **Direct Delivery:** Jump straight into the notes. Do not write introductory greetings, meta-announcements ("Here are your notes:"), or conversational closings.
4. **Mathematical Rigor & LaTeX:** Render all variables, equations, and mathematical statements using LaTeX ($...$ for inline, and
	$$
	...
	$$
	on separate lines for display equations). If some math segment is multi step, then use
	$$
	\begin{align}
	\text{steps here}
	\end{align}
	$$
	Properly indent the math blocks when inside of a list like the above one. When inside of block quote, then use the following way,
> Inside block quotes, use the following way to write block math,
> $$
> \text{Math Here}
> $$
> Inline math continues to be like normal i.e. $\dots$.
5. **Figure Placeholders:** Whenever a figure, plot, or diagram is mentioned in the text and you think it is important, then, insert a placeholder in this format:

**[Image Placeholder: Figure X.X]**  

5. **Table Reconstruction:** Clean up any broken, OCR-scrambled data tables and format them as clean, well-aligned Markdown tables.

Here is the textbook text:
[PASTE TEXTBOOK TEXT HERE]

---

### Generate Skeleton Index

Act as an expert academic study and revision assistant across any technical or theoretical subject. I will provide you with my notes text. Your task is to generate an active-recall "Pure Skeleton Index" based strictly on the provided content. The index must act like a rigorous closed-book examination paper—forcing complete active recall without providing any hints, solutions, formulas, or hand-holding.

Follow these strict rules:

1. **Strict 1:1 Sequential Order (No Conceptual Pooling):**
   - The skeleton index must strictly follow the exact 1-to-1 sequential, chronological order of the headings, subheadings, and topics as they appear in the source notes from top to bottom.
   - Do NOT pool or group items across sections into artificial buckets (e.g., do NOT lump all definitions together or all theorems together). Follow the natural narrative flow of the notes.

2. **Markdown Heading Hierarchy:**
   - Format the skeleton index simply using standard Markdown headings and bullet lists:
     - `## [Section Number & Title]` for main sections.
     - `### [Subsection Title]` for subsections within a section.
     - `**[Topic Title]**` for specific topics within a subsection.
     - Bullet points (`- ...`) under the topic headings for further active-recall prompts and cues.

3. **Strict LaTeX Delimiters (`$` and `$$`):**
   - All mathematical variables, equations, vectors, matrices, bounds, and symbols MUST use proper LaTeX delimiters:
     - Inline math: `$ ... $` (e.g., `$Ax = b$`, `$\mathbb{R}^n$`, `$V^\perp$`).
     - Display / block equations:
       $$
       \text{math here}
       $$
       on separate lines.
   - Never write naked mathematical symbols or plaintext formulas without delimiters.

4. **Zero Spoilers / Exam Conditions (No Hand-Holding):**
   - **No Formulas, Equations, or Values in Theory Items:** For theoretical concepts and derivations, state *what* needs to be recalled or derived, but never disclose the resulting formula, equation, numerical value, bound, or conclusion (e.g., write *"Derive the expression for [Metric/Variable]"* instead of stating the formula itself; write *"State the bounds on [Parameter]"* instead of writing the bounds).
   - **No Proof or Derivation Hints:** Never reveal the proof technique, intermediate algebraic trick, substitution, or critical shortcut (e.g., write *"Prove [Theorem/Law/Property] analytically and conceptually"* rather than hinting at the intermediate identity or technique used).
   - **No Leaked Conclusions:** Do not spoil the outcome when asking to evaluate, compare, or explain behavior (e.g., write *"Analyze the effect of [X] on [Y]"* instead of stating *"Why [X] increases [Y]"*).
   - **Strictly No Solutions:** Exclude all answers, derivations, and solution steps from the prompts.

5. **Full Problem & Example Statements (Never Require Memorizing the Question):**
   - For all exercises, practice problems, and non-trivial worked examples, **state the problem statement completely and in full**. Include all given premises, specifications, initial conditions, numbers, data points, and the exact question or claim to be solved/calculated/proved.
   - The user must never be forced to memorize what the problem was asking—they should only have to supply the *solution, proof, derivation, or calculation*.
   - Never attach the solution, intermediate steps, hints, or final answers inside the problem statement.

6. **Actionable Test Prompts:**
   - Phrase theoretical items as active test questions or challenges using strong imperative verbs: *"Define..."*, *"State the necessary conditions for..."*, *"State and prove [Theorem/Law Name]"*, *"Derive the governing equation for..."*, *"Explain the mechanism behind..."*, *"Compare [X] vs [Y] in terms of [Criteria]"*, *"Determine..."*, *"Evaluate and justify..."*.
   - Never include parenthetical answers, hints, or solution steps in the cues.

7. **Exhaustive Conceptual Coverage:**
   - Cover every core definition, governing law/theorem, principle, mechanism, mathematical derivation, model, trade-off, and non-trivial exercise. Skip only trivial arithmetic examples.

Here is the text:
[PASTE YOUR NOTES / TEXT HERE]


---

### Generate Solutions To Problems

Please provide concise, step-by-step solutions to the following problems in sequential order. 

For each problem, format the output exactly as follows:
1. ### [Descriptive Title]
2. Clean up and restate the problem text (repairing any OCR errors or broken line wraps) starting with the problem number first (e.g. **(6)**).
3. Provide the concise solution using standard LaTeX for mathematical notation.
4. Separate each problem with another horizontal rule (`---`).

Here are the problems:
[Paste your problems here]

---

### Markdown + Transcript To Notes

Act as an expert computer engineering teaching assistant specializing in Digital Design and Computer Architecture (DDCA). I will provide you with two sources for a single lecture:
1. **Slide Markdown**: Raw Markdown extracted from the lecture slides via Marker (contains slide text, bullet points, and extracted figure filenames like `![](image_X.png)` or `_page_X_Figure_Y.png`).
2. **Lecture Transcript**: An automated transcript of the professor's spoken lecture (may contain phonetic speech-to-text errors, run-on sentences, or missing technical jargon).

Your task is to synthesize both sources into comprehensive, publication-quality, Obsidian and Quartz-compatible lecture notes. Merge the structured technical definitions from the slides with the professor's spoken intuitions, design trade-offs, and real-world microarchitecture context.

Follow these strict rules:

1. **Direct Delivery:** Jump straight into the YAML frontmatter and the notes. Do not write any conversational preamble, introductory meta-announcements ("Here are your notes:", "Sure, I can synthesize this:"), or concluding summaries.
2. **Transcript Error Correction & Domain Accuracy:** Clean up phonetic speech-to-text mistakes into precise computer engineering terminology:
	- Correct misheard hardware terms (e.g., replace "sea moss" with "CMOS", "end moss / pee moss" with "nMOS / pMOS", "key map" with "K-map", "latch up" with "latch-up", "clock skew" with "clock skew").
	- Fix broken mathematical statements and timing terminology (e.g., translate spoken "t p d" or "propagation time" to propagation delay $t_{pd}$, and "t c d" to contamination delay $t_{cd}$).
3. **Mathematical Rigor & LaTeX Formatting:**
- Use inline math `$ ... $` for all individual variables, logic levels, signals, timing parameters, and Boolean terms (e.g., `$V_{DD}$`, `$A \cdot \overline{B}$`, `$t_{pd}$`).
- Use standalone display math for equations:
	$$
	F = \overline{A \cdot B} + (C \oplus D)
	$$
	Make sure that it is double dollar characters are in separate lines and in the math in the lines between.
- For multi-step derivations, timing constraints, or Boolean algebra simplifications, use an `aligned` block:
	$$
	\begin{aligned} F &= \overline{(A + B) \cdot (C + D)} \\   &= \overline{A + B} + \overline{C + D} \\   &= (\overline{A} \cdot \overline{B}) + (\overline{C} \cdot \overline{D}) \end{aligned}
	$$
- If display math is placed inside a numbered or bulleted list, indent the `$$` block so it remains part of the list item:
  * Setup time constraint:
	$$
	T_{c} \ge t_{pcq} + t_{pd} + t_{setup} + t_{skew}
	$$
- If display math is inside an Obsidian callout or blockquote, then format it exactly as shown below:
  > **Key Formula:** 
  > $$
  > P_{\text{dynamic}} = \frac{1}{2} C V_{DD}^2 f \alpha
  > $$

### 5. Figure & Diagram Placement
Do not drop all images at the bottom. Weave them directly into the conceptual flow where the professor explains them:
- If an image reference exists in the Slide Markdown (e.g., `![](image_0.png)` or `_page_3_Figure_1.png`), place it immediately above or below the corresponding concept explanation.
- If the professor references a critical diagram or timing chart in the transcript that lacks an extracted filename, insert a descriptive placeholder:
  `[Diagram Placeholder: Timing waveform showing clock, D, and Q with setup/hold violation windows]`

### 7. Tables & Truth Tables
Clean up any garbled truth tables, state transition tables, or comparison grids into properly formatted Markdown tables.

Input files are attached.


---

### Textbook Images To Notes

I am studying calculus from the book *Calculus and Analytic Geometry (9e)*. Whenever I finish reading a section of a chapter, I want notes to revise later. The notes must be neatly formatted Markdown intended for an Obsidian vault. The book's pages have been extracted into images and placed in the `extracted/` directory.

Go through the provided page range and create comprehensive theoretical notes covering each and every concept taught in those pages.

---

### Core Instructions

#### 1. Mathematical Precision & LaTeX Formatting (CRITICAL / TOP PRIORITY)
Math is the most important part of these notes.
- **Math Block Delimiters (`$$`):**
  - The opening `$$` and closing `$$` **MUST** be on their own separate lines.
  - **Never** write inline math blocks like `$$formula$$` on a single line.
  - This rule applies universally across every context:
    - **Top-level text:**
      ```markdown
      $$
      f(x) = \int_1^x \frac{1}{t} \, dt
      $$
      ```
    - **Inside Callouts / Blockquotes:**
      ```markdown
      > [!abstract] Definition: ...
      > $$
      > f(x_1) \neq f(x_2) \quad \text{whenever } x_1 \neq x_2
      > $$
      ```
    - **Inside Lists and Nested Lists:** Match list indentation for the delimiters:
      ```markdown
      1. **Case 1:** Explanation here:
         $$
         \ln(ax) = \ln a + \ln x
         $$
      ```
- **Multi-line Algebraic Derivations:**
  - Use `\begin{align} ... \end{align}` inside `$$ ... $$` with `&` alignment and `\\` line breaks for multi-step proofs and derivations.
- **LaTeX Conventions:**
  - Use standard symbols.
  - Inline math must use `$formula$` with no spaces immediately inside the dollar signs.

#### 2. Section Separators (`---`)
- Horizontal rules (`---`) are **STRICTLY** reserved for separating major top-level sections (e.g., between `# Overview` and `# 6.1 ...`, or between `# 6.1 ...` and `# 6.2 ...`).
- **DO NOT** use `---` within a given section (no dividers between subsections, proofs, or callouts).

#### 3. Heading Structure
- `# X.Y Section Title` (H1) for major sections.
- `## Topic Name` (H2) for main subtopics.
- `### Specific Concept` (H3) for sub-sections.
- so on.

#### 4. Obsidian Callouts & Figure Placeholders
- Use appropriate Obsidian callout syntax for key theoretical components:
  - `> [!abstract] Definition: ...`
  - `> [!theorem] Theorem Name`
  - `> [!warning] Notational Caution`
  - `> [!summary] Summary of ...`
  - `> [!note] Theoretical Remark on ...`
- **Figures / Diagrams:** Leave placeholders using callouts:
  ```markdown
  > [!figure] Figure Placeholder: Figure X.Y
  ```

#### 5. Scope & Theoretical Depth
- **Cover ALL theory:** Include every definition, theorem, corollary, full step-by-step proof etc present in the texbook.
- **Skip Examples & Problems:** Do not include numerical examples, exercises, or problem sets; focus 100% on theory.

#### 6. Output File Location & Naming
- Create the markdown file named after the chapter inside the `Markdown Notes/` directory (e.g., `Markdown Notes/Transcendental Functions.md`).
- If a file for that chapter already exists, append numbers: `2`, `3`, and so on.

#### 7. Directly start with the task
- You don't need to investigate, or do anything, all files are already present in `./extracted/page-{number}.png` format.
- Read any of the previous notes, and then directly start with the task (use your view file tool).

---

### Page Range for Current Task
The page range for this task is: 541 - 544 (section 6.11 theory)



