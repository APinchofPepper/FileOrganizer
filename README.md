# File Organizer

A Python-based utility to organize files in a directory by various criteria such as file type, creation date, file size, or custom rules. This tool is designed for convenience and can handle a wide variety of file organization needs.

---

## Features

- Organize files by:
  - **File Type**: Groups files into folders based on their extensions (e.g., .txt, .jpg).
  - **Date**: Groups files into folders based on their creation or modification date.
  - **File Size**: Categorizes files into Small, Medium, Large, and Huge folders.
  - **Custom Rules**: Apply user-defined rules (e.g., by name pattern or specific extensions).
- Logs all actions to a dedicated log file (`logs/organizer.log`).
- Cross-platform support (Linux, macOS, Windows).
- Simple and modular structure for easy extension.

---

## Installation

### Prerequisites
- Python 3.7 or higher
- Recommended: Set up a virtual environment

### Clone the Repository
```bash
git clone https://github.com/APinchofPepper/FileOrganizer.git
cd FileOrganizer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Running the Organizer
1. Navigate to the project root directory:
```bash
cd file-organizer
```

2. Run the main script:
```bash
python main.py
```

3. Follow the prompts to:
   * Select an organization method.
   * Specify the directory you want to organize.

### Example
**Before Organizing**
```
/example_directory/
├── file1.txt
├── file2.jpg
├── file3.pdf
└── file4
```

**After Organizing by File Type**
```
/example_directory/
├── txt/
│   └── file1.txt
├── jpg/
│   └── file2.jpg
├── pdf/
│   └── file3.pdf
└── no_extension/
    └── file4
```

## Testing
Run the tests to ensure everything works correctly:
```bash
pytest tests/
```

## Project Structure
```
file-organizer/
├── main.py                 # Main script to run the organizer
├── organizers/             # Modules for different organization methods
│   ├── __init__.py
│   ├── by_file_type.py
│   ├── by_date.py
│   ├── by_size.py
│   └── custom_rules.py
├── utils/                  # Utility functions and logging
│   ├── __init__.py
│   ├── file_utils.py
│   └── logger.py
├── logs/                   # Log files
│   └── organizer.log
├── tests/                  # Unit tests for each module
│   ├── __init__.py
│   ├── test_by_file_type.py
│   ├── test_by_date.py
│   └── test_by_size.py
├── LICENSE.md              # License information
└── README.md               # Project documentation
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and submit a pull request.

## License
This project is licensed under the MIT License. See `LICENSE.md` for more details.

## Acknowledgments
* Inspiration for the project: File organization struggles!
* Python's standard libraries (`os`, `shutil`) for making file handling easy.