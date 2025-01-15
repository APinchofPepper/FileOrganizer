import os
import tempfile
from organizers.by_size import run

def test_by_size():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test files with specific sizes
        small_file = os.path.join(temp_dir, "small.txt")
        medium_file = os.path.join(temp_dir, "medium.txt")
        large_file = os.path.join(temp_dir, "large.txt")
        huge_file = os.path.join(temp_dir, "huge.txt")

        # Write content to files to match size categories
        with open(small_file, "wb") as f:
            f.write(b"A" * 1024)  # 1 KB (Small)
        with open(medium_file, "wb") as f:
            f.write(b"A" * (10 * 1024 * 1024))  # 10 MB (Medium)
        with open(large_file, "wb") as f:
            f.write(b"A" * (50 * 1024 * 1024))  # 50 MB (Large)
        with open(huge_file, "wb") as f:
            f.write(b"A" * (200 * 1024 * 1024))  # 200 MB (Huge)

        # Run the organizer
        run(temp_dir)

        # Define the expected directories
        small_dir = os.path.join(temp_dir, "Small")
        medium_dir = os.path.join(temp_dir, "Medium")
        large_dir = os.path.join(temp_dir, "Large")
        huge_dir = os.path.join(temp_dir, "Huge")

        # Assert directories were created
        assert os.path.exists(small_dir), f"Folder {small_dir} not created."
        assert os.path.exists(medium_dir), f"Folder {medium_dir} not created."
        assert os.path.exists(large_dir), f"Folder {large_dir} not created."
        assert os.path.exists(huge_dir), f"Folder {huge_dir} not created."

        # Assert files are in correct directories
        assert os.path.exists(os.path.join(small_dir, "small.txt")), "small.txt not moved to Small folder."
        assert os.path.exists(os.path.join(medium_dir, "medium.txt")), "medium.txt not moved to Medium folder."
        assert os.path.exists(os.path.join(large_dir, "large.txt")), "large.txt not moved to Large folder."
        assert os.path.exists(os.path.join(huge_dir, "huge.txt")), "huge.txt not moved to Huge folder."

        print("Test passed: Files organized by size correctly.")

if __name__ == "__main__":
    test_by_size()
