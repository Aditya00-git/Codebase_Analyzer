from analyzer.scanner import scan_project
from analyzer.file_stats import get_file_and_folder_count, get_largest_files
from analyzer.line_counter import count_lines
from analyzer.language_detector import detect_languages
from analyzer.empty_finder import find_empty_and_small_files
from reports.report_writer import write_report


def run_analysis(project_path, report_path=None):
    files, folders = scan_project(project_path)

    total_files, total_folders = get_file_and_folder_count(files, folders)
    total_lines, empty_lines, code_lines = count_lines(files)
    languages = detect_languages(files)
    empty_files, small_files = find_empty_and_small_files(files)
    largest_files = get_largest_files(files)

    # Print summary to terminal
    print("\nCODEBASE SUMMARY")
    print("-" * 20)
    print("Total files:", total_files)
    print("Total folders:", total_folders)
    print("Total lines:", total_lines)
    print("Code lines:", code_lines)

    print("\nLanguages used:")
    for lang, count in languages.items():
        print(" ", lang, ":", count)

    data = {
        "total_files": total_files,
        "total_folders": total_folders,
        "total_lines": total_lines,
        "empty_lines": empty_lines,
        "code_lines": code_lines,
        "languages": languages,
        "largest_files": largest_files,
        "empty_files": empty_files,
        "small_files": small_files
    }

    if report_path:
        write_report(report_path, data)
        print("\nReport generated at:", report_path)
