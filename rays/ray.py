class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def __str__(self):
        return f"Ray\n  origin: {self.origin}\n  direction: {self.direction}"

    def transform(self, matrix):
        return Ray(matrix * self.origin, matrix * self.direction)

    def position(self, t):
        return self.origin + t * self.direction
