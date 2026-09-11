
### Textbook Text To Notes

Act as an expert academic note-taking assistant. I will provide you with raw text copied from a PDF textbook (which may contain OCR errors, broken line wraps, or garbled tables/figure captions). Your task is to generate comprehensive, publication-quality study notes based strictly on the provided text.

Follow these strict rules:

1. **Source Grounding:** Use ONLY the provided text. Do not invent outside facts, examples, or assumptions.
2. **Direct Delivery:** Jump straight into the notes. Do not write introductory greetings, meta-announcements ("Here are your notes:"), or conversational closings.
3. **Mathematical Rigor & LaTeX:** Render all variables, equations, and mathematical statements using LaTeX ($...$ for inline, $$...$$on separate lines for display equations).
4. **Figure Placeholders:** Whenever a figure, plot, or diagram is mentioned in the text and you think it is important, then, insert a placeholder in this format:

**[Image Placeholder: Figure X.X]**  

5. **Table Reconstruction:** Clean up any broken, OCR-scrambled data tables and format them as clean, well-aligned Markdown tables.

Here is the textbook text:
[PASTE TEXTBOOK TEXT HERE]

---

### Generate Skeleton Index

Act as a study and revision assistant. I will provide you with textbook notes or text. Your task is to generate a comprehensive, active-recall "Pure Skeleton Index" based strictly on the provided content.

Follow these rules:
1. **Zero Spoilers / No Hand-Holding:** Do not include answers, complete formulas, algebraic derivations, or full explanations. State *what* needs to be recalled or proved, not the solution itself.
2. **Exhaustive Detail:** Cover every concept, definition, theorem, corollary, proof method, application, example, case study, and counterexample mentioned in the text. Do not summarize or skip subtle details.
3. **Structured Hierarchy:** Organize by section, then by logical concept clusters (e.g., Definitions, Core Examples, Theorems & Proofs).
4. **Actionable Recall Cues:** Phrase every item as a clear, minimal prompt (e.g., "Definition of...", "Theorem: [Name] (conditions & statement)", "Proof of [Theorem] via [Method/Step]", "Counterexample: [Scenario]").
5. **No Conversational Fluff:** Output only the structured skeleton index.

Here is the text:
[PASTE YOUR NOTES / TEXT HERE]


Provide, concise solutions to the following problems, in the same order, also give each problem a fitting title, then state the question, then the solution separated by --- (horizontal rule). These are copied directly from the pdf textbook (ocr) so might have some formatting issues or broken line wraps, do you best to infer what the text is saying, and when is doubt, ask me to provide the exact screen shot.

**(6)** Benford’s law states that in a very large variety of real-life data sets, the first digit
approximately follows a particular distribution with about a 30% chance of a 1, an 18%
chance of a 2, and in general

 j +1
 
P (D = j) = log 10
 , for j ∈ {1, 2, 3, . . . , 9},
j
where D is the first digit of a randomly chosen element. Check that this is a valid PMF
(using properties of logs, not with a calculator).

**(9)** Let F1 and F2 be CDFs, 0 < p < 1, and F (x) = pF1 (x) + (1 − p)F2 (x) for all x.
(a) Show directly that F has the properties of a valid CDF (see Theorem 3.6.3). The
distribution defined by F is called a mixture of the distributions defined by F1 and F2 .
(b) Consider creating an r.v. in the following way. Flip a coin with probability p of
Heads. If the coin lands Heads, generate an r.v. according to F1; if the coin lands Tails,
generate an r.v. according to F2 . Show that the r.v. obtained in this way has CDF F .

**(33)** A book has n typos. Two proofreaders, Prue and Frida, independently read the book.
Prue catches each typo with probability p1 and misses it with probability q1 = 1 − p1 ,
independently, and likewise for Frida, who has probabilities p2 of catching and q2 = 1−p2
of missing each typo. Let X1 be the number of typos caught by Prue, X2 be the number
caught by Frida, and X be the number caught by at least one of the two proofreaders.
(a) Find the distribution of X.
(b) For this part only, assume that p1 = p2 . Find the conditional distribution of X1
given that X1 + X2 = t.

