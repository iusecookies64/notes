import sys
import re
from pathlib import Path

def reformat_math_blocks(content: str) -> str:
    # Pattern to match $$...$$ math blocks
    pattern = r"\$\$(.*?)\$\$"

    def replace_match(match):
        math_content = match.group(1).strip()
        if not math_content:
            return "$$\n$$"
        return f"\n$$\n{math_content}\n$$\n"

    # Convert all $$...$$ blocks to multi-line format
    updated = re.sub(pattern, replace_match, content, flags=re.DOTALL)
    
    # Clean up any excessive empty lines created around the blocks
    return re.sub(r"\n{3,}", "\n\n", updated)

def process_path(target_path: Path):
    if target_path.is_file() and target_path.suffix.lower() == ".md":
        files = [target_path]
    elif target_path.is_dir():
        files = list(target_path.rglob("*.md"))
    else:
        print(f"Error: {target_path} is not a valid Markdown file or directory.")
        return

    for file_path in files:
        content = file_path.read_text(encoding="utf-8")
        formatted_content = reformat_math_blocks(content)
        file_path.write_text(formatted_content, encoding="utf-8")
        print(f"Processed: {file_path}")

if __name__ == "__main__":
    path = "/home/iusecookies64/Desktop/Tushar/notes/content/Core CS/COA/DDCA Onur Mutlu/04. Sequential Logic Design II — Finite State Machines.md"

    process_path(Path(path))