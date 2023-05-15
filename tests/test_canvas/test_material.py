from math import sqrt
import unittest
from canvas.material import Material
from num_tuples.colour import Colour
from num_tuples.point import Point
from num_tuples.vector import Vector
from rays.light import PointLight


class TestMaterialClass(unittest.TestCase):
    def test_default_material(self):
        m = Material()
        self.assertEqual(m.colour, Colour((1, 1, 1)))
        self.assertEqual(m.ambient, 0.1)
        self.assertEqual(m.diffuse, 0.9)
        self.assertEqual(m.specular, 0.9)
        self.assertEqual(m.shininess, 200)

    def test_lighting_with_the_eye_between_light_and_surface(self):
        eyev = Vector((0, 0, -1))
        normalv = Vector((0, 0, -1))
        light = PointLight(Point((0, 0, -10)), Colour((1, 1, 1)))
        material = Material()
        result = Colour((1.9, 1.9, 1.9))
        self.assertEqual(
            material.lighting(light, Point((0, 0, 0)), eyev, normalv), result
        )

    def test_lighting_with_the_eye_between_light_and_offset_45_degrees(self):
        eyev = Vector((0, 1 / sqrt(2), -1 / sqrt(2)))
        normalv = Vector((0, 0, -1))
        light = PointLight(Point((0, 0, -10)), Colour((1, 1, 1)))
        material = Material()
        result = Colour((1, 1, 1))
        self.assertEqual(
            material.lighting(light, Point((0, 0, 0)), eyev, normalv), result
        )

    def test_lighting_with_eye_opposite_surface_light_offset_45_degrees(self):
        eyev = Vector((0, 0, -1))
        normalv = Vector((0, 0, -1))
        light = PointLight(Point((0, 10, -10)), Colour((1, 1, 1)))
        material = Material()
        result = Colour((0.7364, 0.7364, 0.7364))
        self.assertEqual(
            material.lighting(light, Point((0, 0, 0)), eyev, normalv), result
        )

    def test_lighting_with_the_eye_in_the_path_of_the_reflection_vector(self):
        eyev = Vector((0, -1 / sqrt(2), -1 / sqrt(2)))
        normalv = Vector((0, 0, -1))
        light = PointLight(Point((0, 10, -10)), Colour((1, 1, 1)))
        material = Material()
        result = Colour((1.6364, 1.6364, 1.6364))
        self.assertEqual(
            material.lighting(light, Point((0, 0, 0)), eyev, normalv), result
        )

    def test_lighting_with_the_light_behind_the_surface(self):
        eyev = Vector((0, 0, -1))
        normalv = Vector((0, 0, -1))
        light = PointLight(Point((0, 0, 10)), Colour((1, 1, 1)))
        material = Material()
        result = Colour((0.1, 0.1, 0.1))
        self.assertEqual(
            material.lighting(light, Point((0, 0, 0)), eyev, normalv), result
        )


if __name__ == "__main__":
    unittest.main()
