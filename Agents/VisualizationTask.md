Read @Agents/VisualizationGuidelines.md for visualization guidelines.

---

# Task
# Three Figures for Section 6.10

## Figure 1: Catenary vs. Galileo's Parabola
**Placement:** End of item 1, "The Hanging Chain (Catenary)."

**What to draw:** A chain hanging between two supports at equal height, with two curves overlaid on the same axes.
- **Catenary** (solid, bold): $y = a\cosh(x/a)$, with its lowest point (vertex) on the $y$-axis.
- **Parabola** (dashed, different color): fitted to match the catenary at the vertex and at the two supports.
- The two curves nearly coincide near the vertex and visibly separate toward the supports, where the catenary rises more steeply. Shade or arrow this gap and label it "curves diverge."
- Label the vertex, the arc length $s$ measured from the vertex to a point on the curve, and the constant $a$. Use a small inset to show the tension forces on a tiny chain segment (horizontal tension $T_0$, tangential tension $T$, weight $w\,ds$ downward).

**Caption:** *"Galileo's parabola vs. the true catenary: near the bottom the curves are almost indistinguishable, which is why the mistake was so easy to make."*

**Why it helps:** Students can see why Galileo's guess was reasonable and where it fails, and the force diagram links the physics to the equation $\frac{dy}{dx} = \frac{s}{a}$.

---

## Figure 2: Circle vs. Hyperbola Side by Side
**Placement:** Right after the sector-area theorem, before the proof.

**What to draw:** Two panels with identical axes and scale.
- **Left panel, unit circle** $x^2 + y^2 = 1$: a point $P(\cos t, \sin t)$ on the arc, the ray from the origin, and the circular sector shaded in blue. Label the shaded region "Area $A = t/2$," so $t = 2A$.
- **Right panel, right branch of the unit hyperbola** $x^2 - y^2 = 1$: a point $P(\cosh t, \sinh t)$, the ray from the origin, and the hyperbolic sector shaded in the same blue (bounded by the $x$-axis, the ray, and the arc from $(1,0)$). Label it "Area $A = t/2$," so $t = 2A$.
- Add the dashed asymptotes $y = \pm x$ in the right panel.
- Draw the coordinate "legs" from $P$ to the axes in both panels, labeled $\cos t, \sin t$ and $\cosh t, \sinh t$.
- Optionally, use a slider-style strip showing $t = 0.5, 1, 1.5$, with the point moving along each curve.

**Caption:** *"Both pairs of functions parametrize a unit conic by twice the sector area. This is the geometric reason for the name 'hyperbolic.'"*

**Why it helps:** The parallel layout makes the analogy visible, and the matching colors and labels show that only the sign in the curve's equation has changed.

---

## Figure 3: Decomposing the Sector Area (Proof Diagram)
**Placement:** Inside or just above the proof, where the text says "By inspecting the geometry in the first quadrant."

**What to draw:** A single hyperbola diagram in the first quadrant with $P(\cosh t, \sinh t)$ marked, showing the area subtraction as three color-coded regions:
1. **Right triangle** with vertices $(0,0)$, $(\cosh t, 0)$, $(\cosh t, \sinh t)$, outlined in gray, with area $\tfrac12 \cosh t \sinh t$.
2. **Region under the curve** $y = \sqrt{x^2-1}$ from $x = 1$ to $x = \cosh t$, shaded in orange, labeled $\int_1^{\cosh t}\sqrt{x^2-1}\,dx = \tfrac12\sinh t\cosh t - \tfrac t2$.
3. **Hyperbolic sector** (what remains), shaded in blue and labeled $A = \tfrac t2$.

Under the figure, add a mini "equation bar": **Triangle − Orange region = Blue sector**, with the color-coded expressions beneath each term so the cancellation of the $\tfrac12\cosh t\sinh t$ terms is visible.

**Caption:** *"The sector area is the triangle minus the area under the curve. The product terms cancel, leaving $A = t/2$."*

**Why it helps:** The proof's first step is stated verbally, and many students struggle to see which area is subtracted from which. The color coding ties each term in the algebra to a region of the picture.

---

**Bonus (if space allows):** A graph of $e^x$, $e^{-x}$, $\cosh x$, and $\sinh x$ on one set of axes would show $\cosh$ and $\sinh$ as the average and half-difference of the two exponentials. It would pair well with the introduction's claim that these are "special combinations of $e^x$ and $e^{-x}$."

I can also write TikZ, Desmos, or Python (matplotlib) code to generate any of these.