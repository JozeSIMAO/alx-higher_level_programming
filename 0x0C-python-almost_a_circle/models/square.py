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
            y (int): y coordinate of the sqare
            id (int): id of the new square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter and setter of the size of the square"""
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """returns the print and str representation of the square"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))
