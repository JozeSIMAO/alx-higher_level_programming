#!/usr/bin/python3
"""defines a function that prints a text with 2 new lines"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters.

        Args:
            text: must be a string, otherwise raise  a TypeError
            exception with the message text "must be a string"

        raises:
            TypeError: exception

        return: a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines = []
    for char in text:
        if char in ['.', '?', ':']:
            lines.append(char + '\n\n')
        else:
            if not lines or lines[-1].endswith('\n'):
                lines.append(char)
            else:
                lines[-1] += char

    for line in lines:
        print(line, end='')
