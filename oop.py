# figure calc
# вызов должен быть таким: calcFigure.rectangle.perimetr(передаваемые значения)
import math


class Shape:
    title = 'Фигура'

    def area(self):
        """Вычисление площади"""

    def perimetr(self):
        """Вычисление периметра"""


class Triangle(Shape):
    title = 'Треугольник'

    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        """Рассет площади треугольника"""
        p = self.perimetr() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def perimetr(self):
        """Расчет периметра треугольника"""
        return self.a + self.b + self.c

    def median(self):
        """Вычисляем медиану треугольника"""
        return .5 * (2 * (self.b ** 2) + 2 * (self.c ** 2) - self.a ** 2) ** .5


class Rectangle(Shape):
    title = 'Прямоугольник'

    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def area(self):
        """Рассет площади Прямоугольника"""
        return self.a * self.b

    def perimetr(self):
        """Расчет периметра Прямоугольника"""
        return 2 * (self.a + self.b)


class Circle(Shape):
    title = 'Круг'

    def __init__(self, r):
        super().__init__()
        self.r = r

    def area(self):
        """Рассет площади Круга"""
        return math.pi * self.r ** 2

    def perimetr(self):
        """Расчет периметра Круга"""
        return 2 * self.r * math.pi


class Rommb(Rectangle):
    title = 'Ромб'


class Trapezoid(Shape):
    title = 'Трапеция'

    def __init__(self, a, b, c, d):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def area(self):
        """Рассет площади треугольника"""
        h = (self.c ** 2 - (((self.a - self.b) ** 2 + self.c ** 2 - self.d ** 2) / (2 * (self.a - self.b))) ** 2) ** .5
        return ((self.a + self.b) / 2) * h

    def perimetr(self):
        """Расчет периметра треугольника"""
        return self.a + self.b + self.c + self.d


class Sphere(Circle):
    title = 'Сфера'

    def area(self):
        """Рассет площади сферы"""
        return self.r ** 2 * 4 * math.pi


class Cube(Rectangle):
    title = 'Куб'

    def area(self):
        """Рассет площади куба"""
        return (self.a + self.b) * 6

    def perimetr(self):
        """Расчет периметра куба"""
        return self.a ** 2 * 6


class Cylinder(Shape):
    title = 'Цилиндр'

    def __init__(self, r, h):
        self.h = h
        self.r = r

    def area(self):
        """Рассет площади цилиндра"""
        return 2 * math.pi * self.r * self.h


if __name__ == "__main__":
    pass
    # print(FigureCalc.triangle(3, 4, 5).perimetr())
    # print(romb.area())
    # print(triangle.area())
    # print(triangle.median())
