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

    def lighting(self, light, point, eyev, normalv):
        effective_colour = self.colour * light.intensity

        lightv = light.position.vector_from(point).normalise()

        ambient = self.ambient * effective_colour

        light_dot_normal = lightv.dot(normalv)

        if light_dot_normal < 0:
            diffuse = Colour((0, 0, 0))
            specular = Colour((0, 0, 0))
        else:
            diffuse = self.diffuse * light_dot_normal * effective_colour

            reflectv = (-lightv).reflect(normalv)
            reflect_dot_eye = reflectv.dot(eyev)

            if reflect_dot_eye < 0:
                specular = Colour((0, 0, 0))
            else:
                factor = pow(reflect_dot_eye, self.shininess)
                specular = self.specular * factor * light.intensity

        return ambient + diffuse + specular
