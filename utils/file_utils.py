import shutil
from utils.logger import log_action
import os

def safe_move(src, dest):
    """Move files safely, handling duplicates."""
    try:
        shutil.move(src, dest)
        log_action("Moved", f"{src} -> {dest}")
    except shutil.Error:
        base, ext = os.path.splitext(dest)
        new_dest = f"{base}_copy{ext}"
        safe_move(src, new_dest)
    except Exception as e:
        log_action("Error", f"Failed to move {src}: {e}")
