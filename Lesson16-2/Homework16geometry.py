from abc import ABC, abstractmethod
from math import pi, sqrt

class Figure(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass


class Circle(Figure):
    def __init__(self, radius):
        self.__r = radius

    def area(self):
        return pi * self.__r ** 2

    def perimeter(self):
        return 2 * pi * self.__r


class Rectangle(Figure):
    def __init__(self, w, h):
        self.__w = w
        self.__h = h

    def area(self):
        return self.__w * self.__h

    def perimeter(self):
        return 2 * (self.__w + self.__h)


class Triangle(Figure):
    def __init__(self, side):
        self.__s = side

    def area(self):
        return (sqrt(3) / 4) * self.__s ** 2

    def perimeter(self):
        return 3 * self.__s

figures = [
    Circle(3),
    Rectangle(4, 5),
    Triangle(2)
]

for f in figures:
    print(f"{f.__class__.__name__}:")
    print(f"  Площа = {f.area():.2f}")
    print(f"  Периметр = {f.perimeter():.2f}\n")
