from lib2to3.pytree import Base
from num_tuples.base_num_tuple import BaseNumTuple


class Point(BaseNumTuple):
    def __init__(self, xs):
        if len(xs) == 4:
            xs = xs[:-1]
        BaseNumTuple.__init__(self, xs + (1,))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'Point ({(", ").join((str(e) for e in self.tuple[:-1]))})'
