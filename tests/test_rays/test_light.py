import unittest
from rays.light import PointLight
from num_tuples.colour import Colour
from num_tuples.point import Point


class TestLightClass(unittest.TestCase):
    def test_a_point_light_has_position_and_intensity(self):
        p = Point((0, 0, 0))
        i = Colour((1, 1, 1))
        l = PointLight(p, i)

        self.assertEqual(l.position, p)
        self.assertEqual(l.intensity, i)


if __name__ == "__main__":
    unittest.main()
