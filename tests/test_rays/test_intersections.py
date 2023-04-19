import unittest

from rays.intersections import Intersection, Intersections
from shapes.sphere import Sphere


class TestIntersectionClasses(unittest.TestCase):
    def test_an_intersection_encapsulates_t_and_object(self):
        s = Sphere()
        i = Intersection(3.5, s)
        self.assertEqual(i.t, 3.5)
        self.assertEqual(i.object, s)

    def test_aggregating_intersections(self):
        s = Sphere()
        i1 = Intersection(1, s)
        i2 = Intersection(2, s)
        xs = Intersections([i1, i2])
        self.assertEqual(xs.count, 2)
        self.assertEqual(xs[0].t, 1)
        self.assertEqual(xs[1].t, 2)

    def test_the_hit_when_all_intersections_have_positive_t(self):
        s = Sphere()
        i1 = Intersection(1, s)
        i2 = Intersection(2, s)
        xs = Intersections([i1, i2])
        self.assertEqual(xs.hit(), i1)

    def test_the_hit_when_some_intersections_have_negative_t(self):
        s = Sphere()
        i1 = Intersection(-1, s)
        i2 = Intersection(1, s)
        xs = Intersections([i1, i2])
        self.assertEqual(xs.hit(), i2)

    def test_the_hit_when_all_intersections_have_negative_t(self):
        s = Sphere()
        i1 = Intersection(-1, s)
        i2 = Intersection(-2, s)
        xs = Intersections([i1, i2])
        self.assertEqual(xs.hit(), None)

    def test_the_hit_is_always_the_lowest_nonnegative_intersection(self):
        s = Sphere()
        i1 = Intersection(5, s)
        i2 = Intersection(7, s)
        i3 = Intersection(-3, s)
        i4 = Intersection(2, s)
        xs = Intersections([i1, i2, i3, i4])
        self.assertEqual(xs.hit(), i4)
