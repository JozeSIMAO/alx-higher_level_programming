#!/usr/bin/python3
"""defines a class Rectangle"""


class Rectangle:
    """represents a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return (0)
        return (2 * (self.width + self.height))

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ("")
        rectangle = "#"
        for i in range(self.__height):
            rectangle += str(self.print_symbol) * self.__width
            if i < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
