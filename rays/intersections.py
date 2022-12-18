class Intersection:
    def __init__(self, t, object):
        self.t = t
        self.object = object

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Intersection at t={self.t}\n  object: {self.object}"


class Intersections:
    def __init__(self, intersections):
        self.intersections = intersections

    def __getitem__(self, arg):
        if not isinstance(arg, int) and arg > -1 and arg < len(self):
            raise IndexError()
        return self.intersections[arg]

    def __len__(self):
        return len(self.intersections)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        str_rep = "A list of intersections\n"
        for i in self.intersections:
            str_rep += f"{str(i)}\n"

    def count(self):
        return len(self.intersections)

    def hit(self):
        ys = sorted(self.intersections, key=lambda x: (x.t <= 0, x.t))
        return ys[0] if ys[0].t > 0 else None

    def ts(self):
        return tuple(x.t for x in self.intersections)

    def objects(self):
        return tuple(x.object for x in self.intersections)


def intersect(sphere, ray):
    ray = ray.transform(sphere.transform.inverse())
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
