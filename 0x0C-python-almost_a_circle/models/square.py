#!/usr/bin/python3
"""Defines a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new Square

        Args:
            size (int): size of the new square
            x (int): x coordinate of new square
            y (int): y coordinate of the square
            id (int): id of the new square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size of the square"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """returns the print and str representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Updates the attributes of the square based on *args and **kwargs

        Args:
            args (int): attributes values
            kwargs (dict): key/value pairs of attributes"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
                else:
                    break
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
