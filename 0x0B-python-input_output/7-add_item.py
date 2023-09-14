#!/usr/bin/python3
# 7-add_item.py
"""a script that adds all arguments to a Python list,
and then save them to a file"""
import sys


if __name__ == "__main__":
    """adds all arguments to a Python list, and saves to a file"""
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    filename = "add_item.json"

    try:
        item_list = load_from_json_file(filename)
    except FileNotFoundError:
        item_list = []

    for arg in sys.argv[1:]:
        item_list.append(arg)
    save_to_json_file(item_list, filename)
