#!/usr/bin/python3
# 0-read_file.py

"""Defines function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Reads a text file(utf8) and prints it to stdout"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
