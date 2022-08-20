from numbers import Number
from math import isclose

from num_tuples.base_num_tuple import BaseNumTuple


class SquareMatrix:
    def __init__(self, xss):
        for xs in xss:
            if len(xs) != len(xss):
                raise Exception("This is not a square matrix")
        self.matrix = xss

    def __abs__(self):
        return SquareMatrix._determinant(self)

    def __add__(self, other):
        if not self.same_dim(other):
            raise Exception("Cannot add matrices of different dimensions")
        xss = []
        for i in range(len(self)):
            xss.append([sum(e) for e in zip(self[i], other[i])])

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            for j in range(len(self)):
                if not isclose(self[i][j], other[i][j], abs_tol=1e-5):
                    return False
        return True

    def __getitem__(self, arg):
        if not isinstance(arg, int) and arg > -1 and arg < len(self):
            raise IndexError()
        return self.matrix[arg]

    def __len__(self):
        return len(self.matrix)

    def __matmul__(self, other):
        return SquareMatrix(
            [
                [
                    sum(a * b for a, b in zip(s_row, o_col))
                    for o_col in zip(*other.matrix)
                ]
                for s_row in self.matrix
            ]
        )

    def __mul__(self, factor):
        if isinstance(factor, BaseNumTuple):
            if len(self) != len(factor):
                raise Exception(
                    "Cannot multiply a matrix and a tuple of different dimensions"
                )
            xss = ()
            for xs in self.matrix:
                xss += (sum(p * q for p, q in zip(factor.tuple, tuple(xs))),)

            return type(factor)(xss)

    def __neg__(self):
        xss = []
        for xs in self.matrix:
            xss.append([-e for e in xs])

    def __repr__(self):
        return self.__str__()

    def __rmul__(self, factor):
        """
        Scalar Multiplication
        Return type `SquareMatrix`
        """
        if isinstance(factor, Number):
            xss = []
            for xs in self.matrix:
                xss.append([factor * x for x in xs])
            return SquareMatrix(xss)

    def __str__(self):
        str_rep = f"{len(self)}x{len(self)} Square Matrix\n"
        s = [[str(e) for e in row] for row in self.matrix]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = "\t".join("{{:{}}}".format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        return str_rep + "\n".join(table)

    def __sub__(self, other):
        if not self.same_dim(other):
            raise Exception("Cannot add matrices of different dimensions")
        return self.add(-other)

    def cofactor(self, d_row, d_col):
        return (
            self.minor(d_row, d_col)
            if (d_row + d_col) % 2 == 0
            else -self.minor(d_row, d_col)
        )

    @staticmethod
    def _determinant(m):
        determinant = 0
        if len(m) == 2:
            determinant = m[0][0] * m[1][1] - m[0][1] * m[1][0]
        for i in range(len(m)):
            determinant = determinant + m[0][i] * m.cofactor(0, i)
        return determinant

    @staticmethod
    def identity(n):
        xss = []
        for i in range(n):
            xs = n * [0]
            xs[i] = 1
            xss.append(xs)
        return SquareMatrix(xss)

    def inverse(self):
        if not self.invertible():
            return None
        m = SquareMatrix.identity(len(self))
        for i in range(len(self)):
            for j in range(len(self)):
                c = self.cofactor(i, j)
                m[j][i] = c / abs(self)
        return m

    def invertible(self):
        return abs(self) != 0

    def minor(self, d_row, d_col):
        return abs(self.submatrix(d_row, d_col))

    def same_dim(self, other):
        return len(self) == len(other)

    def submatrix(self, d_row, d_col):
        xss = [xs.copy() for xs in self.matrix]
        xss.pop(d_row)
        [xs.pop(d_col) for xs in xss]
        return SquareMatrix(xss)

    def transpose(self):
        xss = []
        for i in range(len(self)):
            xs = []
            for j in range(len(self)):
                xs.append(self[j][i])
            xss.append(xs)
        return SquareMatrix(xss)


if __name__ == "__main__":
    m1 = SquareMatrix(
        [
            [1, 2, 3, 4],
            [5.5, 6.5, 7.5, 8.5],
            [9, 10, 11, 12],
            [13.5, 14.5, 15.5, 16.5],
        ]
    )

    m2 = SquareMatrix([[-2, 1, 2, 3], [3, 2, 1, -1], [4, 3, 6, 5], [1, 2, 7, 8]])

    t = BaseNumTuple((1, 4, 5, 6))

    breakpoint()
