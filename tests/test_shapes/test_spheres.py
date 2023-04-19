import unittest
from shapes.sphere import Sphere
from matrices.square_matrix import SquareMatrix
from matrices.transformations import translation, scaling
from rays.ray import Ray
from num_tuples.point import Point
from num_tuples.vector import Vector


class TestSphereClass(unittest.TestCase):
    def test_a_ray_intersects_a_sphere_at_two_points(self):
        r = Ray(Point((0, 0, -5)), Vector((0, 0, 1)))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(xs.ts(), (4, 6))
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs.objects(), (s, s))

    def test_a_ray_intersects_a_sphere_at_a_tangent(self):
        r = Ray(Point((0, 1, -5)), Vector((0, 0, 1)))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(xs.ts(), (5, 5))
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs.objects(), (s, s))

    def test_a_ray_misses_a_sphere(self):
        r = Ray(Point((0, 2, -5)), Vector((0, 0, 1)))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(xs.ts(), ())
        self.assertEqual(len(xs), 0)
        self.assertEqual(xs.objects(), ())

    def test_a_ray_originates_inside_a_sphere(self):
        r = Ray(Point((0, 0, 0)), Vector((0, 0, 1)))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(xs.ts(), (-1, 1))
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs.objects(), (s, s))

    def test_a_sphere_is_behind_a_ray(self):
        r = Ray(Point((0, 0, 5)), Vector((0, 0, 1)))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(xs.count, 2)
        self.assertEqual(xs[0].t, -6)
        self.assertEqual(xs[1].t, -4)

    def intersect_sets_the_object_on_the_intersection(self):
        r = Ray(Point((0, 0, -5)), Vector((0, 0, 1)))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(xs.count, 2)
        self.assertEqual(xs[0].object, s)
        self.assertEqual(xs[1].object, s)

    def test_a_spheres_default_transformation(self):
        s = Sphere()
        self.assertEqual(s.transform, SquareMatrix.identity())

    def test_changing_a_spheres_transformation(self):
        s = Sphere()
        t = translation(2, 3, 4)
        s.transform = t
        self.assertEqual(s.transform, t)

    def test_intersecting_a_scaled_sphere_with_a_ray(self):
        r = Ray(Point((0, 0, -5)), Vector((0, 0, 1)))
        s = Sphere()
        s.transform = scaling(2, 2, 2)
        xs = s.intersect(r)
        self.assertEqual(xs.count, 2)
        self.assertEqual(xs[0].t, 3)
        self.assertEqual(xs[1].t, 7)

    def test_intersecting_a_translated_sphere_with_a_ray(self):
        r = Ray(Point((0, 0, -5)), Vector((0, 0, 1)))
        s = Sphere()
        s.transform = translation(5, 0, 0)
        xs = s.intersect(r)
        self.assertEqual(len(xs), 0)
