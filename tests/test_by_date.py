import os
import time
import shutil
import tempfile
from organizers.by_date import run

def test_by_date():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create temporary files with specific creation times
        file1_path = os.path.join(temp_dir, "file1.txt")
        file2_path = os.path.join(temp_dir, "file2.txt")
        file3_path = os.path.join(temp_dir, "file3.txt")

        # Create files
        with open(file1_path, "w") as f:
            f.write("Test file 1")
        with open(file2_path, "w") as f:
            f.write("Test file 2")
        with open(file3_path, "w") as f:
            f.write("Test file 3")

        # Set creation times (simulated for testing)
        time_now = time.time()
        time_past = time_now - (86400 * 2)  # 2 days ago
        os.utime(file1_path, (time_past, time_past))
        os.utime(file2_path, (time_now, time_now))
        os.utime(file3_path, (time_now, time_now))

        # Run the organizer
        run(temp_dir)

        # Check that files are moved to the correct date-based folders
        date_past_folder = os.path.join(temp_dir, time.strftime('%Y-%m-%d', time.localtime(time_past)))
        date_now_folder = os.path.join(temp_dir, time.strftime('%Y-%m-%d', time.localtime(time_now)))

        # Assert folders were created
        assert os.path.exists(date_past_folder), f"Folder for past date {date_past_folder} not created."
        assert os.path.exists(date_now_folder), f"Folder for current date {date_now_folder} not created."

        # Assert files are in correct folders
        assert os.path.exists(os.path.join(date_past_folder, "file1.txt")), "file1.txt not moved to correct folder."
        assert os.path.exists(os.path.join(date_now_folder, "file2.txt")), "file2.txt not moved to correct folder."
        assert os.path.exists(os.path.join(date_now_folder, "file3.txt")), "file3.txt not moved to correct folder."

        print("Test passed: Files organized by date correctly.")

if __name__ == "__main__":
    test_by_date()
