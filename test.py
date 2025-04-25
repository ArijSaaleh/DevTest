import unittest
from Calculate import Circle, Triangle, ShapeFactory
from math import pi


class TestCalculate(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(1)
        self.assertAlmostEqual(circle.area(), pi)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)

    def test_triangle_right_angle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

    def test_triangle_not_right_angle(self):
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right_triangle())

    def test_factory_circle(self):
        shape = ShapeFactory.create('circle', radius=2)
        self.assertAlmostEqual(shape.area(), pi * 4)

    def test_factory_triangle(self):
        shape = ShapeFactory.create('triangle', a=3, b=4, c=5)
        self.assertAlmostEqual(shape.area(), 6.0)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 10)

    def test_unknown_shape(self):
        with self.assertRaises(ValueError):
            ShapeFactory.create('square', side=2)


if __name__ == '__main__':
    unittest.main()
