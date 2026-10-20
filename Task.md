Apply the required fixes below to Section 6.4 in @[content/Mathematics/Linear Algebra (Strang)/06. Eigenvalues and Eigenvectors.md]. The section is based on Strang, pp. 262-268 (extracted pages in `tempp/Linear Algebra/extracted/page-262.png` to `page-268.png`). Do not rewrite the section. Make only these targeted edits, preserve the existing structure, formatting, callouts, and Skeleton Index order, and follow `Agents.md`.

## Required Fixes (Must Fix)

1. **Fix the DFT sign convention mismatch (p. 267 vs. notes):**
   - Strang defines the Discrete Fourier Transform of a vector $x$ as $\bar{F}x$, but the notes define $y = F_N x$ with $w_N = e^{+2\pi i / N}$ in the DFT subsection.
   - Either change the notes to adopt Strang's convention ($\bar{F}x$), or add one explicit line in the DFT subsection stating that the notes use the opposite sign convention to Strang.
   - Keep the rest of the FFT / convolution material internally consistent with whichever convention is chosen.

2. **Add the missing Rayleigh quotient extremal principle (p. 264):**
   - After the Spectral Theorem for Complex Hermitian Matrices, add a short paragraph stating that maximizing the Rayleigh quotient $\frac{x^H S x}{x^H x}$ gives $\lambda_{\max}$, minimizing it gives $\lambda_{\min}$, and the in-between eigenvalues are saddle points of the quotient.
   - Do not add numerical examples.
   - Add a matching prompt to the 6.4 Skeleton Index (after the Spectral Theorem / Schur prompts) asking to state this extremal principle, without leaking the conclusion in the prompt.

3. **Correct the rotation-scaling geometry claim (Real Invariant Subspaces subsection):**
   - The block $\begin{bmatrix} a & b \\ -b & a \end{bmatrix}$ equals $r$ times a rotation by $-\theta$ (not $+\theta$) in $(u, v)$ coordinates, where $r = |\lambda|$ and $\theta = \arg(\lambda)$.
   - Qualify the geometric claim: this is a genuine Euclidean rotation-scaling only if $u$ and $v$ are orthonormal, which is not guaranteed in general. State it as a rotation-scaling in the $(u, v)$ coordinate representation instead of an unconditional planar rotation.

4. **Make the eigenvalue guarantee precise (section introduction):**
   - Change the claim that every $n \times n$ matrix is guaranteed to possess $n$ eigenvalues to state that every $n \times n$ matrix possesses $n$ eigenvalues over $\mathbb{C}$, counted with algebraic multiplicity.

## Secondary Fixes (Should Fix)

5. **Remove the unfulfilled "normal matrices" promise (section introduction):**
   - The introduction promises the spectral theory of normal and unitary matrices, but no normal-matrix theorem is stated in the section. Delete "normal and" from that promise, or remove the incidental normal-matrix remark near the Fourier orthogonality discussion. Do not add a new normal-matrix theory subsection (out of scope for pp. 262-268).

6. **Remove the loose orthogonality hand-wave (Fourier matrix discussion):**
   - Delete the claim that $P_N$ being a real orthogonal matrix by itself guarantees orthogonal eigenvectors for distinct eigenvalues, since that theorem is never proved in the notes. Keep the direct geometric-series proof of $F_N^H F_N = N I$ that follows it.

7. **Note the Hadamard product notation equivalence:**
   - Strang writes the Hadamard (componentwise) product as `.*` on p. 268, while the notes use $\odot$. Add one short line noting the two notations are equivalent.

8. **Handle out-of-scope extensions (Agents.md §2.1):**
   - The rotation-scaling subsection, the skew-Hermitian row in the comparison table, the Abel-Ruffini / Cardano / Ferrari / QR remark, and the zero-padding pipeline are not in pp. 262-268. Either trim them, or clearly mark them as extensions beyond Strang §6.4. Do not import any further topics.

## Out of Scope

- Do not add Problem Set 6.4 (the book's problem set starts after p. 268).
- Do not add numerical worked examples; the section follows the theory-only rule in `Agents.md` (the existing $N = 1024$ FFT comparison may stay).
- Do not change Sections 6.1-6.3 or their Skeleton Index entries.
