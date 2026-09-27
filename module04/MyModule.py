"""Functions for collecting numbers and finding their extrema."""


def get_a_list_of_numbers():
    """Read numbers one by one until the user types 'end'."""
    numbers = []

    while True:
        user_input = input("Enter a number, or 'end' to finish: ")
        if user_input.strip().lower() == "end":
            break
        numbers.append(float(user_input))

    return numbers


def find_min(list_of_numbers):
    """Return the smallest number, or None for an empty list."""
    if not list_of_numbers:
        return None
    return min(list_of_numbers)


def find_max(list_of_numbers):
    """Return the largest number, or None for an empty list."""
    if not list_of_numbers:
        return None
    return max(list_of_numbers)