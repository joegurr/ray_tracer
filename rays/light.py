class PointLight:
    def __init__(self, p, i):
        self.position = p
        self.intensity = i

    def __str__(self):
        return f"PointLight\n\tposition: {self.position}\n\tintensity: {self.intensity}"
