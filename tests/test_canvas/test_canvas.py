import os
import unittest

from canvas.canvas import Canvas
from num_tuples.colour import Colour


class TestCanvasClass(unittest.TestCase):
    def test_creating_a_canvas(self):
        c = Canvas(10, 20)
        self.assertEqual(c.width, 10)
        self.assertEqual(c.height, 20)

        for i in range(20):
            for j in range(10):
                self.assertEqual(c[i][j], Colour((0, 0, 0)))

    def test_writing_pixels_to_a_canvas(self):
        c = Canvas(10, 20)
        red = Colour((1, 0, 0))
        c.write_pixel(2, 3, red)
        self.assertEqual(c.pixel_at(2, 3), red)

    def test_constructing_the_PPM_header(self):
        filename = "./test_PPM_header.ppm"
        c = Canvas(5, 3)
        c.write_PPM(filename)
        with open(filename, "r") as f:
            lines = f.readlines()
        ppm_header_str = """P3\n5 3\n255\n"""
        self.assertEqual("".join(lines[0:3]), ppm_header_str)
        os.remove(filename)

    def test_constructing_the_PPM_pixel_data(self):
        filename = "./test_pixel_data.ppm"
        c = Canvas(5, 3)
        c.write_pixel(0, 0, Colour((1.5, 0, 0)))
        c.write_pixel(2, 1, Colour((0, 0.5, 0)))
        c.write_pixel(4, 2, Colour((-0.5, 0, 1)))
        c.write_PPM(filename)
        with open(filename, "r") as f:
            lines = f.readlines()
        ppm_pixel_str = """255 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 128 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 255\n"""
        self.assertEqual("".join(lines[3:6]), ppm_pixel_str)
        os.remove(filename)

    def test_splitting_long_lines_in_PPM_files(self):
        filename = "./test_long_lines.ppm"
        c = Canvas(10, 2)
        for i in range(c.height):
            for j in range(c.width):
                c[i][j] = Colour((1, 0.8, 0.6))
        c.write_PPM(filename)
        with open(filename, "r") as f:
            lines = f.readlines()
        ppm_pixel_str = """255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204\n153 255 204 153 255 204 153 255 204 153 255 204 153\n255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204\n153 255 204 153 255 204 153 255 204 153 255 204 153\n"""
        self.assertEqual("".join(lines[3:8]), ppm_pixel_str)
        os.remove(filename)

    def test_PPM_files_are_terminated_by_a_newline_character(self):
        filename = "test_files_end_in_newline.ppm"
        c = Canvas(5, 3)
        c.write_PPM(filename)
        with open(filename, "r") as f:
            line = f.readlines()[-1]
        self.assertEqual(line[-1], "\n")
        os.remove(filename)


if __name__ == "__main__":
    unittest.main()
