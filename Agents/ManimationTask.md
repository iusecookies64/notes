# Guidelines

## Environment & Files
- Use the `visuals` conda environment (Python 3.11, Manim Community, LaTeX, and ffmpeg installed). Run commands via `conda run -n visuals <command>` or after `conda activate visuals`.
- Put **all** code files, intermediate build/media files, and final output videos inside `tempp/ManimationDraft/`. Run Manim from inside `tempp/ManimationDraft/` (or pass `--media_dir tempp/ManimationDraft/media`) so nothing is generated outside this folder.

## Theme & Resolution
- Use a dark theme: set `config.background_color = "#121212"` and use light, high-contrast colors for all objects and text.
- Render at **720p** resolution (`1280x720`, 30 fps — e.g., `manim -qm` or `-r 1280,720 --fps 30`).

## Workflow
1. Write the Manim script in `tempp/ManimationDraft/`.
2. Compile the script to video and fix any syntax or runtime errors.
3. Convert the rendered video into a storage-efficient `.webm` file (e.g. VP9 with `ffmpeg -c:v libvpx-vp9 -b:v 0 -crf 36 -an`) inside `tempp/ManimationDraft/`.
4. Ask the user to review the rendered video.
- **Do NOT visually verify the output yourself** (do not extract frames or inspect images/video). It is unreliable and wastes tokens.

---

# Task
Create a 2D Manim Community animation that visually explains **why a 2D shift (translation) is NOT a linear transformation** by showing how the coordinate plane changes.

## Animation Description
- **Topic**: Linear Transformations in 2D — Why a Shift (Translation) is Not Linear
- **Scene Setup**:
  - A static background reference grid (dimmed) with a clearly marked fixed origin at $(0, 0)$ labeled $\vec{0}$.
  - A foreground transforming `NumberPlane` (bright blue/cyan) initially aligned with the reference grid, with basis vectors $\hat{i} = (1, 0)$ and $\hat{j} = (0, 1)$.

- **Steps**:
  1. **Recap of a True 2D Linear Transformation**:
     - Apply a standard linear transformation (e.g., $\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ or a rotation/scale) to the foreground plane.
     - Show caption: *"Linear Transformation: Grid lines stay parallel & evenly spaced, and the Origin stays fixed ($T(\vec{0}) = \vec{0}$)."*
     - Emphasize the origin dot staying pinned at $(0, 0)$, then restore the plane to its initial state.
  2. **Applying a 2D Shift (Translation)**:
     - Display the transformation rule: $T(\vec{v}) = \vec{v} + \vec{s}$ with shift vector $\vec{s} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$.
     - Animate the entire foreground plane shifting by $(2, 1)$ while the background reference grid and true origin $(0, 0)$ stay in place.
  3. **Reason 1 — The Origin Moves ($T(\vec{0}) \neq \vec{0}$)**:
     - Draw an arrow from the fixed origin $(0, 0)$ to the shifted grid's origin at $(2, 1)$.
     - Highlight that although grid lines remain parallel and evenly spaced, the origin has moved: $T(\vec{0}) = \vec{s} \neq \vec{0}$.
  4. **Reason 2 — Scaling Rule Breaks ($T(2\vec{v}) \neq 2T(\vec{v})$)**:
     - Pick a vector $\vec{v} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$ on the plane.
     - Visually compare the two results on the plane:
       - $T(2\vec{v}) = 2\vec{v} + \vec{s} = \begin{bmatrix} 4 \\ 3 \end{bmatrix}$ (scale first, then shift the plane once).
       - $2T(\vec{v}) = 2(\vec{v} + \vec{s}) = 2\vec{v} + 2\vec{s} = \begin{bmatrix} 6 \\ 4 \end{bmatrix}$ (shift first, then double — which shifts the origin twice!).
     - Conclude with the summary caption: *"A shift is an Affine Transformation, NOT a Linear Transformation."*
