import argparse


def get_cli_args():
    parser = argparse.ArgumentParser(
        description="Codebase Analyzer Tool"
    )

    parser.add_argument(
        "path",
        help="Path of the project to analyze"
    )

    parser.add_argument(
        "--report",
        help="Generate analysis report to a text file",
        default=None
    )

    return parser.parse_args()
