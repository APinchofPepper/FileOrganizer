import os
import shutil
import re
from utils.logger import log_action

# Example: Custom rules defined as a dictionary
# Key: Folder name, Value: Regex pattern to match filenames
CUSTOM_RULES = {
    "Images": r".*\.(jpg|jpeg|png|gif)$",
    "Documents": r".*\.(docx|pdf|txt)$",
    "Code": r".*\.(py|js|html|css)$"
}

def match_rule(filename):
    """Match a filename against custom rules."""
    for folder, pattern in CUSTOM_RULES.items():
        if re.match(pattern, filename, re.IGNORECASE):
            return folder
    return "Uncategorized"

def run(directory):
    """Organize files in the given directory by custom rules."""
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isdir(file_path):
            continue

        folder = match_rule(filename)
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)

        try:
            shutil.move(file_path, os.path.join(folder_path, filename))
            log_action("Moved", f"{file_path} -> {folder_path}")
        except Exception as e:
            log_action("Error", f"Failed to move {file_path}: {e}")

    print("Files organized by custom rules!")
