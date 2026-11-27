#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_ordered_list(self):
        """The max is found at the end of an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """The max is found in the middle of a list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """The max is found at the start of a list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Calling with no argument returns None."""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """A list with one element returns that element."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """The max of negative numbers is the one closest to zero."""
        self.assertEqual(max_integer([-5, -1, -3]), -1)

    def test_mixed_signs(self):
        """A mix of negative and positive numbers works."""
        self.assertEqual(max_integer([-10, 0, 10, -20]), 10)

    def test_duplicates(self):
        """Repeated values still give the right max."""
        self.assertEqual(max_integer([2, 5, 5, 1]), 5)

    def test_floats(self):
        """Floats are compared correctly."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_ints_and_floats(self):
        """Integers and floats can be mixed."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_string(self):
        """A string returns its highest character."""
        self.assertEqual(max_integer("School"), "o")

    def test_list_of_strings(self):
        """A list of strings returns the last one alphabetically."""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_none(self):
        """None raises a TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_mixed_types(self):
        """Comparing numbers with strings raises a TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])


if __name__ == "__main__":
    unittest.main()
