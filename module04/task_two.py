"""Count words in a UTF-8 text file."""

import string


def count_words(filename):
    """Return the word count, or None if the file does not exist."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        return None

    # Treat ASCII punctuation as word separators.
    for mark in string.punctuation:
        text = text.replace(mark, " ")

    return len(text.split())


filename = "The_Zen_of_Python.txt"
number_of_words = count_words(filename)

print(f"File: {filename}")
print(f"Number of words: {number_of_words}")