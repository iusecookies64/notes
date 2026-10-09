import sys
from pathlib import Path
import tiktoken

# import tiktoken.model

# # Print all explicitly supported model strings
# for model_name, encoding_name in tiktoken.model.MODEL_TO_ENCODING.items():
#   print(f"Model: {model_name:<30} Encodings: {encoding_name}")


def count_tokens_in_file(file_path: str, model: str = "gpt-4o") -> int:
  # Read the file text
  path = Path(file_path)
  if not path.exists():
    raise FileNotFoundError(f"File not found: {file_path}")

  text = path.read_text(encoding="utf-8", errors="ignore")

  # Get the appropriate encoding for the model
  try:
    enc = tiktoken.encoding_for_model(model)
  except KeyError:
    enc = tiktoken.get_encoding("cl100k_base")  # Default fallback encoding

  tokens = enc.encode(text)
  return len(tokens)


if __name__ == "__main__":
  file_path = "/home/iusecookies64/Desktop/Tushar/notes/content/Mathematics/Linear Algebra (Strang)/03. The Four Fundamental Subspaces.md"
  model_name = "gpt-5"

  try:
    total_tokens = count_tokens_in_file(file_path, model_name)
    print(f"File: {file_path}")
    print(f"Model: {model_name}")
    print(f"Total Tokens: {total_tokens}")
  except Exception as e:
    print(f"Error: {e}")
