import unittest

from num_tuples.point import Point
from num_tuples.vector import Vector


class TestPointClass(unittest.TestCase):
    def test_point_creates_tuples_with_w_equal_1(self):
        p = Point((4, -4, 3))
        self.assertEqual(p[3], 1)

    def test_subtracting_points(self):
        p1 = Point((3, 2, 1))
        p2 = Point((5, 6, 7))
        p3 = Point((-2, -4, -6))
        self.assertEqual(p1 - p2, p3)

    def test_subtracting_a_vector_from_a_point(self):
        p1 = Point((3, 2, 1))
        v = Vector((5, 6, 7))
        p2 = Point((-2, -4, -6))
        self.assertEqual(p1 - v, p2)

    def test_negating_a_point(self):
        p1 = Point((1, -2, 3))
        p2 = Point((-1, 2, -3))
        self.assertEqual(-p1, p2)


if __name__ == "__main__":
    unittest.main()
