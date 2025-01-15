import os
import shutil
from utils.logger import log_action

def run(directory):
    """Organize files in the given directory by file type."""
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isdir(file_path):
            continue

        file_extension = filename.split('.')[-1] if '.' in filename else "no_extension"
        folder_path = os.path.join(directory, file_extension)
        os.makedirs(folder_path, exist_ok=True)

        try:
            shutil.move(file_path, os.path.join(folder_path, filename))
            log_action("Moved", f"{file_path} -> {folder_path}")
        except Exception as e:
            log_action("Error", f"Failed to move {file_path}: {e}")

    print("Files organized by file type!")
