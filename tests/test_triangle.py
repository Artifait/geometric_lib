import unittest

import triangle

INVALID = [-5, -0.1, 0, "5", None, [5], True, float("nan"), float("inf")]


class TestTriangle(unittest.TestCase):

    def test_area_example_from_docs(self):
        self.assertAlmostEqual(triangle.area(6, 4), 12.0)

    def test_area_swapped_args(self):
        self.assertAlmostEqual(triangle.area(4, 6), 12.0)

    def test_area_float(self):
        self.assertAlmostEqual(triangle.area(3.0, 5.0), 7.5)

    def test_area_odd_result(self):
        self.assertAlmostEqual(triangle.area(3, 3), 4.5)

    def test_perimeter_example_from_docs(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_perimeter_equilateral(self):
        self.assertEqual(triangle.perimeter(2, 2, 2), 6)

    def test_perimeter_isosceles(self):
        self.assertEqual(triangle.perimeter(5, 5, 8), 18)

    def test_perimeter_float(self):
        self.assertAlmostEqual(triangle.perimeter(1.5, 2.5, 3.0), 7.0)

    # --- невалидные данные: ожидается -1 ---
    def test_area_invalid_base(self):
        for base in INVALID:
            with self.subTest(base=base):
                self.assertEqual(triangle.area(base, 4), -1)

    def test_area_invalid_height(self):
        for h in INVALID:
            with self.subTest(height=h):
                self.assertEqual(triangle.area(6, h), -1)

    def test_perimeter_invalid_side_a(self):
        for a in INVALID:
            with self.subTest(a=a):
                self.assertEqual(triangle.perimeter(a, 4, 5), -1)

    def test_perimeter_invalid_side_b(self):
        for b in INVALID:
            with self.subTest(b=b):
                self.assertEqual(triangle.perimeter(3, b, 5), -1)

    def test_perimeter_invalid_side_c(self):
        for c in INVALID:
            with self.subTest(c=c):
                self.assertEqual(triangle.perimeter(3, 4, c), -1)

    def test_perimeter_triangle_does_not_exist(self):
        for sides in [(1, 2, 10), (1, 2, 3), (10, 1, 2), (2, 10, 1)]:
            with self.subTest(sides=sides):
                self.assertEqual(triangle.perimeter(*sides), -1)


if __name__ == "__main__":
    unittest.main()
