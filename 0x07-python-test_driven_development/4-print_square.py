#!/usr/bin/python3
# 4-print_square.py
"""Defines a square printing function."""


def print_square(size):
    """Prints a square with the # character.
    Args:
        size (int): The heights/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValeError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
