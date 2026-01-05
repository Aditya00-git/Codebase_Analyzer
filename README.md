CODEBASE ANALYZER TOOL (PYTHON CLI)

------------------------------------------------------------
PROJECT OVERVIEW
------------------------------------------------------------
The Codebase Analyzer Tool is a Python-based command-line application designed to
analyze the structure and content of any software project directory. It provides
useful insights into file organization, code size, language usage, and basic file
health metrics.

The tool is intentionally built without machine learning or complex frameworks,
focusing instead on clean logic, readability, and real-world developer utility.


------------------------------------------------------------
KEY FEATURES
------------------------------------------------------------
- Recursive scanning of project directories
- Total file and folder count
- Line of code analysis (total, empty, and code lines)
- Programming language detection using file extensions
- Identification of empty and very small files
- Detection of largest files in the project
- Command-line interface (CLI) usage
- Optional generation of a detailed text report


------------------------------------------------------------
TECHNOLOGIES USED
------------------------------------------------------------
- Python (standard library only)
- os
- argparse

No external dependencies are required.


------------------------------------------------------------
PROJECT STRUCTURE
------------------------------------------------------------
codebase_analyzer/
|
├── analyzer/
│   ├── scanner.py            -> Scans directories and files
│   ├── file_stats.py         -> File and folder statistics
│   ├── line_counter.py       -> Line counting logic
│   ├── language_detector.py  -> Language detection
│   ├── empty_finder.py       -> Empty and small file detection
│
├── cli/
│   ├── args.py               -> CLI argument parsing
│   ├── commands.py           -> CLI execution logic
│
├── reports/
│   ├── report_writer.py      -> Text report generation
│
├── analyze.py                -> Entry point for the tool
├── constants.py              -> Shared constants
├── requirements.txt
└── README.txt


------------------------------------------------------------
HOW THE TOOL WORKS
------------------------------------------------------------
1. The user provides a project path via the command line.
2. The scanner module recursively traverses the directory structure.
3. Individual analyzer modules compute statistics such as:
   - File and folder counts
   - Line counts
   - Language distribution
   - Empty and small files
4. Results are displayed in the terminal.
5. Optionally, a structured text report is generated.


------------------------------------------------------------
INSTALLATION
------------------------------------------------------------
1. Clone or download the project folder.
2. Navigate to the project directory.
3. Ensure Python 3 is installed.

No additional installation steps are required.


------------------------------------------------------------
USAGE
------------------------------------------------------------

Basic analysis (terminal output only):
python analyze.py <project_path>

Example:
python analyze.py .

Generate analysis report:
python analyze.py <project_path> --report report.txt

Example:
python analyze.py . --report analysis_report.txt


------------------------------------------------------------
OUTPUT DETAILS
------------------------------------------------------------
Terminal Output:
- Summary of files, folders, and lines
- Language usage statistics

Text Report:
- Complete breakdown of analysis results
- Suitable for documentation or sharing


------------------------------------------------------------
CONCLUSION
------------------------------------------------------------
The Codebase Analyzer Tool demonstrates strong software engineering fundamentals,
including modular design, CLI development, and clean code practices. It is a
lightweight yet powerful utility suitable for real-world usage and professional
showcase.


------------------------------------------------------------
AUTHOR
------------------------------------------------------------
Aditya Seswani
