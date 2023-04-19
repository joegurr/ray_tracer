from math import sqrt
from num_tuples.base_num_tuple import BaseNumTuple


class Vector(BaseNumTuple):
    def __init__(self, xs):
        if len(xs) == 4:
            xs = xs[:-1]
        BaseNumTuple.__init__(self, xs + (0,))

    def __abs__(self):
        return sqrt(sum(e**2 for e in self.tuple[:-1]))

    def __str__(self):
        return f'Vector <{(", ").join((str(e) for e in self.tuple[:-1]))}>'

    def cross(self, other):
        u = self.tuple
        v = other.tuple
        return Vector(
            (
                u[1] * v[2] - u[2] * v[1],
                u[2] * v[0] - u[0] * v[2],
                u[0] * v[1] - u[1] * v[0],
            )
        )

    def dot(self, other):
        return sum(n * m for m, n in zip(self.tuple[:-1], other.tuple[:-1]))

    def normalise(self):
        "Returns a unit vector"
        return self.__truediv__(abs(self))
