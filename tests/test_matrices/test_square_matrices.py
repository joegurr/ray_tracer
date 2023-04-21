import unittest
from matrices.square_matrix import SquareMatrix
from num_tuples.base_num_tuple import BaseNumTuple


class TestSquareMatrixClass(unittest.TestCase):
    def test_constructing_and_inspecting_a_4x4_matrix(self):
        m = SquareMatrix(
            [
                [1, 2, 3, 4],
                [5.5, 6.5, 7.5, 8.5],
                [9, 10, 11, 12],
                [13.5, 14.5, 15.5, 16.5],
            ]
        )

        self.assertEqual(m[0][0], 1)
        self.assertEqual(m[0][3], 4)
        self.assertEqual(m[1][0], 5.5)
        self.assertEqual(m[1][2], 7.5)
        self.assertEqual(m[2][2], 11)
        self.assertEqual(m[3][0], 13.5)
        self.assertEqual(m[3][2], 15.5)

    def test_a_2x2_matrix(self):
        m = SquareMatrix([[-3, 5], [1, -2]])

        self.assertEqual(m[0][0], -3)
        self.assertEqual(m[0][1], 5)
        self.assertEqual(m[1][0], 1)
        self.assertEqual(m[1][1], -2)

    def test_a_3x3_matrix(self):
        m = SquareMatrix([[-3, 5, 0], [1, -2, -7], [0, 1, 1]])

        self.assertEqual(m[0][0], -3)
        self.assertEqual(m[1][1], -2)
        self.assertEqual(m[2][2], 1)

    def test_matrix_equality(self):
        m1 = SquareMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
        m2 = SquareMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
        m3 = SquareMatrix([[2, 3, 4, 5], [6, 7, 8, 9], [8, 7, 6, 5], [4, 3, 2, 1]])
        self.assertEqual(m1, m2)
        self.assertNotEqual(m1, m3)

    def test_multiplying_matrices(self):
        m1 = SquareMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
        m2 = SquareMatrix([[-2, 1, 2, 3], [3, 2, 1, -1], [4, 3, 6, 5], [1, 2, 7, 8]])
        m3 = SquareMatrix(
            [[20, 22, 50, 48], [44, 54, 114, 108], [40, 58, 110, 102], [16, 26, 46, 42]]
        )
        self.assertEqual(m1 @ m2, m3)

    def test_multiplying_a_matrix_by_a_tuple(self):
        m = SquareMatrix([[1, 2, 3, 4], [2, 4, 4, 2], [8, 6, 4, 1], [0, 0, 0, 1]])
        t1 = BaseNumTuple((1, 2, 3, 1))
        t2 = BaseNumTuple((18, 24, 33, 1))

        self.assertEqual(m * t1, t2)

    def test_multiplying_a_matrix_by_the_identity_matrix(self):
        m = SquareMatrix([[0, 1, 2, 4], [1, 2, 4, 8], [2, 4, 8, 16], [4, 8, 16, 32]])
        i = SquareMatrix.identity(4)
        self.assertEqual(m @ i, m)

    def test_multiplying_a_tuple_by_the_identity_matrix(self):
        t = BaseNumTuple((1, 2, 3, 4))
        i = SquareMatrix.identity(4)
        self.assertEqual(i * t, t)

    def test_transposing_a_matrix(self):
        m = SquareMatrix([[0, 9, 3, 0], [9, 8, 0, 8], [1, 8, 5, 3], [0, 0, 5, 8]])
        mT = SquareMatrix([[0, 9, 1, 0], [9, 8, 8, 0], [3, 0, 5, 5], [0, 8, 3, 8]])
        self.assertEqual(m.transpose(), mT)

    def test_transposing_identity_matrix(self):
        i = SquareMatrix.identity(3)
        iT = i.transpose()
        self.assertEqual(i, iT)

    def test_calc_determinant_of_2x2_matrix(self):
        m = SquareMatrix([[1, 5], [-3, 2]])
        self.assertEqual(abs(m), 17)

    def test_sub_matrix_of_3x3_matrix(self):
        m = SquareMatrix([[1, 5, 0], [-3, 2, 7], [0, 6, -3]])
        s = SquareMatrix([[-3, 2], [0, 6]])
        self.assertEqual(m.submatrix(0, 2), s)

    def test_sub_matrix_of_4x4_matrix(self):
        m = SquareMatrix([[-6, 1, 1, 6], [-8, 5, 8, 6], [-1, 0, 8, 2], [-7, 1, -1, 1]])
        s = SquareMatrix([[-6, 1, 6], [-8, 8, 6], [-7, -1, 1]])
        self.assertEqual(m.submatrix(2, 1), s)

    def test_calc_minor_of_a_3x3_matrix(self):
        m = SquareMatrix([[3, 5, 0], [2, -1, -7], [6, -1, 5]])
        self.assertEqual(m.minor(1, 0), 25)
        self.assertEqual(abs(m.submatrix(1, 0)), 25)

    def test_calc_cofactor_of_a_3x3_matrix(self):
        m = SquareMatrix([[3, 5, 0], [2, -1, -7], [6, -1, 5]])

        self.assertEqual(m.minor(0, 0), -12)
        self.assertEqual(m.cofactor(0, 0), -12)
        self.assertEqual(m.minor(1, 0), 25)
        self.assertEqual(m.cofactor(1, 0), -25)

    def test_cal_determinant_of_3x3_matrix(self):
        m = SquareMatrix([[1, 2, 6], [-5, 8, -4], [2, 6, 4]])

        self.assertEqual(m.cofactor(0, 0), 56)
        self.assertEqual(m.cofactor(0, 1), 12)
        self.assertEqual(m.cofactor(0, 2), -46)
        self.assertEqual(abs(m), -196)

    def test_cal_determinant_of_4x4_matrix(self):
        m = SquareMatrix([[-2, -8, 3, 5], [-3, 1, 7, 3], [1, 2, -9, 6], [-6, 7, 7, -9]])

        self.assertEqual(m.cofactor(0, 0), 690)
        self.assertEqual(m.cofactor(0, 1), 447)
        self.assertEqual(m.cofactor(0, 2), 210)
        self.assertEqual(m.cofactor(0, 3), 51)
        self.assertEqual(abs(m), -4071)

    def test_an_invertible_matrix_for_invertibility(self):
        m = SquareMatrix([[6, 4, 4, 4], [5, 5, 7, 6], [4, -9, 3, -7], [9, 1, 7, -6]])
        self.assertEqual(abs(m), -2120)
        self.assertTrue(m.invertible())

    def test_a_non_invertible_matrix_for_invertibility(self):
        m = SquareMatrix([[-4, 2, -2, 3], [9, 6, 2, 6], [0, -5, 1, -5], [0, 0, 0, 0]])
        self.assertEqual(abs(m), 0)
        self.assertFalse(m.invertible())

    def test_calculating_the_inverse_of_some_matrices(self):
        m1 = SquareMatrix(
            [[-5, 2, 6, -8], [1, -5, 1, 8], [7, 7, -6, -7], [1, -3, 7, 4]]
        )
        m1i = SquareMatrix(
            [
                [0.21805, 0.45113, 0.24060, -0.04511],
                [-0.80827, -1.45677, -0.44361, 0.52068],
                [-0.07895, -0.22368, -0.05263, 0.19737],
                [-0.52256, -0.81391, -0.30075, 0.30639],
            ]
        )

        m1I = m1.inverse()
        self.assertEqual(abs(m1), 532)
        self.assertEqual(m1.cofactor(2, 3), -160)
        self.assertEqual(m1I[3][2], -160 / 532)
        self.assertEqual(m1.cofactor(3, 2), 105)
        self.assertEqual(m1I[2][3], 105 / 532)
        self.assertEqual(m1i, m1I)

        m2 = SquareMatrix([[8, -5, 9, 2], [7, 5, 6, 1], [-6, 0, 9, 6], [-3, 0, -9, -4]])
        m2i = SquareMatrix(
            [
                [-0.15385, -0.15385, -0.28205, -0.53846],
                [-0.07692, 0.12308, 0.02564, 0.03077],
                [0.35897, 0.35897, 0.43590, 0.92308],
                [-0.69231, -0.69231, -0.76923, -1.92308],
            ]
        )

        self.assertEqual(m2.inverse(), m2i)

        m3 = SquareMatrix(
            [[9, 3, 0, 9], [-5, -2, -6, -3], [-4, 9, 6, 4], [-7, 6, 6, 2]]
        )
        m3i = SquareMatrix(
            [
                [-0.04074, -0.07778, 0.14444, -0.222222],
                [-0.07778, 0.03333, 0.36667, -0.33333],
                [-0.02901, -0.14630, -0.10926, 0.12963],
                [0.17778, 0.06667, -0.26667, 0.33333],
            ]
        )

        self.assertEqual(m3.inverse(), m3i)

    def test_multiplying_a_product_by_its_inverse(self):
        a = SquareMatrix([[3, -9, 7, 3], [3, -8, 2, -9], [-4, 4, 4, 1], [-6, 5, -1, 1]])
        b = SquareMatrix([[8, 2, 2, 2], [3, -1, 7, 0], [7, 0, 5, 4], [6, -2, 0, 5]])
        c = a @ b
        self.assertEqual(c @ b.inverse(), a)


if __name__ == "__main__":
    unittest.main()
