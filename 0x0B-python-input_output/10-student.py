#!/usr/bin/python3
"""defines a class Student"""


class Student:
    """represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new studenet

        Args:
            first_name (str): first name of student
            last_nmae (str): last name of student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """gets a dictionary representation of the student

        if attrs is a  list of strings, only attribute names contained
        in this list must be retrieved

        Args:
            attrs (list): is a list of strings
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return ({k: getattr(self, k) for k in attrs if hasattr(self, k)})
        return (self.__dict__)
