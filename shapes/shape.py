from canvas.material import Material
from matrices.square_matrix import SquareMatrix


class Shape:
    def __init__(self, transform=None, material=None):
        self.transform = transform if transform else SquareMatrix.identity(4)
        self.material = material if material else Material()

    def __str__(self):
        return "Shape"

    def intersect(self, ray):
        return self.local_intersect(ray.transform(self.transform.inverse()))

    def local_intersect(self, ray):
        pass

    def normal_at(self, world_point):
        pass
