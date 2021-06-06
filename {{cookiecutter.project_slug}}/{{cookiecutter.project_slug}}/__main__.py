"""{{cookiecutter.project_slug}}.__main__

support calling `python -m {{cookiecutter.project_slug}}`
"""
import sys
from typing import List


def main(argv: List[str]) -> int:
    print("{{cookiecutter.project_slug}} commandline placeholder:")
    print("[input_argv]", argv)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
