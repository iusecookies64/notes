# Task
Write a Manim Community animation from the description below, render it, and produce a storage-efficient `.webm` video. Run everything yourself and fix any errors until the final video exists and has been checked.

# Animation description
<DESCRIPTION>
(Paste the full spec here: the scene setup, the numbered steps, what should be highlighted, and any labels or math to show.)
</DESCRIPTION>

# Environment
- Use the conda env named `manim` (Python 3.11, Manim Community already installed, LaTeX and ffmpeg available).
- Activate it with `conda activate manim`. If activation doesn't work in your shell, use `conda run -n manim <command>`.
- Always invoke Manim as `python -m manim ...`, not bare `manim`, because the plain command was not on PATH in this setup.
- Check the Manim version with `python -m manim --version` and write code that matches it. Don't assume names from older releases.
- Work in a new folder named after the animation, e.g. `./<animation_name>/`. Put the script there as `<animation_name>.py` with a single Scene class.

# Requirements for the script
- Dark theme: set `config.background_color` to a dark colour such as `"#0d1117"`, and choose light, high-contrast colours for all objects and text.
- Follow the description step by step, in order. Add short on-screen captions that explain each step.
- Use `Tex`/`MathTex` for math (LaTeX is installed). Use `ThreeDScene` for 3D content.
- In 3D scenes:
  - Use `add_fixed_in_frame_mobjects` for HUD text and captions.
  - Use `add_fixed_orientation_mobjects` for labels attached to 3D points.
  - Keep geometry simple, because depth sorting of translucent surfaces is imperfect. Prefer wireframe grids and thin lines over big filled surfaces.
  - Use `always_redraw` for anything driven by a `ValueTracker`.
- Don't import rate functions by name from `from manim import *` unless you've confirmed they exist in this version. Use `rate_functions.xxx`, or an inline lambda, e.g. `lambda t: 1 - (1 - t) ** 2`.
- Total length should be roughly 20–40 seconds unless the description says otherwise. Add `self.wait()` pauses so each step can be read.
- Add a docstring at the top of the script with the render command.

# Workflow
1. Syntax-check the script with `python -m py_compile`.
2. Do a fast preview render: `python -m manim -ql <script>.py <SceneName>`. Fix all errors.
3. Verify visually. Extract a few frames from the preview, e.g. `ffmpeg -i <preview.mp4> -vf fps=1/3 frames/f_%02d.png`, and look at them. Check for these:
   - Overlapping or off-screen text.
   - Objects drawn in the wrong depth order.
   - Wrong colours.
   - Labels pointing at the wrong objects.
   - A step from the description that is missing.
   Fix anything wrong and re-preview.
4. Final render: `python -m manim -r 1280,720 --fps 30 <script>.py <SceneName>`.
5. Encode to webm with two-pass constant-quality VP9, audio removed:
   ```bash
   IN=media/videos/<script>/720p30/<SceneName>.mp4
   ffmpeg -y -i "$IN" -c:v libvpx-vp9 -b:v 0 -crf 36 -pix_fmt yuv420p