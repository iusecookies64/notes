# General Agent Guidelines

This document defines the core operating principles, workspace boundaries, and scripting policies for AI agents.

---

## 1. Direct Execution & Scope Boundaries

- **Jump Straight to the Task:** Begin working on the user's explicit request immediately without unnecessary preamble or broad repository reconnaissance, unless the task inherently requires cross-project architectural understanding or interface discovery.
- **No Unsolicited Exploration:** Do **not** browse, list, search, or read files and directories that were not mentioned by the user or are not directly required to complete the task. However, tracing dependencies/imports, inspecting error traces, and locating relevant source files during debugging or feature work are considered directly required.
- **Use Native Tools First:** Always use built-in agent tools (such as `read_file`, `edit_file`, `write_file`) for reading source documents, viewing PDFs/images, and writing or editing content.

---

## 2. Scripting & Shell Execution Policy

Scripts and shell commands must **never** be used as a crutch for routine reading or post-hoc checking, but **should** be used when they prevent massive token waste on purely mechanical file operations.

### 2.1 Strictly Prohibited Scripting (Do NOT Do This)
1. **No Ad-Hoc Formatting Verification Scripts:**
   - Do **not** write or execute throwaway Python, regex, or shell scripts to verify Markdown structure, LaTeX delimiters, heading hierarchies, or callout formatting after writing or editing notes. Adhere strictly to formatting guidelines during generation.
   - *(Note: Standard project build tools, compilers, linters, and test suites—such as `pytest`, `eslint`, `tsc`, `ruff`, or `cargo test` in software repositories—remain encouraged when verifying code changes).*
2. **No File-Exploration or Document-Parsing Scripts:**
   - Do **not** run shell commands or Python scripts to explore the directory tree, inspect file lengths/contents, or extract text/images from PDFs when native reading tools can handle them directly.

### 2.2 High-Efficiency Mechanical Operations (When to Use or Propose Scripts)
1. **Bulk File Concatenation, Splicing, and Splitting:**
   - When a workflow requires purely mechanical manipulation of large text blocks—such as **concatenating multiple large files** (e.g., combining ~1,000-line sections written by subagents into a single coherent file), **splicing pre-written files together**, or **splitting a large file at known line boundaries**—do **not** manually read and re-generate thousands of lines through LLM output tokens.
   - In these high-leverage cases where a short script or shell command (`cat`, `sed`, `head`/`tail`, or a 5-line Python script) will save substantial time and token usage:
     - **Run the concise command/script directly** if it is a safe, deterministic mechanical step (like concatenating completed subagent section files into the final target file), **or ask the user first** if there is any ambiguity.
     - Clean up any temporary helper scripts or intermediate files immediately after the operation succeeds.