**(34)** There are n students at a certain school, of whom X ∼ Bin(n, p) are Statistics majors.
A simple random sample of size m is drawn (“simple random sample” means sampling
without replacement, with all subsets of the given size equally likely).
(a) Find the PMF of the number of Statistics majors in the sample, using the law of total
probability (don’t forget to say what the support is). You can leave your answer as a
sum (though with some algebra it can be simplified, by writing the binomial coefficients
in terms of factorials and using the binomial theorem).
(b) Give a story proof derivation of the distribution of the number of Statistics majors
in the sample; simplify fully.
Hint: Does it matter whether the students declare their majors before or after the
random sample is drawn?

**(37)** A message is sent over a noisy channel. The message is a sequence x1, x2 , . . . , xn of
n bits (xi ∈ {0, 1}). Since the channel is noisy, there is a chance that any bit might be
corrupted, resulting in an error (a 0 becomes a 1 or vice versa). Assume that the error
events are independent. Let p be the probability that an individual bit has an error
(0 < p < 1/2). Let y1 , y2 , . . . , yn be the received message (so yi = xi if there is no error
in that bit, but yi = 1 − xi if there is an error there).
To help detect errors, the nth bit is reserved for a parity check: xn is defined to be 0 if
x1 + x2 + · · · + xn−1 is even, and 1 if x1 + x2 + · · · + xn−1 is odd. When the message is
received, the recipient checks whether yn has the same parity as y1 + y2 + · · · + yn−1. If
the parity is wrong, the recipient knows that at least one error occurred; otherwise, the
recipient assumes that there were no errors.
(a) For n = 5, p = 0.1, what is the probability that the received message has errors
which go undetected?
(b) For general n and p, write down an expression (as a sum) for the probability that
the received message has errors which go undetected.
(c) Give a simplified expression, not involving a sum of a large number of terms, for the
probability that the received message has errors which go undetected.
Hint for (c): Letting
!
 !
X
 n k
 n−k X
 n k
 n−ka =
 p (1 − p) and b =
 p (1 − p) ,
k
 k
k even, k≥0
 k odd, k≥1
the binomial theorem makes it possible to find simple expressions for a + b and a − b,
which then makes it possible to obtain a and b.

**(42)** Let X be a random day of the week, coded so that Monday is 1, Tuesday is 2, etc. (so
X takes values 1, 2, . . . , 7, with equal probabilities). Let Y be the next day after X (again
represented as an integer between 1 and 7). Do X and Y have the same distribution?
What is P (X < Y )?

**(43)** (a) Is it possible to have two r.v.s X and Y such that X and Y have the same distribution
but P (X < Y ) ≥ p, where:
• p = 0.9?
• p = 0.99?
• p = 0.9999999999999?
• p = 1?
For each, give an example showing it is possible, or prove it is impossible.
Hint: Do the previous question first.
(b) Consider the same question as in Part (a), but now assume that X and Y are
independent. Do your answers change?

**(44)** For x and y binary digits (0 or 1), let x ⊕ y be 0 if x = y and 1 if x 6= y (this operation
is called exclusive or (often abbreviated to XOR), or addition mod 2 ).
(a) Let X ∼ Bern(p) and Y ∼ Bern(1/2), independently. What is the distribution of
X ⊕ Y ?
(b) With notation as in (a), is X ⊕ Y independent of X? Is X ⊕ Y independent of Y ?
Be sure to consider both the case p = 1/2 and the case p 6= 1/2.
(c) Let X1 , . . . , Xn be i.i.d. Bern(1/2). For each nonempty subset J of {1, 2, . . . , n}, let
M
YJ =
 Xj ,
j∈J
where the notation means to “add” in the ⊕ sense all the elements of J; the order in
which this is done doesn’t matter since x ⊕ y = y ⊕ x and (x ⊕ y) ⊕ z = x ⊕ (y ⊕ z).
Show that YJ ∼ Bern(1/2) and that these 2n − 1 r.v.s are pairwise independent, but
not independent. For example, we can use this to simulate 1023 pairwise independent
fair coin tosses using only 10 independent fair coin tosses.
Hint: Apply the previous parts with p = 1/2. Show that if J and K are two different
nonempty subsets of {1, 2, . . . , n}, then we can write YJ = A ⊕ B, YK = A ⊕ C, where A
consists of the Xi with i ∈ J ∩ K, B consists of the Xi with i ∈ J ∩ K c , and C consists of
the Xi with i ∈ J c ∩ K. Then A, B, C are independent since they are based on disjoint
sets of Xi . Also, at most one of these sets of Xi can be empty. If J ∩ K = ∅, then
YJ = B, YK = C. Otherwise, compute P (YJ = y, YK = z) by conditioning on whether
A = 1.