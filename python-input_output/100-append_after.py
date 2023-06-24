#!/usr/bin/python3
"""13. Search and update
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text to a file, after each line containing
    a specific string
    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)  # Move the file pointer to the beginning
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
