import unittest
from canvas.material import Material
from num_tuples.colour import Colour


class TestMaterialClass(unittest.TestCase):
    def test_default_material(self):
        m = Material()
        self.assertEqual(m.colour, Colour((1, 1, 1)))
        self.assertEqual(m.ambient, 0.1)
        self.assertEqual(m.diffuse, 0.9)
        self.assertEqual(m.specular, 0.9)
        self.assertEqual(m.shininess, 200)


if __name__ == "__main__":
    unittest.main()
