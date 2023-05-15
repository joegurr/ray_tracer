import os
from shapes.sphere import Sphere
from canvas.material import Material
from num_tuples.point import Point
from num_tuples.colour import Colour
from canvas.canvas import Canvas
from rays.ray import Ray
from rays.light import PointLight

import time

s = time.time()

ray_origin = Point((0, 0, -5))

wall_z = 10

wall_size = 7

canvas_pixels = 100

pixel_size = wall_size / canvas_pixels

half = wall_size / 2

canvas = Canvas(canvas_pixels, canvas_pixels)
shape = Sphere(material=Material(colour=Colour((1, 0.2, 1))))

light_position = Point((-10, 10, -10))
light_colour = Colour((1, 0.2, 1))
light = PointLight(light_position, light_colour)

for y in range(canvas_pixels - 1):
    world_y = half - pixel_size * y

    for x in range(canvas_pixels - 1):
        world_x = -half + pixel_size * x

        position = Point((world_y, world_x, wall_z))

        r = Ray(ray_origin, position.vector_from(ray_origin).normalise())
        xs = shape.intersect(r)

        if xs.hit():
            point = r.position(xs.hit().t)
            normal = shape.normal_at(point)
            eye = -r.direction
            colour = shape.material.lighting(light, point, eye, normal)
            canvas.write_pixel(x, y, colour)

# TODO-JOE: don't use unix delimiters, do this properly
canvas.write_PPM(f"./scene/{os.path.basename(__file__)[:-3]}.ppm")
print(f"Took {(time.time() - s)/60:.2f} minutes")
