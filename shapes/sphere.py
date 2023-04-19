from num_tuples.point import Point
from shapes.shape import Shape
from rays.intersections import Intersections, Intersection


class Sphere(Shape):
    def __init__(self, transform=None):
        self.origin = Point((0, 0, 0))
        super().__init__(transform)

    def __str__(self):
        return "Sphere"

    def local_intersect(sphere, ray):
        sphere_to_ray = ray.origin.vector_from(sphere.origin)
        a = ray.direction.dot(ray.direction)
        b = 2 * ray.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - 1

        d = b**2 - 4 * a * c

        if d < 0:
            return Intersections([])

        t1 = (-b - d**0.5) / (2 * a)
        t2 = (-b + d**0.5) / (2 * a)

        return Intersections([Intersection(t1, sphere), Intersection(t2, sphere)])
