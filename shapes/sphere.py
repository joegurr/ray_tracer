from num_tuples.point import Point
from matrices.square_matrix import SquareMatrix


class Sphere:
    def __init__(self):
        self.origin = Point((0, 0, 0))
        self.transform = SquareMatrix.identity()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "Sphere"
