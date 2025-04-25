from math import sqrt, pi, isclose
from abc import ABC, abstractmethod

# This code defines a base class Shape and two derived classes Circle and Triangle.
# It also includes a factory class ShapeFactory to create instances of these shapes.
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

#class circle
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2

#class triangle 
class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Invalid triangle sides.")
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_triangle(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2, rel_tol=1e-9)

#class shape factory
# This factory class is responsible for creating instances of the shapes.
# It uses the factory method pattern to encapsulate the instantiation logic.
class ShapeFactory:
    @staticmethod
    def create(shape_type: str, **kwargs) -> Shape:
        shape_type = shape_type.lower()
        if shape_type == 'circle':
            return Circle(kwargs['radius'])
        elif shape_type == 'triangle':
            return Triangle(kwargs['a'], kwargs['b'], kwargs['c'])
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")
