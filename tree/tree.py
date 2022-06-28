"""This module provides Directree main module."""

import os
import pathlib

# initialise characters that is used to visualizethe directory tree
PIPE = "┃"
L = "┗━ 🌿"
HAMMER = "┣━ 🌿"
PIPE_SPACE = "┃   "
SPACE = "    "

class Directree:
    def __init__(self, root_dir):
        self._tree_generator = _Generator(root_dir)

    def generate_tree(self):
        tree = self._tree_generator.grow_tree()
        for data in tree:
            print(data)

class _Generator:
    """Generates the Directory tree"""
    def __init__(self, root_dir):
        self._root_dir = pathlib.Path(root_dir)
        self._tree = []

    def grow_tree(self):
        self._tree_head()
        self._tree_body(self._root_dir)
        return self._tree

    def _tree_head(self):
        """Generate directory tree head"""
        self._tree.append(f"{self._root_dir}{os.sep}")
        self._tree.append(PIPE)

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