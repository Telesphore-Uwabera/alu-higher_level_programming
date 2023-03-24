#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves them to a JSON file"""

import sys
import os.path
from typing import List
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_item(args: List[str]) -> None:
    """Adds all arguments to a Python list and saves them to a JSON file"""
    filename = 'add_item.json'
    if os.path.isfile(filename):
        items = load_from_json_file(filename)
    else:
        items = []
    items.extend(args)
    save_to_json_file(items, filename)

if __name__ == "__main__":
    args = sys.argv[1:]
    add_item(args)
