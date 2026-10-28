# Visualization Guidelines

This document defines the environment, libraries, styling standards, workspace structure, and workflows for generating mathematical and technical visualizations (static figures and animations) across the repository.

---

## 1. Environment & Available Libraries

All visualization scripts must run inside the dedicated **`visuals`** Conda environment (Python 3.11):
- Run commands via `conda run -n visuals <command>` or after activating the environment via `conda activate visuals`.

### Available Libraries and Tools:
- **Manim Community (`manim`)**: Programmatic 2D/3D mathematical animations and static scene frames (`manim -s`).
- **Matplotlib (`matplotlib`)**: 2D and 3D plotting, coordinate geometry, custom patches, and publication-quality figures.
- **Pillow (`PIL`)**: Raster image processing, transformations, and format conversion.
- **NumPy & SciPy**: Vector/matrix computations, coordinate projection, numerical calculus, and scientific algorithms.
- **SymPy**: Symbolic mathematics, algebraic derivations, and exact formula manipulation.
- **Seaborn**: Statistical data visualizations and styled distribution plots.
- **Plotly**: Modern interactive and high-resolution charting.
- **NetworkX**: Graph theory structures, network nodes, and tree visualizations.
- **LaTeX (pdfTeX / TeX Live with `amsmath`, `amssymb`)**: Native typesetting for LaTeX mathematical typography.
- **ffmpeg**: Video compilation, slicing, re-encoding, and audio/video format conversions.

---

## 2. Workspace & Directory Rules

- Put all visualization projects inside **`tempp/Visualization/`**.
- For each visualization task, create a dedicated folder inside `tempp/Visualization/` (e.g., `tempp/Visualization/<task_name>/`).
- Place **all** script files, intermediate build/media files (e.g., `./media`), and final exported outputs inside this dedicated task folder.
- Execute all generation scripts from inside that dedicated folder (or pass `--media_dir ./media`) so that **nothing is generated outside this folder**.

---

## 3. Universal Theme & Verification Rules

- **Dark Theme:**
  - Set the background color to `#121212` (for Manim: `config.background_color = "#121212"`; for Matplotlib: `facecolor="#121212"` on both figure and axes).
  - Use light, high-contrast, vivid colors for all axes, grids, geometry, text, and labels (e.g., Cyan `#38BDF8`, Salmon/Coral `#F87171`, Gold `#FACC15`, Violet `#C084FC`, Teal `#2DD4BF`, Crisp White `#FFFFFF`, Slate Gray `#94A3B8`).
- **Clutter-Free Visuals:**
  - Prioritize visual geometry, intuitive arrows, and concise mathematical notations over large blocks of text.
  - Avoid lengthy paragraphs, explanations, or cards inside the diagram itself unless explicitly requested.
- **No Self-Verification via Image/Video Inspection:**
  - **Do NOT visually verify the output yourself** (do not extract frames, read image files, or inspect generated videos/images). It is unreliable and wastes tokens.
  - Rely on execution exit codes and terminal logs to ensure successful rendering, then invite the user to review the final output.
- **Subagents for Multiple Visuals:**
  - When generating multiple diagrams or complex visual suites, delegate separate visuals to subagents where each subagent strictly adheres to these guidelines.

---

## 4. Format-Specific Instructions

### 4.1 Static Figures (Matplotlib or Manim Static `-s`)
- **Format:** Export or convert the final figure into a storage-efficient **`.webp`** file.
- **Export Methods:**
  - **Matplotlib / Pillow:**
    ```python
    fig.savefig("output.webp", format="webp", dpi=150, pil_kwargs={"quality": 85}, bbox_inches="tight")
    ```
  - **CLI Tools:**
    ```bash
    cwebp -q 85 input.png -o output.webp
    # or
    ffmpeg -i input.png -c:v libwebp -quality 85 output.webp
    ```
- **Workflow:**
  1. Write the figure generation script inside `tempp/Visualization/<task_name>/`.
  2. Execute the script in the `visuals` environment and resolve any runtime/LaTeX errors.
  3. Ensure the final image is saved as `.webp` inside the dedicated folder.
  4. Ask the user to review the generated figure.

---

### 4.2 Animations (Manim Community / Video)
- **Format:** Export or convert the final animation into a storage-efficient **`.webm`** file (VP9 codec).
- **Resolution & Framerate:** Render at **720p** resolution (`1280x720`, 30 fps — e.g., `manim -qm` or `-r 1280,720 --fps 30`).
- **Conversion Command:**
  ```bash
  ffmpeg -i input.mp4 -c:v libvpx-vp9 -b:v 0 -crf 36 -an output.webm
  ```
- **Workflow:**
  1. Write the Manim script inside `tempp/Visualization/<task_name>/`.
  2. Compile the script to video with `--media_dir ./media` (to ensure intermediate files stay local) and resolve any syntax or runtime errors.
  3. Convert the rendered `.mp4` into a `.webm` file inside the dedicated folder.
  4. Ask the user to review the rendered video.