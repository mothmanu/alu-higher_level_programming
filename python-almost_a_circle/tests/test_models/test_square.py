#!/usr/bin/python3
"""Unit tests for the Square class in models/square.py."""
import io
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInit(unittest.TestCase):
    """Tests for creating squares."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def test_is_rectangle(self):
        """Square inherits from Rectangle and Base."""
        s = Square(1)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)

    def test_auto_ids(self):
        """Ids go up by one when no id is given."""
        self.assertEqual(Square(1).id, 1)
        self.assertEqual(Square(1).id, 2)

    def test_given_id(self):
        """A given id is used."""
        self.assertEqual(Square(1, 0, 0, 7).id, 7)

    def test_attributes(self):
        """Width and height both equal the size."""
        s = Square(3, 1, 2)
        self.assertEqual((s.width, s.height, s.size, s.x, s.y),
                         (3, 3, 3, 1, 2))

    def test_no_new_attributes(self):
        """Square stores only the Rectangle attributes."""
        self.assertEqual(sorted(Square(2).__dict__),
                         sorted(Rectangle(2, 2, 0, 0, 1).__dict__))

    def test_missing_size(self):
        """size is required."""
        with self.assertRaises(TypeError):
            Square()

    def test_too_many_args(self):
        """Five arguments raise a TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)


class TestSquareValidation(unittest.TestCase):
    """Tests for the validation inherited from Rectangle."""

    def check(self, exc, msg, *args):
        """Assert that Square(*args) raises exc with msg."""
        with self.assertRaises(exc) as ctx:
            Square(*args)
        self.assertEqual(str(ctx.exception), msg)

    def test_size_type(self):
        """size errors use the width message."""
        for bad in ["1", 1.5, None, [1], True]:
            self.check(TypeError, "width must be an integer", bad)

    def test_size_value(self):
        """size must be greater than 0."""
        self.check(ValueError, "width must be > 0", 0)
        self.check(ValueError, "width must be > 0", -1)

    def test_x_y(self):
        """x and y are checked like in Rectangle."""
        self.check(TypeError, "x must be an integer", 1, "1")
        self.check(TypeError, "y must be an integer", 1, 0, "1")
        self.check(ValueError, "x must be >= 0", 1, -1)
        self.check(ValueError, "y must be >= 0", 1, 0, -1)

    def test_size_setter(self):
        """The size setter changes width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual((s.size, s.width, s.height), (10, 10, 10))

    def test_size_setter_validates(self):
        """The size setter uses the width error messages."""
        s = Square(5)
        with self.assertRaises(TypeError) as ctx:
            s.size = "9"
        self.assertEqual(str(ctx.exception), "width must be an integer")
        with self.assertRaises(ValueError):
            s.size = 0


class TestSquareMethods(unittest.TestCase):
    """Tests for area, display, __str__, update and to_dictionary."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def output(self, func):
        """Return what func prints."""
        buf = io.StringIO()
        with redirect_stdout(buf):
            func()
        return buf.getvalue()

    def test_area(self):
        """area returns size squared."""
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(2, 2).area(), 4)

    def test_display(self):
        """display prints the square shifted by x and y."""
        self.assertEqual(self.output(Square(2).display), "##\n##\n")
        self.assertEqual(self.output(Square(2, 1, 1).display),
                         "\n ##\n ##\n")

    def test_str(self):
        """__str__ shows id, x/y and size."""
        self.assertEqual(str(Square(5)), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(Square(3, 1, 3)), "[Square] (2) 1/3 - 3")

    def test_update_args(self):
        """update sets id, size, x and y in order."""
        s = Square(5)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")
        s.update(1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")
        s.update(1, 2, 3)
        self.assertEqual(str(s), "[Square] (1) 3/0 - 2")
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """update sets attributes from keyword arguments."""
        s = Square(5)
        s.update(x=12)
        self.assertEqual(str(s), "[Square] (1) 12/0 - 5")
        s.update(size=7, y=1)
        self.assertEqual(str(s), "[Square] (1) 12/1 - 7")
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 12/1 - 7")

    def test_update_args_beat_kwargs(self):
        """kwargs are ignored when args are given."""
        s = Square(5)
        s.update(3, size=9)
        self.assertEqual((s.id, s.size), (3, 5))

    def test_update_none_id(self):
        """Updating the id to None gives a new automatic id."""
        s = Square(1, 0, 0, 89)
        s.update(None)
        self.assertEqual(s.id, 1)

    def test_update_validates(self):
        """update runs the same checks as the setters."""
        s = Square(1)
        with self.assertRaises(TypeError):
            s.update(1, "2")
        with self.assertRaises(ValueError):
            s.update(size=-1)

    def test_to_dictionary(self):
        """to_dictionary returns id, size, x and y."""
        s = Square(10, 2, 1, 1)
        self.assertEqual(s.to_dictionary(),
                         {"id": 1, "x": 2, "size": 10, "y": 1})

    def test_to_dictionary_update(self):
        """A dictionary can copy one square's values to another."""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertNotEqual(s1, s2)


if __name__ == "__main__":
    unittest.main()
