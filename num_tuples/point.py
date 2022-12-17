from num_tuples.base_num_tuple import BaseNumTuple
from num_tuples.vector import Vector


class Point(BaseNumTuple):
    def __init__(self, xs):
        if len(xs) == 4:
            xs = xs[:-1]
        BaseNumTuple.__init__(self, xs + (1,))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'Point ({(", ").join((str(e) for e in self.tuple[:-1]))})'

    def vector_from(self, other):
        return Vector((self - other).tuple[:-1])
