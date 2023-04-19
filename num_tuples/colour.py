from num_tuples.base_num_tuple import BaseNumTuple


class Colour(BaseNumTuple):
    def __init__(self, xs):
        if len(xs) != 3:
            raise Exception("Colours only have three inputs")
        BaseNumTuple.__init__(self, xs)

    def __str__(self):
        return f'Colour ({(", ").join((str(e) for e in self.tuple))})'

    def __mul__(self, other):
        return self._hadamard_product(other)

    def _hadamard_product(self, other):
        return Colour(tuple(p * q for p, q in zip(self.tuple, other.tuple)))

    def _ppm_colour_component_str(self, i):
        c = self[i]
        if c < 0:
            c = 0
        elif c >= 1:
            c = 1
        c = round(255 * c)
        return str(round(c)) + " "

    def ppm_colour_str(self):
        ppm_colour_str = ""
        for i in range(len(self)):
            ppm_colour_str += self._ppm_colour_component_str(i)
        return ppm_colour_str
