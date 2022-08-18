import unittest

from num_tuples.base_num_tuple import BaseNumTuple


class TestBaseNumTupleClass(unittest.TestCase):
    def test_adding_tuples(self):
        t1 = BaseNumTuple((3, -2, 5, 1))
        t2 = BaseNumTuple((-2, 3, 1, 0))
        t3 = BaseNumTuple((1, 1, 6, 1))
        self.assertEqual(t1 + t2, t3)
        self.assertTrue(isinstance(t1 + t2, BaseNumTuple))

    def test_subtracting_tuples(self):
        t1 = BaseNumTuple((3, 2, 1, 3))
        t2 = BaseNumTuple((5, 6, 7, 3))
        t3 = BaseNumTuple((-2, -4, -6, 0))
        self.assertEqual(t1 - t2, t3)

    def test_negating_a_tuple(self):
        t1 = BaseNumTuple((1, -2, 3, -4))
        t2 = BaseNumTuple((-1, 2, -3, 4))
        self.assertEqual(-t1, t2)

    def test_multiplying_a_tuple_by_a_scalar(self):
        t1 = BaseNumTuple((1, -2, 3, -4))
        t2 = BaseNumTuple((3.5, -7, 10.5, -14))
        t3 = BaseNumTuple((0.5, -1, 1.5, -2))
        self.assertAlmostEqual(3.5 * t1, t2)
        self.assertAlmostEqual(0.5 * t1, t3)

    def test_dividing_a_tuple_by_a_scalar(self):
        t1 = BaseNumTuple((1, -2, 3, -4))
        t2 = BaseNumTuple((0.5, -1, 1.5, -2))
        self.assertAlmostEqual(t1 / 2, t2)


if __name__ == "__main__":
    unittest.main()
