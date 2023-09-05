#!/usr/bin/python3
def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize a flag to indicate if a new line is needed
    new_line_needed = True

    # Iterate through each character in the text
    for char in text:
        # Print the character without adding a new line
        print(char, end="")

        # Check if a new line is needed
        if char in ".?:\n":
            new_line_needed = True
        elif char != " ":
            new_line_needed = False

        # Add two new lines if needed
        if new_line_needed:
            print("\n")
            new_line_needed = False
