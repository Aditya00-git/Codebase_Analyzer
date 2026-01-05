from cli.args import get_cli_args
from cli.commands import run_analysis


def main():
    args = get_cli_args()
    run_analysis(args.path, args.report)


if __name__ == "__main__":
    main()
