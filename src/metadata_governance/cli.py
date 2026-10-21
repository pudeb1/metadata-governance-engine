"""Minimal CLI for checking the package installation."""
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Metadata Governance Engine")
    parser.add_argument("--version", action="store_true", help="Print package version")
    args = parser.parse_args()
    if args.version:
        print("mge 0.1.0")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
