"""
Utility
=======

A set of utility functions for bubbleZ

"""

__all__ = ['FileAlreadyExists',]


# Define Error class for wrong shapes
class FileAlreadyExists(Exception):
    """
    A filename already exists in a specific directory.

    """

    pass