from num_tuples.colour import Colour


class Canvas:
    def __init__(self, width, height):
        canvas = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(Colour((0, 0, 0)))
            canvas.append(row)
        self.canvas = canvas
        self.width = width
        self.height = height

    def __getitem__(self, i):
        return self.canvas[i]

    def __str__(self):
        return f"Canvas {self.width}x{self.height}"

    def _PPM_header(self):
        return f"""P3\n{self.width} {self.height}\n255\n"""

    def pixel_at(self, x_coord, y_coord):
        return self.canvas[y_coord][x_coord]

    def write_pixel(self, x_coord, y_coord, colour):
        self.canvas[y_coord][x_coord] = colour

    def write_PPM(self, filename):
        ppm_header_str = self._PPM_header()
        ppm_str = ""
        for i in range(self.height):
            row_str = ""
            for j in range(self.width):
                row_str += f"{self[i][j].ppm_colour_str()}"  # add colour here
            # can't let line length get longer than 70 chars
            if len(row_str) > 70:
                new_row_str = ""
                xs = row_str.split(" ")
                len_counter = 0
                while xs:
                    len_counter += len(xs[0]) + 1
                    if len_counter > 70:
                        len_counter = 0
                        new_row_str = new_row_str[:-1] + "\n"
                    new_row_str += xs.pop(0) + " "
                ppm_str += new_row_str[:-2] + "\n"
            else:
                row_str = row_str[:-1] + "\n"
                ppm_str += row_str
        ppm_header_str += ppm_str
        with open(filename, "w") as f:
            f.write(ppm_header_str)
