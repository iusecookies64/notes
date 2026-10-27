# Guidelines

## Environment & Files
- Use the `visuals` conda environment (Python 3.11, Matplotlib, Manim Community, Pillow, LaTeX, and ffmpeg installed). Run commands via `conda run -n visuals <command>` or after `conda activate visuals`.
- Put **all** code files, intermediate build/media files, and final output images inside `tempp/FigureGenerationDraft/`. Run generation scripts from inside `tempp/FigureGenerationDraft/` so nothing is generated outside this folder.

## Theme & Format
- Use a dark theme: set background color to `#121212` and use light, high-contrast colors for all axes, grids, objects, and text.
- Export or convert the final figure into a storage-efficient `.webp` file (e.g., via Matplotlib/Pillow `savefig(..., format="webp", dpi=150, pil_kwargs={"quality": 85})`, `cwebp -q 85`, or `ffmpeg -c:v libwebp -quality 85`) inside `tempp/FigureGenerationDraft/`.

## Workflow
1. Write the figure-generation script (e.g., Python with Matplotlib or Manim static frame `-s`) in `tempp/FigureGenerationDraft/`.
2. Execute the script to render the figure and fix any syntax or runtime errors.
3. Ensure the final image is saved as a storage-efficient `.webp` file inside `tempp/FigureGenerationDraft/`.
4. Ask the user to review the generated figure.
- **Do NOT visually verify the output yourself** (do not inspect or read the generated image files). It is unreliable and wastes tokens.

---

# Task
<!-- Describe the figure to generate below -->
