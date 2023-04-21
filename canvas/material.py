from num_tuples.colour import Colour


class Material:
    def __init__(
        self,
        colour=Colour((1, 1, 1)),
        ambient=0.1,
        diffuse=0.9,
        specular=0.9,
        shininess=200,
    ):
        self.colour = colour
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess

    def __eq__(self, other):
        return (
            self.colour == other.colour
            and self.ambient == other.ambient
            and self.diffuse == other.diffuse
            and self.specular == other.specular
            and self.shininess == other.shininess
        )
