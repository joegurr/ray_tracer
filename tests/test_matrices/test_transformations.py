import unittest
from math import pi, sqrt

from num_tuples.vector import Vector
from num_tuples.point import Point
from matrices.transformations import (
    translation,
    scaling,
    rotation_x,
    rotation_y,
    rotation_z,
    shearing,
)


class TestMatrixTransformations(unittest.TestCase):
    def test_multiplying_by_a_translation_matrix(self):
        p1 = Point((-3, 4, 5))
        transform = translation(5, -3, 2)
        p2 = Point((2, 1, 7))
        self.assertEqual(transform * p1, p2)

    def test_multiplying_by_the_inverse_of_a_translation_matrix(self):
        p1 = Point((-3, 4, 5))
        transform = translation(5, -3, 2)
        inv = transform.inverse()
        p2 = Point((-8, 7, 3))
        self.assertEqual(inv * p1, p2)

    def test_translation_does_not_affect_vectors(self):
        v = Vector((-3, 4, 5))
        transform = translation(5, -3, 2)
        self.assertEqual(transform * v, v)

    def test_a_scaling_matrix_applied_to_a_point(self):
        p1 = Point((-4, 6, 8))
        transform = scaling(2, 3, 4)
        p2 = Point((-8, 18, 32))
        self.assertEqual(transform * p1, p2)

    def test_a_scaling_matrix_applied_to_a_vector(self):
        v1 = Vector((-4, 6, 8))
        transform = scaling(2, 3, 4)
        v2 = Vector((-8, 18, 32))
        self.assertEqual(transform * v1, v2)

    def test_multiplying_by_the_inverse_of_a_scaling_matrix(self):
        v1 = Vector((-4, 6, 8))
        transform = scaling(2, 3, 4)
        inv = transform.inverse()
        v2 = Vector((-2, 2, 2))
        self.assertEqual(inv * v1, v2)

    def test_reflection_is_scaling_by_a_negative_value(self):
        p1 = Point((2, 3, 4))
        transform = scaling(-1, 1, 1)
        p2 = Point((-2, 3, 4))
        self.assertEqual(transform * p1, p2)

    def test_rotating_a_point_around_the_x_axis(self):
        p1 = Point((0, 1, 0))
        eighth = rotation_x(pi / 4)
        quarter = rotation_x(pi / 2)
        p2 = Point((0, sqrt(2) / 2, sqrt(2) / 2))
        p3 = Point((0, 0, 1))
        self.assertEqual(eighth * p1, p2)
        self.assertEqual(quarter * p1, p3)

    def test_inverse_of_an_x_rotation_rotates_in_opposite_direction(self):
        p1 = Point((0, 1, 0))
        eighth = rotation_x(pi / 4)
        inv = eighth.inverse()
        p2 = Point((0, sqrt(2) / 2, -sqrt(2) / 2))
        self.assertEqual(inv * p1, p2)

    def test_rotating_a_point_around_the_y_axis(self):
        p1 = Point((0, 0, 1))
        eighth = rotation_y(pi / 4)
        quarter = rotation_y(pi / 2)
        p2 = Point((sqrt(2) / 2, 0, sqrt(2) / 2))
        p3 = Point((1, 0, 0))
        self.assertEqual(eighth * p1, p2)
        self.assertEqual(quarter * p1, p3)

    def test_rotating_a_point_around_the_z_axis(self):
        p1 = Point((0, 1, 0))
        eighth = rotation_z(pi / 4)
        quarter = rotation_z(pi / 2)
        p2 = Point((-sqrt(2) / 2, sqrt(2) / 2, 0))
        p3 = Point((-1, 0, 0))
        self.assertEqual(eighth * p1, p2)
        self.assertEqual(quarter * p1, p3)

    def test_shearing_transform_moves_x_in_proportion_to_y(self):
        p1 = Point((2, 3, 4))
        p2 = Point((5, 3, 4))
        transform = shearing(1, 0, 0, 0, 0, 0)
        self.assertEqual(transform * p1, p2)

    def test_shearing_transform_moves_x_in_proportion_to_z(self):
        p1 = Point((2, 3, 4))
        p2 = Point((6, 3, 4))
        transform = shearing(0, 1, 0, 0, 0, 0)
        self.assertEqual(transform * p1, p2)

    def test_shearing_transform_moves_y_in_proportion_to_x(self):
        p1 = Point((2, 3, 4))
        p2 = Point((2, 5, 4))
        transform = shearing(0, 0, 1, 0, 0, 0)
        self.assertEqual(transform * p1, p2)

    def test_shearing_transform_moves_y_in_proportion_to_z(self):
        p1 = Point((2, 3, 4))
        p2 = Point((2, 7, 4))
        transform = shearing(0, 0, 0, 1, 0, 0)
        self.assertEqual(transform * p1, p2)

    def test_shearing_transform_moves_z_in_proportion_to_x(self):
        p1 = Point((2, 3, 4))
        p2 = Point((2, 3, 6))
        transform = shearing(0, 0, 0, 0, 1, 0)
        self.assertEqual(transform * p1, p2)

    def test_shearing_transform_moves_z_in_proportion_to_y(self):
        p1 = Point((2, 3, 4))
        p2 = Point((2, 3, 7))
        transform = shearing(0, 0, 0, 0, 0, 1)
        self.assertEqual(transform * p1, p2)

    def test_individual_transformations_are_applied_in_sequence(self):
        p1 = Point((1, 0, 1))
        A = rotation_x(pi / 2)
        B = scaling(5, 5, 5)
        C = translation(10, 5, 7)
        p2 = Point((1, -1, 0))
        p3 = Point((5, -5, 0))
        p4 = Point((15, 0, 7))
        self.assertEqual(A * p1, p2)
        self.assertEqual(B * p2, p3)
        self.assertEqual(C * p3, p4)

    def test_chained_transformations_must_be_applied_in_reverse_order(self):
        p1 = Point((1, 0, 1))
        A = rotation_x(pi / 2)
        B = scaling(5, 5, 5)
        C = translation(10, 5, 7)
        T = C @ B @ A
        p2 = Point((15, 0, 7))
        self.assertEqual(T * p1, p2)


if __name__ == "__main__":
    unittest.main()
