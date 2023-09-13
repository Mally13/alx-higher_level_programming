#!/usr/bin/python3
# 5-to_json_string.py

"""Defines a string-to-JSON function"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of a string object(string)"""
    return json.dumps(my_obj)
