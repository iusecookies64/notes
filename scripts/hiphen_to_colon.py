import os
from pathlib import Path


def rename_colons_to_hyphens(target_directory: str, dry_run: bool = True) -> None:
    """Recursively renames files with ':' to '-' in target_directory.

    :param target_directory: Root directory path to scan.
    :param dry_run: If True, prints proposed changes without modifying files.
    """
    root_path = Path(target_directory).expanduser().resolve()

    if not root_path.is_dir():
        print(f"Error: Directory '{root_path}' does not exist.")
        return

    renamed_count = 0
    skipped_count = 0

    # topdown=False traverses bottom-up to prevent invalid path references
    for dirpath, _, filenames in os.walk(root_path, topdown=False):
        current_dir = Path(dirpath)

        for filename in filenames:
            if ":" not in filename:
                continue

            old_file_path = current_dir / filename
            new_filename = filename.replace(":", "-")
            new_file_path = current_dir / new_filename

            # Guard against overwriting an existing file
            if new_file_path.exists():
                print(f"[SKIPPED] Collision detected: '{new_file_path.name}' already exists.")
                skipped_count += 1
                continue

            if dry_run:
                print(f"[DRY RUN] {old_file_path.name}  ->  {new_filename}")
            else:
                old_file_path.rename(new_file_path)
                print(f"[RENAMED] {old_file_path.name}  ->  {new_filename}")

            renamed_count += 1

    mode_label = "Dry run complete" if dry_run else "Operation complete"
    print(f"\n{mode_label}: {renamed_count} files flagged/renamed, {skipped_count} skipped.")


if __name__ == "__main__":
    # 1. Set your target directory path
    DIRECTORY_TO_CLEAN = "/home/iusecookies64/Desktop/Tushar/notes/content"

    # 2. Run in dry_run=True first to verify matches
    #    Change to dry_run=False when ready to execute
    rename_colons_to_hyphens(DIRECTORY_TO_CLEAN, dry_run=False)