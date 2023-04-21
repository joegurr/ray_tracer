from math import pi, sqrt
import unittest
from canvas.material import Material
from shapes.sphere import Sphere
from matrices.square_matrix import SquareMatrix
from matrices.transformations import translation, scaling, rotation_z
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

    def test_normal_on_sphere_at_point_on_x_axis(self):
        s = Sphere()
        n1 = s.normal_at(Point((1, 0, 0)))
        n2 = Vector((1, 0, 0))
        self.assertEqual(n1, n2)

    def test_normal_on_sphere_at_point_on_y_axis(self):
        s = Sphere()
        n1 = s.normal_at(Point((0, 1, 0)))
        n2 = Vector((0, 1, 0))
        self.assertEqual(n1, n2)

    def test_normal_on_sphere_at_point_on_z_axis(self):
        s = Sphere()
        n1 = s.normal_at(Point((0, 0, 1)))
        n2 = Vector((0, 0, 1))
        self.assertEqual(n1, n2)

    def test_normal_on_sphere_at_a_non_axial_point(self):
        s = Sphere()
        n1 = s.normal_at(Point((sqrt(3) / 3, sqrt(3) / 3, sqrt(3) / 3)))
        n2 = Vector((sqrt(3) / 3, sqrt(3) / 3, sqrt(3) / 3))
        self.assertEqual(n1, n2)

    def test_the_normal_is_a_normalised_vector(self):
        s = Sphere()
        n1 = s.normal_at(Point((sqrt(3) / 3, sqrt(3) / 3, sqrt(3) / 3)))
        n2 = n1.normalise()
        self.assertEqual(n1, n2)

    def test_computing_the_normal_on_a_translated_sphere(self):
        s = Sphere(translation(0, 1, 0))
        n1 = s.normal_at(Point((0, 1.70711, -0.70711)))
        n2 = Vector((0, 0.70711, -0.70711))
        self.assertEqual(n1, n2)

    def test_computing_the_normal_on_a_transformed_sphere(self):
        s = Sphere(scaling(1, 0.5, 1) @ rotation_z(pi / 5))
        n1 = s.normal_at(Point((0, sqrt(2) / 2, -sqrt(2) / 2)))
        n2 = Vector((0, 0.97014, -0.24254))
        self.assertEqual(n1, n2)

    def test_a_sphere_has_a_default_material(self):
        s = Sphere()
        m = Material()
        self.assertEqual(s.material, m)

    def test_a_sphere_may_be_assigned_a_material(self):
        m = Material(ambient=1)
        s = Sphere(material=m)
        self.assertEqual(s.material, m)


if __name__ == "__main__":
    unittest.main()
