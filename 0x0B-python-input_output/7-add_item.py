#!/usr/bin/python3
"""
This program takes arguments and adds them to a Python list,
then saves the list as a JSON representation in a file named add_item.json.
If the file doesn't exist, it will be created.
"""

from sys import argv
from os.path import exists
import json

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

namefile = "add_item.json"
argc = len(argv)

file_list = []

if exists(namefile):
    file_list = load_from_json_file(namefile)

file_list.extend(argv[1:])
save_to_json_file(file_list, namefile)
