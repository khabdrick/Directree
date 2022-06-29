import argparse
import pathlib
import sys

from . import __version__
from .tree import Directree

def main():
    args = parse_cmd_line_arguments()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("The specified root directory doesn't exist")
        sys.exit()
    tree = Directree(root_dir, dir_only=args.dir_only)
    tree.generate_tree()

def parse_cmd_line_arguments():
    parser = argparse.ArgumentParser(
        prog="tree",
        description="Directree is a directory tree generator",
        epilog="Good luck!",
    )
    parser.version = f"Directree v{__version__}"
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
        "root_dir",
        metavar="ROOT_DIR",
        nargs="?",
        default=".",
        help="Generate a full directory tree starting at ROOT_DIR",
    )
    parser.add_argument(
        "-d",
        "--dir-only",
        action="store_true",
        help="Generate a directory-only tree",
    )
    return parser.parse_args()