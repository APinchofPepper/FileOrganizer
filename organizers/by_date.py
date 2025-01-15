import os
import shutil
from datetime import datetime
from utils.logger import log_action

def run(directory):
    """Organize files in the given directory by modification date."""
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isdir(file_path):
            continue

        # Use modification time instead of creation time
        mod_time = os.path.getmtime(file_path)
        date_folder = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')
        folder_path = os.path.join(directory, date_folder)
        os.makedirs(folder_path, exist_ok=True)

        try:
            shutil.move(file_path, os.path.join(folder_path, filename))
            log_action("Moved", f"{file_path} -> {folder_path}")
        except Exception as e:
            log_action("Error", f"Failed to move {file_path}: {e}")

    print("Files organized by date!")
