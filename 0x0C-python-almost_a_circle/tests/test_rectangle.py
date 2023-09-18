#!/usr/bin/python3
"""unittest for the Rectangle class"""


import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_constructor(self):
        r = Rectangle(4, 5, 1, 2, 42)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 42)

    def test_area(self):
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test_display(self):
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        r = Rectangle(4, 5, 1, 2, 42)
        expected_str = "[Rectangle] (42) 1/2 - 4/5"
        self.assertEqual(str(r), expected_str)

    def test_update(self):
        r = Rectangle(4, 5, 1, 2, 42)
        r.update(1, 6, 7, 8, 9)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 8)
        self.assertEqual(r.y, 9)

if __name__ == '__main__':
    unittest.main()

