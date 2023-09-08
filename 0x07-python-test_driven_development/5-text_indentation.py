#!/usr/bin/python3
# text_indentation.py
"""defines a text indentation function

This module provides a function, text_indentation, which takes a text string as input and
prints the text with two new lines after each '.', '?', and ':' characters.

Example:
    text = "Hello. This is a sample text: It has multiple sentences. Is it working?"
    text_indentation(text)
    
    Output:
    Hello.
    
    This is a sample text:
    
    It has multiple sentences.
    
    Is it working?

Args:
    text (str): The input text to be formatted.

Raises:
    TypeError: If text is not a string.
"""

def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text: text to print
    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    char = 0
    while char < len(text) and text[char] == ' ':
        char += 1

    while char < len(text):
        print(text[char], end="")
        if text[char] == "\n" or text[char] in ".?:":
            if text[char] in ".?:":
                print("\n")
            char += 1
            while char < len(text) and text[char] == ' ':
                char += 1
            continue
        char += 1

