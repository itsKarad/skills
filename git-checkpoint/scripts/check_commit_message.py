#!/usr/bin/env python3
"""Validate a commit title, either directly or as a Git commit-msg hook."""

import argparse
from pathlib import Path
import re
import sys


PREFIXES = ("feat", "fix", "refactor", "docs", "test", "perf", "build", "ci", "chore")
TITLE_PATTERN = re.compile(r"^(?:" + "|".join(PREFIXES) + r"): \S")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("message_file", nargs="?", type=Path, help="Git commit message file")
    source.add_argument("--message", help="Commit message to check directly")
    args = parser.parse_args()

    if args.message_file is not None:
        try:
            message = args.message_file.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            parser.error("Could not read the commit message file as UTF-8.")
    else:
        message = args.message

    lines = message.splitlines()
    if lines and TITLE_PATTERN.match(lines[0]):
        return 0

    print(
        "Invalid commit title. Use type: summary with a nonempty summary.\n"
        "Allowed types: " + ", ".join(PREFIXES) + ".\n"
        "Example: fix: validate checkpoint commit messages",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
