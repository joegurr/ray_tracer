from matrices.square_matrix import SquareMatrix


class Shape:
    def __init__(self, transform=None):
        self.transform = SquareMatrix.identity(4) if not transform else transform

    def __str__(self):
        return "Shape"

    def intersect(self, ray):
        return self.local_intersect(ray.transform(self.transform.inverse()))

    def local_intersect(self, ray):
        pass
