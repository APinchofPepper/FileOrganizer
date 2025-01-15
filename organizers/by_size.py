import os
import shutil
from utils.logger import log_action

# Size categories in bytes
SIZE_CATEGORIES = {
    "Small": 10 * 1024,          # <= 10 KB
    "Medium": 10 * 1024 * 1024,  # > 10 KB and <= 10 MB
    "Large": 100 * 1024 * 1024,  # > 10 MB and <= 100 MB
    "Huge": float('inf')         # > 100 MB
}

def categorize_file(size):
    """Categorize file size."""
    for category, max_size in SIZE_CATEGORIES.items():
        if size <= max_size:
            return category
    return "Unknown"

def run(directory):
    """Organize files in the given directory by size."""
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isdir(file_path):
            continue

        file_size = os.path.getsize(file_path)
        category = categorize_file(file_size)
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok=True)

        try:
            shutil.move(file_path, os.path.join(folder_path, filename))
            log_action("Moved", f"{file_path} -> {folder_path}")
        except Exception as e:
            log_action("Error", f"Failed to move {file_path}: {e}")

    print("Files organized by size!")
