import unittest

import rectangle

INVALID = [-5, -0.1, 0, "5", None, [5], True, float("nan"), float("inf")]


class TestRectangle(unittest.TestCase):

    def test_area_example_from_docs(self):
        self.assertEqual(rectangle.area(10, 5), 50)

    def test_area_swapped_sides(self):
        self.assertEqual(rectangle.area(5, 10), 50)

    def test_area_equal_sides(self):
        self.assertEqual(rectangle.area(4, 4), 16)

    def test_area_float_sides(self):
        self.assertAlmostEqual(rectangle.area(1.5, 2.5), 3.75)

    def test_perimeter_example_from_docs(self):
        self.assertEqual(rectangle.perimeter(10, 5), 30)

    def test_perimeter_swapped_sides(self):
        self.assertEqual(rectangle.perimeter(5, 10), 30)

    def test_perimeter_equal_sides(self):
        self.assertEqual(rectangle.perimeter(4, 4), 16)

    def test_perimeter_float_sides(self):
        self.assertAlmostEqual(rectangle.perimeter(1.5, 2.5), 8.0)

    def test_perimeter_very_different_sides(self):
        self.assertEqual(rectangle.perimeter(1, 10), 22)
        self.assertEqual(rectangle.perimeter(10, 1), 22)


    def test_area_invalid_first_side(self):
        for a in INVALID:
            with self.subTest(a=a):
                self.assertEqual(rectangle.area(a, 3), -1)

    def test_area_invalid_second_side(self):
        for b in INVALID:
            with self.subTest(b=b):
                self.assertEqual(rectangle.area(3, b), -1)

    def test_perimeter_invalid_first_side(self):
        for a in INVALID:
            with self.subTest(a=a):
                self.assertEqual(rectangle.perimeter(a, 3), -1)

    def test_perimeter_invalid_second_side(self):
        for b in INVALID:
            with self.subTest(b=b):
                self.assertEqual(rectangle.perimeter(3, b), -1)


if __name__ == "__main__":
    unittest.main()
