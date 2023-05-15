import os
from shapes.sphere import Sphere
from canvas.material import Material
from num_tuples.point import Point
from num_tuples.colour import Colour
from canvas.canvas import Canvas
from rays.ray import Ray

import time

s = time.time()

ray_origin = Point((0, 0, -5))

wall_z = 10

wall_size = 7

canvas_pixels = 100

pixel_size = wall_size / canvas_pixels

half = wall_size / 2

canvas = Canvas(canvas_pixels, canvas_pixels)
colour = Colour((1, 0, 0))
shape = Sphere()

for y in range(canvas_pixels - 1):
    world_y = half - pixel_size * y

    for x in range(canvas_pixels - 1):
        world_x = -half + pixel_size * x

        position = Point((world_y, world_x, wall_z))

        r = Ray(ray_origin, position.vector_from(ray_origin).normalise())
        xs = shape.intersect(r)

        if xs.hit():
            canvas.write_pixel(x, y, colour)

# TODO-JOE: don't use unix delimiters, do this properly
canvas.write_PPM(f"./scene/{os.path.basename(__file__)[:-3]}.ppm")
print(f"Took {(time.time() - s)/60:.2f} minutes")
