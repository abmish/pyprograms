"""
Define a custom exception class which takes a string message as attribute.
"""

class CustomError(Exception):
    """
    User defined exception class
    Attributes:
        desc -- description of the error
    """
    def __init__(self, desc):
        self.desc = desc

custom_error = CustomError("user defined error")
