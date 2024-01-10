#!/usr/bin/python3
"""
This program takes command-line arguments, adds them to a Python list,
then saves the list as a JSON representation in a file named add_item.json.
If the file doesn't exist, it will be created.
"""

import sys
import json
from os.path import exists

def save_to_json_file(my_obj, filename):
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)

def load_from_json_file(filename):
    if exists(filename):
        with open(filename, mode='r', encoding='utf-8') as file:
            return json.load(file)
    return []

def main():
    namefile = "add_item.json"
    argc = len(sys.argv)

    file_list = load_from_json_file(namefile)

    if argc > 1:
        file_list.extend(sys.argv[1:])
        save_to_json_file(file_list, namefile)
    
    print(file_list)

if __name__ == "__main__":
    main()
