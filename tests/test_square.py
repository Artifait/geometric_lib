import unittest

import square

INVALID = [-5, -0.1, 0, "5", None, [5], True, float("nan"), float("inf")]


class TestSquare(unittest.TestCase):

    def test_area_example_from_docs(self):
        self.assertEqual(square.area(4), 16)

    def test_area_float(self):
        self.assertAlmostEqual(square.area(2.5), 6.25)

    def test_area_unit(self):
        self.assertEqual(square.area(1), 1)

    def test_perimeter_example_from_docs(self):
        self.assertEqual(square.perimeter(4), 16)

    def test_perimeter_float(self):
        self.assertAlmostEqual(square.perimeter(2.5), 10.0)

    def test_perimeter_unit(self):
        self.assertEqual(square.perimeter(1), 4)

    def test_area_and_perimeter_differ_for_side_3(self):
        # a=3: S=9, P=12 — ловит перепутанные формулы
        self.assertEqual(square.area(3), 9)
        self.assertEqual(square.perimeter(3), 12)

    def test_area_invalid(self):
        for a in INVALID:
            with self.subTest(a=a):
                self.assertEqual(square.area(a), -1)

    def test_perimeter_invalid(self):
        for a in INVALID:
            with self.subTest(a=a):
                self.assertEqual(square.perimeter(a), -1)


if __name__ == "__main__":
    unittest.main()
