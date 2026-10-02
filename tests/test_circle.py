import math
import unittest

import circle

INVALID = [-5, -0.1, 0, "5", None, [5], True, float("nan"), float("inf")]


class TestCircle(unittest.TestCase):

    def test_area_example_from_docs(self):
        self.assertAlmostEqual(circle.area(5), 78.5398, places=4)

    def test_area_int_radius(self):
        self.assertAlmostEqual(circle.area(2), 4 * math.pi)

    def test_area_float_radius(self):
        self.assertAlmostEqual(circle.area(0.5), 0.25 * math.pi)

    def test_area_returns_float(self):
        self.assertIsInstance(circle.area(5), float)

    def test_perimeter_example_from_docs(self):
        self.assertAlmostEqual(circle.perimeter(5), 31.4159, places=4)

    def test_perimeter_int_radius(self):
        self.assertAlmostEqual(circle.perimeter(1), 2 * math.pi)

    def test_perimeter_float_radius(self):
        self.assertAlmostEqual(circle.perimeter(0.5), math.pi)

    def test_perimeter_returns_float(self):
        self.assertIsInstance(circle.perimeter(5), float)


    def test_area_invalid(self):
        for r in INVALID:
            with self.subTest(r=r):
                self.assertEqual(circle.area(r), -1)

    def test_perimeter_invalid(self):
        for r in INVALID:
            with self.subTest(r=r):
                self.assertEqual(circle.perimeter(r), -1)


if __name__ == "__main__":
    unittest.main()
