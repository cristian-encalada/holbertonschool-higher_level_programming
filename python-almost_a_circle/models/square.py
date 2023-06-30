#!/usr/bin/python3
"""Task 10"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        "String representation"
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
