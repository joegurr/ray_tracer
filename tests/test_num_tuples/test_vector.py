from math import sqrt
import unittest

from num_tuples.vector import Vector


class TestVectorClass(unittest.TestCase):
    def test_vector_creates_tuples_with_w_equal_0(self):
        v = Vector((4, -4, 3))
        self.assertEqual(v[3], 0)

    def test_subtracting_two_vectors(self):
        v1 = Vector((3, 2, 1))
        v2 = Vector((5, 6, 7))
        v3 = Vector((-2, -4, -6))
        self.assertEqual(v1 - v2, v3)

    def test_subtracting_a_vector_from_the_zero_vector(self):
        O = Vector((0, 0, 0))
        v1 = Vector((1, -2, 3))
        v2 = Vector((-1, 2, -3))
        self.assertEqual(O - v1, v2)

    def test_magnitude(self):
        e1 = Vector((1, 0, 0))
        e2 = Vector((0, 1, 0))
        e3 = Vector((0, 0, 1))
        v1 = Vector((1, 2, 3))
        v2 = Vector((-1, -2, -3))

        self.assertEqual(abs(e1), 1)
        self.assertEqual(abs(e2), 1)
        self.assertEqual(abs(e3), 1)
        self.assertAlmostEqual(abs(v1), sqrt(14))
        self.assertAlmostEqual(abs(v2), sqrt(14))

    def test_normalisation(self):
        v1 = Vector((4, 0, 0))
        e1 = Vector((1, 0, 0))

        v2 = Vector((1, 2, 3))
        v3 = Vector((1 / sqrt(14), 2 / sqrt(14), 3 / sqrt(14)))

        self.assertEqual(v1.normalise(), e1)
        self.assertAlmostEqual(v2.normalise(), v3)
        self.assertAlmostEqual(abs(v2.normalise()), 1)

    def test_dot_product(self):
        v1 = Vector((1, 2, 3))
        v2 = Vector((2, 3, 4))
        self.assertEqual(v1.dot(v2), 20)

    def test_cross_product(self):
        v1 = Vector((1, 2, 3))
        v2 = Vector((2, 3, 4))
        v12 = Vector((-1, 2, -1))
        self.assertEqual(v1.cross(v2), v12)
        self.assertEqual(v2.cross(v1), -v12)

    def test_reflecting_a_vector_approaching_at_45_degrees(self):
        v = Vector((1, -1, 0))
        n = Vector((0, 1, 0))
        r1 = v.reflect(n)
        r2 = Vector((1, 1, 0))
        self.assertEqual(r1, r2)

    def test_reflecting_a_vector_off_a_slanted_surface(self):
        v = Vector((0, -1, 0))
        n = Vector((sqrt(2) / 2, sqrt(2) / 2, 0))
        r1 = v.reflect(n)
        r2 = Vector((1, 0, 0))
        self.assertEqual(r1, r2)


if __name__ == "__main__":
    unittest.main()
