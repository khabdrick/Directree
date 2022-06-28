"""This module provides Directree main module."""

import os
import pathlib

# initialise characters that is used to visualizethe directory tree
PIPE = "┃"
L = "┗━ 🌿"
HAMMER = "┣━ 🌿"
PIPE_SPACE = "┃   "
SPACE = "    "

class DirectoryTree:
    def __init__(self, root_dir):
        self._generator = _TreeGenerator(root_dir)

    def _tree_body(self, directory, prefix=""):
        """Generate directory tree diagram"""
        entries = directory.iterdir()
        entries = sorted(entries, key=lambda entry: entry.is_file())
        entries_count = len(entries)
        for index, entry in enumerate(entries):
            connector = ELBOW if index == entries_count - 1 else TEE
            if entry.is_dir():
                self._add_directory(
                    entry, index, entries_count, prefix, connector
                )
            else:
                self._add_file(entry, prefix, connector)