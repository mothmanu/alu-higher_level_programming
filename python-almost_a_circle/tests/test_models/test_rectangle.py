#!/usr/bin/python3
"""Unit tests for the Rectangle class in models/rectangle.py."""
import io
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInit(unittest.TestCase):
    """Tests for creating rectangles."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def test_is_base(self):
        """Rectangle inherits from Base."""
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_auto_ids(self):
        """Ids go up by one when no id is given."""
        self.assertEqual(Rectangle(10, 2).id, 1)
        self.assertEqual(Rectangle(2, 10).id, 2)

    def test_given_id(self):
        """A given id is used."""
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)

    def test_attributes(self):
        """All four attributes are stored."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 4))

    def test_defaults(self):
        """x and y default to 0."""
        r = Rectangle(1, 2)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_private_attributes(self):
        """The attributes are private."""
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__width
        self.assertIn("_Rectangle__width", r.__dict__)

    def test_missing_args(self):
        """Width and height are required."""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_too_many_args(self):
        """Six arguments raise a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)


class TestRectangleValidation(unittest.TestCase):
    """Tests for the validation of width, height, x and y."""

    def check(self, exc, msg, *args):
        """Assert that Rectangle(*args) raises exc with msg."""
        with self.assertRaises(exc) as ctx:
            Rectangle(*args)
        self.assertEqual(str(ctx.exception), msg)

    def test_width_type(self):
        """Width must be an integer."""
        for bad in ["1", 1.5, None, [1], {}, True, (1,)]:
            self.check(TypeError, "width must be an integer", bad, 1)

    def test_height_type(self):
        """Height must be an integer."""
        for bad in ["1", 1.5, None, [1], {}, False]:
            self.check(TypeError, "height must be an integer", 1, bad)

    def test_x_type(self):
        """x must be an integer."""
        for bad in ["1", 1.5, None, [1], {}]:
            self.check(TypeError, "x must be an integer", 1, 1, bad)

    def test_y_type(self):
        """y must be an integer."""
        for bad in ["1", 1.5, None, [1], {}]:
            self.check(TypeError, "y must be an integer", 1, 1, 0, bad)

    def test_width_value(self):
        """Width must be greater than 0."""
        self.check(ValueError, "width must be > 0", 0, 1)
        self.check(ValueError, "width must be > 0", -10, 1)

    def test_height_value(self):
        """Height must be greater than 0."""
        self.check(ValueError, "height must be > 0", 1, 0)
        self.check(ValueError, "height must be > 0", 1, -1)

    def test_x_value(self):
        """x must be 0 or more."""
        self.check(ValueError, "x must be >= 0", 1, 1, -1)

    def test_y_value(self):
        """y must be 0 or more."""
        self.check(ValueError, "y must be >= 0", 1, 1, 0, -1)

    def test_order(self):
        """Width is checked first, then height, x and y."""
        self.check(TypeError, "width must be an integer", "a", "b")
        self.check(TypeError, "height must be an integer", 1, "b", "c")
        self.check(ValueError, "width must be > 0", -1, "b")
        self.check(TypeError, "x must be an integer", 1, 1, "c", -1)

    def test_setters_validate(self):
        """The setters run the same checks."""
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10
        with self.assertRaises(TypeError):
            r.x = {}
        with self.assertRaises(ValueError):
            r.y = -1
        with self.assertRaises(TypeError):
            r.height = "3"

    def test_setters_assign(self):
        """Valid values are stored by the setters."""
        r = Rectangle(1, 1)
        r.width, r.height, r.x, r.y = 5, 6, 7, 8
        self.assertEqual((r.width, r.height, r.x, r.y), (5, 6, 7, 8))


class TestRectangleMethods(unittest.TestCase):
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
        """area returns width times height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_area_large(self):
        """area works with large numbers."""
        self.assertEqual(Rectangle(10 ** 6, 10 ** 6).area(), 10 ** 12)

    def test_area_args(self):
        """area takes no arguments."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).area(1)

    def test_display_simple(self):
        """display prints rows of #."""
        self.assertEqual(self.output(Rectangle(2, 2).display), "##\n##\n")

    def test_display_one(self):
        """A 1x1 rectangle prints a single #."""
        self.assertEqual(self.output(Rectangle(1, 1).display), "#\n")

    def test_display_x_y(self):
        """display shifts the rectangle by x and y."""
        self.assertEqual(self.output(Rectangle(2, 3, 2, 2).display),
                         "\n\n  ##\n  ##\n  ##\n")

    def test_display_x_only(self):
        """display works with only x."""
        self.assertEqual(self.output(Rectangle(3, 2, 1, 0).display),
                         " ###\n ###\n")

    def test_display_y_only(self):
        """display works with only y."""
        self.assertEqual(self.output(Rectangle(1, 1, 0, 1).display),
                         "\n#\n")

    def test_display_args(self):
        """display takes no arguments."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).display(1)

    def test_str(self):
        """__str__ shows id, x/y and width/height."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(Rectangle(5, 5, 1)),
                         "[Rectangle] (1) 1/0 - 5/5")

    def test_update_args(self):
        """update sets attributes from positional arguments in order."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """update sets attributes from keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/1")

    def test_update_args_beat_kwargs(self):
        """kwargs are ignored when args are given."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, height=7)
        self.assertEqual((r.id, r.width, r.height), (89, 2, 10))

    def test_update_nothing(self):
        """update with no arguments changes nothing."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_update_unknown_key(self):
        """Unknown keys are ignored."""
        r = Rectangle(1, 2)
        r.update(color="red")
        self.assertFalse(hasattr(r, "color"))

    def test_update_none_id(self):
        """Updating the id to None gives a new automatic id."""
        r = Rectangle(1, 2, 0, 0, 89)
        r.update(None)
        self.assertEqual(r.id, 1)

    def test_update_validates(self):
        """update runs the same checks as the setters."""
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            r.update(1, "2")
        with self.assertRaises(ValueError):
            r.update(width=0)

    def test_to_dictionary(self):
        """to_dictionary returns all five attributes."""
        r = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(r.to_dictionary(),
                         {"x": 1, "y": 9, "id": 1, "height": 2, "width": 10})

    def test_to_dictionary_update(self):
        """A dictionary can copy one rectangle's values to another."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)


if __name__ == "__main__":
    unittest.main()
