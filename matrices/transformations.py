from math import sin, cos
from matrices.square_matrix import SquareMatrix


def translation(x, y, z):
    return SquareMatrix([[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]])


def scaling(x, y, z):
    return SquareMatrix([[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]])


def rotation_x(r):
    return SquareMatrix(
        [[1, 0, 0, 0], [0, cos(r), -sin(r), 0], [0, sin(r), cos(r), 0], [0, 0, 0, 1]]
    )


def rotation_y(r):
    return SquareMatrix(
        [[cos(r), 0, sin(r), 0], [0, 1, 0, 0], [-sin(r), 0, cos(r), 0], [0, 0, 0, 1]]
    )


def rotation_z(r):
    return SquareMatrix(
        [[cos(r), -sin(r), 0, 0], [sin(r), cos(r), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    )


def shearing(x_y, x_z, y_x, y_z, z_x, z_y):
    return SquareMatrix(
        [[1, x_y, x_z, 0], [y_x, 1, y_z, 0], [z_x, z_y, 1, 0], [0, 0, 0, 1]]
    )
