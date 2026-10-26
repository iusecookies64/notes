# Environment & Files
- Use the `manim` conda environment (Python 3.11, Manim Community, LaTeX, and ffmpeg installed). Run commands via `conda run -n manim <command>` or after `conda activate manim`.
- Put **all** code files, intermediate build/media files, and final output videos inside `tempp/ManimationDraft/`. Run Manim from inside `tempp/ManimationDraft/` (or pass `--media_dir tempp/ManimationDraft/media`) so nothing is generated outside this folder.

# Theme & Resolution
- Use a dark theme: set `config.background_color = "#121212"` and use light, high-contrast colors for all objects and text.
- Render at **720p** resolution (`1280x720`, 30 fps — e.g., `manim -qm` or `-r 1280,720 --fps 30`).

# Workflow
1. Write the Manim script in `tempp/ManimationDraft/`.
2. Compile the script to video and fix any syntax or runtime errors.
3. Convert the rendered video into a storage-efficient `.webm` file (e.g. VP9 with `ffmpeg -c:v libvpx-vp9 -b:v 0 -crf 36 -an`) inside `tempp/ManimationDraft/`.
4. Ask the user to review the rendered video.
- **Do NOT visually verify the output yourself** (do not extract frames or inspect images/video). It is unreliable and wastes tokens.
