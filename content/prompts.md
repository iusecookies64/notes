
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

Act as a study and revision assistant. I will provide you with my notes text. Your task is to generate an active-recall "Pure Skeleton Index" based strictly on the provided content.

Follow these rules:
1. **Zero Spoilers / No Hand-Holding:** Do not include answers, complete formulas, algebraic derivations, or full explanations. State *what* needs to be recalled or proved, not the solution itself.
2. **Exhaustive Detail:** Cover all important concept, definition, theorem, corollary, proof method, application etc, skip trivial problems/examples.
3. **Problems:** For problems, provide a short statement or setup followed by the things need to be calculated.
4. **Structured Hierarchy:** Organize by section, then by logical concept clusters (e.g., Definitions, Core Examples, Theorems & Proofs).
5. **Actionable Recall Cues:** Phrase every item as a clear, minimal prompt (e.g., "Definition of...", "Theorem: [Name] (conditions & statement)", "Proof of [Theorem] via [Method/Step]", "Counterexample: [Scenario]").

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


