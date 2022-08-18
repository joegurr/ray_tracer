from math import sqrt
from numbers import Number


class BaseNumTuple:
    def __init__(self, xs):
        self.tuple = xs

    def __abs__(self):
        return sqrt(sum(e**2 for e in self.tuple))

    def __add__(self, other):
        "Return type is `type(self)`"
        return type(self)(tuple(map(sum, zip(self.tuple, other.tuple))))

    def __eq__(self, other):
        if type(self) != type(other):
            return False

        if len(self) != len(other):
            return False

        for i in range(len(self)):
            if self.tuple[i] != other.tuple[i]:
                return False
        return True

    def __getitem__(self, arg):
        if not isinstance(arg, int) and arg > -1 and arg < len(self):
            raise IndexError()
        return self.tuple[arg]

    def __len__(self):
        return len(self.tuple)

    def __neg__(self):
        "Return type is `type(self)`"
        return type(self)(tuple((-e for e in self.tuple)))

    def __repr__(self):
        return self.__str__()

    def __rmul__(self, num):
        "Return type is `type(self)`"
        if not isinstance(num, Number):
            return self
        return type(self)(tuple((num * e for e in self.tuple)))

    def __str__(self):
        return f'_Tuple ({(", ").join((str(e) for e in self.tuple))})'

    def __sub__(self, other):
        "Return type is `type(self)`"
        return type(self)(tuple(map(sum, zip(self.tuple, (-e for e in other.tuple)))))

    def __truediv__(self, num):
        "Return type is `type(self)`"
        if not isinstance(num, Number):
            return self
        return type(self)(tuple((e / num for e in self.tuple)))
