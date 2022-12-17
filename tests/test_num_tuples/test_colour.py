import unittest

from num_tuples.colour import Colour


class TestColourClass(unittest.TestCase):
    def test_colours_are_rgb_tuples(self):
        c = Colour((-0.5, 0.4, 1.7))
        self.assertTrue(isinstance(c, Colour))

    def test_adding_colours(self):
        c1 = Colour((0.9, 0.6, 0.75))
        c2 = Colour((0.7, 0.1, 0.25))
        c3 = Colour((1.6, 0.7, 1.0))

        self.assertEqual(c1 + c2, c3)
        self.assertTrue(isinstance(c1 + c2, Colour))

    def test_subtracting_colours(self):
        c1 = Colour((0.9, 0.6, 0.75))
        c2 = Colour((0.7, 0.1, 0.25))
        c3 = Colour((0.2, 0.5, 0.5))

        self.assertEqual(c1 - c2, c3)
        self.assertTrue(isinstance(c1 - c2, Colour))

    def test_multiplying_a_colour_by_a_scalar(self):
        c1 = Colour((0.2, 0.3, 0.4))
        c2 = Colour((0.4, 0.6, 0.8))

        self.assertEqual(2 * c1, c2)
        self.assertTrue(isinstance(2 * c1, Colour))

    def test_multiplying_colours(self):
        c1 = Colour((1, 0.2, 0.4))
        c2 = Colour((0.9, 1, 0.1))
        c3 = Colour((0.9, 0.2, 0.04))

        self.assertEqual(c1 * c2, c3)
        self.assertTrue(isinstance(c1 * c2, Colour))
