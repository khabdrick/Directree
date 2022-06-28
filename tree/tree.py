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

    def generate(self):
        tree = self._generator.build_tree()
        for entry in tree:
            print(entry)