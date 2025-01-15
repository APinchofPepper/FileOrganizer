import os
import tempfile
from organizers.by_file_type import run

def test_by_file_type():
    """Test the by_file_type organizer."""
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test files with different extensions
        file_txt = os.path.join(temp_dir, "file1.txt")
        file_jpg = os.path.join(temp_dir, "file2.jpg")
        file_pdf = os.path.join(temp_dir, "file3.pdf")
        file_no_ext = os.path.join(temp_dir, "file4")  # No extension

        # Write content to the files
        open(file_txt, "w").close()
        open(file_jpg, "w").close()
        open(file_pdf, "w").close()
        open(file_no_ext, "w").close()

        # Run the organizer
        run(temp_dir)

        # Define expected directories
        txt_dir = os.path.join(temp_dir, "txt")
        jpg_dir = os.path.join(temp_dir, "jpg")
        pdf_dir = os.path.join(temp_dir, "pdf")
        no_ext_dir = os.path.join(temp_dir, "no_extension")

        # Assert directories were created
        assert os.path.exists(txt_dir), f"Folder {txt_dir} not created."
        assert os.path.exists(jpg_dir), f"Folder {jpg_dir} not created."
        assert os.path.exists(pdf_dir), f"Folder {pdf_dir} not created."
        assert os.path.exists(no_ext_dir), f"Folder {no_ext_dir} not created."

        # Assert files are in correct directories
        assert os.path.exists(os.path.join(txt_dir, "file1.txt")), "file1.txt not moved to txt folder."
        assert os.path.exists(os.path.join(jpg_dir, "file2.jpg")), "file2.jpg not moved to jpg folder."
        assert os.path.exists(os.path.join(pdf_dir, "file3.pdf")), "file3.pdf not moved to pdf folder."
        assert os.path.exists(os.path.join(no_ext_dir, "file4")), "file4 (no extension) not moved to no_extension folder."

        print("Test passed: Files organized by file type correctly.")

if __name__ == "__main__":
    test_by_file_type()
