import os
from collections import defaultdict
from pathlib import Path

def analyze_directory(directory_path):
    target_dir = Path(directory_path)
    if not target_dir.is_dir():
        print(f"Error: '{directory_path}' is not a valid directory.")
        return

    # Store total size and count for each extension
    extension_data = defaultdict(lambda: {"size": 0, "count": 0})
    total_size = 0
    total_files = 0

    print(f"Scanning directory: {target_dir.resolve()}\n")

    # Walk through all files in the directory and subdirectories
    for root, _, files in os.walk(target_dir):
        for file in files:
            file_path = Path(root) / file
            try:
                # Protect against broken symlinks
                if file_path.is_file() and not file_path.is_symlink():
                    file_size = file_path.stat().st_size
                    
                    # Group by lower-case extensions (e.g., merge .PNG and .png)
                    ext = file_path.suffix.lower()
                    if not ext:
                        ext = "[No Extension]"
                        
                    extension_data[ext]["size"] += file_size
                    extension_data[ext]["count"] += 1
                    total_size += file_size
                    total_files += 1
            except Exception:
                # Silently skip files that are locked or lack permissions
                pass

    # Helper function to convert raw bytes into readable units
    def format_size(size_in_bytes):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_in_bytes < 1024.0:
                return f"{size_in_bytes:.2f} {unit}"
            size_in_bytes /= 1024.0
        return f"{size_in_bytes:.2f} PB"

    # Sort results by size descending
    sorted_extensions = sorted(extension_data.items(), key=lambda item: item[1]["size"], reverse=True)

    # Print the resulting breakdown table
    print(f"{'Extension':<15} | {'File Count':<10} | {'Total Size':<15}")
    print("-" * 46)
    for ext, data in sorted_extensions:
        print(f"{ext:<15} | {data['count']:<10} | {format_size(data['size']):<15}")
        
    print("-" * 46)
    print(f"{'TOTAL':<15} | {total_files:<10} | {format_size(total_size):<15}")

if __name__ == "__main__":
    folder_to_scan = "/home/iusecookies64/Desktop/Tushar/notes/content"
    analyze_directory(folder_to_scan)
