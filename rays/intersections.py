class Intersection:
    def __init__(self, t, object):
        self.t = t
        self.object = object

    def __str__(self):
        return f"Intersection at t={self.t}\n  object: {self.object}"


class Intersections:
    def __init__(self, intersections):
        self.intersections = intersections
        self.count = len(intersections)

    def __getitem__(self, arg):
        if not isinstance(arg, int) and arg > -1 and arg < len(self):
            raise IndexError()
        return self.intersections[arg]

    def __len__(self):
        return len(self.intersections)

    def __str__(self):
        str_rep = "A list of intersections\n"
        for i in self.intersections:
            str_rep += f"{str(i)}\n"

    def hit(self):
        ys = sorted(self.intersections, key=lambda x: (x.t <= 0, x.t))
        return ys[0] if ys[0].t > 0 else None

    def ts(self):
        return tuple(x.t for x in self.intersections)

    def objects(self):
        return tuple(x.object for x in self.intersections)
