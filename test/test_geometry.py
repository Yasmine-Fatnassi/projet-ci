import unittest
import math
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from geometry import rectangle_area, rectangle_perimeter, circle_area, circle_circumference

class TestGeometricFunctions(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(5, 10), 50)
        self.assertEqual(rectangle_area(0, 10), 0)
        self.assertEqual(rectangle_area(0, 0), 0)
        self.assertAlmostEqual(rectangle_area(5.5, 4.2), 23.1, places=1)
    
    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(5, 10), 30)
        self.assertEqual(rectangle_perimeter(0, 10), 20)
        self.assertEqual(rectangle_perimeter(0, 0), 0)
        self.assertAlmostEqual(rectangle_perimeter(5.5, 4.2), 19.4, places=1)

    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(5), math.pi * 25, places=7)
        self.assertEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.5), math.pi * 6.25, places=7)

    def test_circle_circumference(self):
        self.assertAlmostEqual(circle_circumference(5), 2 * math.pi * 5, places=7)
        self.assertEqual(circle_circumference(0), 0)
        self.assertAlmostEqual(circle_circumference(2.5), 2 * math.pi * 2.5, places=7)

if __name__ == '__main__':
    unittest.main()

