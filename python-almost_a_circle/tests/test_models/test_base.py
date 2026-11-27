#!/usr/bin/python3
"""Unit tests for the Base class in models/base.py."""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInit(unittest.TestCase):
    """Tests for creating Base instances and their ids."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def test_auto_ids(self):
        """Ids go up by one when no id is given."""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)

    def test_given_id(self):
        """A given id is used as is."""
        self.assertEqual(Base(12).id, 12)

    def test_given_id_does_not_count(self):
        """A given id doesn't change the automatic counter."""
        Base()
        Base(12)
        self.assertEqual(Base().id, 2)

    def test_none_id(self):
        """Passing None uses the automatic id."""
        self.assertEqual(Base(None).id, 1)

    def test_other_id_types(self):
        """Any value other than None is stored as the id."""
        self.assertEqual(Base("abc").id, "abc")
        self.assertEqual(Base(-5).id, -5)
        self.assertEqual(Base([1]).id, [1])

    def test_counter_is_private(self):
        """The counter can't be reached by its plain name."""
        with self.assertRaises(AttributeError):
            Base.__nb_objects

    def test_too_many_args(self):
        """Two arguments raise a TypeError."""
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestToJsonString(unittest.TestCase):
    """Tests for Base.to_json_string."""

    def test_none(self):
        """None gives an empty JSON list."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty(self):
        """An empty list gives an empty JSON list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_one_dict(self):
        """One dictionary is converted to a JSON string."""
        d = {"id": 1, "width": 2}
        result = Base.to_json_string([d])
        self.assertEqual(type(result), str)
        self.assertEqual(json.loads(result), [d])

    def test_rectangle_dict(self):
        """A rectangle's dictionary converts correctly."""
        r = Rectangle(10, 7, 2, 8, 1)
        result = Base.to_json_string([r.to_dictionary()])
        self.assertEqual(json.loads(result), [r.to_dictionary()])

    def test_two_dicts(self):
        """Two dictionaries give a JSON list of two."""
        result = Base.to_json_string([{"id": 1}, {"id": 2}])
        self.assertEqual(json.loads(result), [{"id": 1}, {"id": 2}])

    def test_no_args(self):
        """Calling with no argument raises a TypeError."""
        with self.assertRaises(TypeError):
            Base.to_json_string()


class TestFromJsonString(unittest.TestCase):
    """Tests for Base.from_json_string."""

    def test_none(self):
        """None gives an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        """An empty string gives an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_empty_list_string(self):
        """The string [] gives an empty list."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_round_trip(self):
        """to_json_string then from_json_string gives the original list."""
        data = [{"id": 89, "width": 10, "height": 4},
                {"id": 7, "width": 1, "height": 7}]
        result = Base.from_json_string(Base.to_json_string(data))
        self.assertEqual(result, data)
        self.assertEqual(type(result), list)

    def test_no_args(self):
        """Calling with no argument raises a TypeError."""
        with self.assertRaises(TypeError):
            Base.from_json_string()


class TestSaveAndLoad(unittest.TestCase):
    """Tests for save_to_file, create and load_from_file."""

    def setUp(self):
        """Reset the counter before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove any JSON files a test created."""
        for name in ("Base.json", "Rectangle.json", "Square.json"):
            if os.path.exists(name):
                os.remove(name)

    def read(self, name):
        """Return the parsed contents of a JSON file."""
        with open(name, "r") as f:
            return json.loads(f.read())

    def test_save_rectangles(self):
        """Rectangles are saved to Rectangle.json."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertEqual(self.read("Rectangle.json"),
                         [r1.to_dictionary(), r2.to_dictionary()])

    def test_save_squares(self):
        """Squares are saved to Square.json."""
        s = Square(5, 1, 2)
        Square.save_to_file([s])
        self.assertEqual(self.read("Square.json"), [s.to_dictionary()])

    def test_save_none(self):
        """Saving None writes an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_empty(self):
        """Saving an empty list writes an empty list."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_overwrites(self):
        """Saving again replaces the old contents."""
        Rectangle.save_to_file([Rectangle(1, 2), Rectangle(3, 4)])
        Rectangle.save_to_file([Rectangle(5, 6)])
        self.assertEqual(len(self.read("Rectangle.json")), 1)

    def test_create_rectangle(self):
        """create builds a new Rectangle with the same values."""
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_create_square(self):
        """create builds a new Square with the same values."""
        s1 = Square(3, 1, 2, 7)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s2), "[Square] (7) 1/2 - 3")
        self.assertIsNot(s1, s2)

    def test_create_partial(self):
        """create works with only some attributes given."""
        r = Rectangle.create(id=89, width=4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 4)

    def test_load_rectangles(self):
        """Rectangles saved to a file load back with the same values."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual([str(r) for r in loaded], [str(r1), str(r2)])
        self.assertTrue(all(type(r) is Rectangle for r in loaded))

    def test_load_squares(self):
        """Squares saved to a file load back with the same values."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()
        self.assertEqual([str(s) for s in loaded], [str(s1), str(s2)])
        self.assertTrue(all(type(s) is Square for s in loaded))

    def test_load_missing_file(self):
        """A missing file gives an empty list."""
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])


if __name__ == "__main__":
    unittest.main()
