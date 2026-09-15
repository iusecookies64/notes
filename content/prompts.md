
### Textbook Text To Notes

Act as an expert academic note-taking assistant. I will provide you with raw text copied from a PDF textbook (which may contain OCR errors, broken line wraps, or garbled tables/figure captions). Your task is to generate comprehensive, publication-quality study notes based strictly on the provided text.

Follow these strict rules:

1. **Source Grounding:** Use ONLY the provided text. Do not invent outside facts, examples, or assumptions.
2. **Direct Delivery:** Jump straight into the notes. Do not write introductory greetings, meta-announcements ("Here are your notes:"), or conversational closings.
3. **Mathematical Rigor & LaTeX:** Render all variables, equations, and mathematical statements using LaTeX ($...$ for inline, and
$$
...
$$
	on separate lines for display equations). If some math segment is multi step, then use
$$
\begin{align}
\text{steps here}
\end{align}
$$
4. **Figure Placeholders:** Whenever a figure, plot, or diagram is mentioned in the text and you think it is important, then, insert a placeholder in this format:

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
3. **Structured Hierarchy:** Organize by section, then by logical concept clusters (e.g., Definitions, Core Examples, Theorems & Proofs).
4. **Actionable Recall Cues:** Phrase every item as a clear, minimal prompt (e.g., "Definition of...", "Theorem: [Name] (conditions & statement)", "Proof of [Theorem] via [Method/Step]", "Counterexample: [Scenario]").

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

