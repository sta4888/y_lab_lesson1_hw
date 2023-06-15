import math
import os
import sys


class Shape:
    """
    Класс родитель - Фигура
    """
    title = 'Фигура'

    def area(self):
        """Вычисление площади"""

    def perimetr(self):
        """Вычисление периметра"""


class Triangle(Shape):
    title = 'Треугольник'

    def __init__(self, a_side: float, b_side: float, c_side: float):
        super().__init__()
        self.a_side = a_side
        self.b_side = b_side
        self.c_side = c_side

    def area(self) -> float:
        """
        Расет площади треугольника
        :return: -> float результат расчета площади треугольника
        """
        p = self.perimetr() / 2  # для рассчета площади необходимо сперва периметр поделить пополам
        return (p * (p - self.a_side) * (p - self.b_side) * (p - self.c_side)) ** 0.5

    def perimetr(self) -> float:
        """
        Расчет периметра треугольника
        :return: -> float результат расчета периметра треугольника
        """
        return self.a_side + self.b_side + self.c_side

    def median(self) -> float:
        """
        Вычисляем медиану треугольника
        :return: -> float вычисление медианы
        """
        return .5 * (2 * (self.b_side ** 2) + 2 * (self.c_side ** 2) - self.a_side ** 2) ** .5

    @staticmethod
    def get_area(a_side: float, b_side: float, c_side: float) -> float:
        """
        Расет площади треугольника
        :return: -> float результат расчета площади треугольника
        """
        p = Triangle.get_perimetr(a_side, b_side,
                                  c_side) / 2  # для рассчета площади необходимо сперва периметр поделить пополам
        return (p * (p - a_side) * (p - b_side) * (p - c_side)) ** 0.5

    @staticmethod
    def get_perimetr(a_side: float, b_side: float, c_side: float) -> float:
        """
        Расчет периметра треугольника
        :return: -> float результат расчета периметра треугольника
        """
        return a_side + b_side + c_side

    @staticmethod
    def get_median(a_side: float, b_side: float, c_side: float) -> float:
        """
        Вычисляем медиану треугольника
        :return: -> float вычисление медианы
        """
        return .5 * (2 * (b_side ** 2) + 2 * (c_side ** 2) - a_side ** 2) ** .5

    @staticmethod
    def print_figure():
        r = """
               /\\
              /  \\
             /    \\
            /      \\
           /        \\
          /          \\
         /            \\
        /              \\
       /                \\
      /                  \\
     /                    \\
    /______________________\\
        """
        return r

class Rectangle(Shape):
    title = 'Прямоугольник'

    def __init__(self, a_side: float, b_side: float):
        super().__init__()
        self.a = a_side
        self.b = b_side

    def area(self):
        """Рассет площади Прямоугольника"""
        return self.a * self.b

    def perimetr(self):
        """Расчет периметра Прямоугольника"""
        return 2 * (self.a + self.b)

    @staticmethod
    def get_perimetr(a_side: float, b_side: float):
        """
        Расчет периметра прямоугольника
        :param a_side: -> int сторона
        :param b_side: -> int сторона
        :return: -> int периметр
        """
        return a_side * b_side

    @staticmethod
    def get_area(a_side, b_side):
        """
        Расчет площади прямоугольника
        :param a_side: -> int сторона
        :param b_side: -> int сторона
        :return: -> int площадь
        """
        return 2 * (a_side + b_side)

    @staticmethod
    def print_figure():
        r = """
        *--------------*
        |              |
        |              |
        |              |
        |              |
        |              |
        |              |
        *--------------*
        """
        return r


class Circle(Shape):
    title = 'Круг'

    def __init__(self, radius: float):
        super().__init__()
        self.radius = radius

    def area(self) -> float:
        """
        Расет площади Круга
        :return: -> float возвращает площадь от переданного радиуса
        """
        return math.pi * self.radius ** 2

    def perimetr(self) -> float:
        """
        Расчет периметра Круга
        :return: -> float
        """
        return 2 * self.radius * math.pi

    @staticmethod
    def get_area(radius: float) -> float:
        """
        Расет площади Круга
        :return: -> float возвращает площадь от переданного радиуса
        """
        return math.pi * radius ** 2

    @staticmethod
    def get_perimetr(radius: float) -> float:
        """
        Расчет периметра Круга
        :return: -> float
        """
        return 2 * radius * math.pi

    @staticmethod
    def print_figure():
        r = """
         , - ~ ~ ~ - ,
     , '               ' ,
   ,                       ,
  ,                         ,
 ,                           ,
 ,                           ,
 ,                           ,
  ,                         ,
   ,                       ,
     ,                  , '
       ' - , _ _ _ ,  '


        """
        return r

class Rommb(Rectangle):
    title = 'Ромб'

    @staticmethod
    def print_figure():
        return "Пока нет фигуры в базе =("

class Trapezoid(Shape):
    """
    Необходимо передать все 4 стороны
    """
    title = 'Трапеция'

    def __init__(self, a_side: float, b_side: float, c_side: float, d_side):
        super().__init__()
        self.a_side = a_side
        self.b_side = b_side
        self.c_side = c_side
        self.d_side = d_side

    def area(self) -> float:
        """
        Расет площади трапеции
        :return: -> float расчет площади трапеции, сперва вычисляем высоту и уже после вычисляем площадь
        """
        height = (self.c_side ** 2 - (((self.a_side - self.b_side) ** 2 + self.c_side ** 2 - self.d_side ** 2) / (
                2 * (self.a_side - self.b_side))) ** 2) ** .5
        return ((self.a_side + self.b_side) / 2) * height

    def perimetr(self) -> float:
        """
        Расчет периметра трапеции
        :return: -> float
        """
        return self.a_side + self.b_side + self.c_side + self.d_side

    @staticmethod
    def get_area(a_side: float, b_side: float, c_side: float, d_side):
        """
        Расет площади трапеции
        :return: -> float расчет площади трапеции, сперва вычисляем высоту и уже после вычисляем площадь
        """
        height = (c_side ** 2 - (
                ((a_side - b_side) ** 2 + c_side ** 2 - d_side ** 2) / (2 * (a_side - b_side))) ** 2) ** .5
        return ((a_side + b_side) / 2) * height

    @staticmethod
    def get_perimetr(a_side: float, b_side: float, c_side: float, d_side):
        """
        Расчет периметра трапеции
        :return: -> float
        """
        return a_side + b_side + c_side + d_side

    @staticmethod
    def print_figure():
        return "Пока нет фигуры в базе =("

class Sphere(Circle):
    title = 'Сфера'

    def area(self) -> float:
        """
        Расет площади сферы
        :return: -> float
        """
        return self.radius ** 2 * 4 * math.pi

    @staticmethod
    def get_area(radius: float) -> float:
        """
        Расет площади сферы
        :return: -> float
        """
        return radius ** 2 * 4 * math.pi
    @staticmethod
    def print_figure():
        r = """


                      ░░░░░░░░░░░░
                  ░░░░░░░░░░░░░░░░░░░░
                ░░▒▒░░░░░░░░░░░░░░░░░░░░
              ░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░
            ░░▒▒▒▒░░░░░░░░░░░░░░    ░░░░░░░░
            ░░▒▒▒▒░░░░░░░░░░░░        ░░░░░░
          ░░▓▓▒▒▒▒░░░░░░░░░░          ░░░░░░░░
          ░░▓▓▒▒▒▒░░░░░░░░░░░░░░    ░░░░░░░░░░
          ░░▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░
          ░░▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░
          ░░▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░
          ░░▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░
            ░░▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░
            ░░▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒░░
              ░░▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
                ░░▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░
                  ░░░░▓▓▓▓▓▓▓▓▓▓▒▒░░░░
                      ░░░░░░░░░░░░

        """
        return r

class Cube(Rectangle):
    title = 'Куб'

    def area(self) -> float:
        """Расет площади куба"""
        return (self.a + self.b) * 6

    def perimetr(self) -> float:
        """Расчет периметра куба"""
        return self.a ** 2 * 6

    @staticmethod
    def get_area(a_side: float, b_side: float) -> float:
        """Расет площади куба"""
        return (a_side + b_side) * 6

    @staticmethod
    def get_perimetr(a_side: float, b_side: float) -> float:
        """Расчет периметра куба"""
        return a_side ** 2 * 6

    @staticmethod
    def print_figure():
        r = """
            +-------------+
          /|             /|
         / |            / |
        *--+-----------*  |
        |  |           |  |
        |  |           |  |
        |  |           |  |
        |  +-----------+--+
        | /            | /
        |/             |/
        *--------------*
        """
        return r

class Cylinder(Shape):
    title = 'Цилиндр'

    def __init__(self, radius: float, height: float):
        self.height = height
        self.radius = radius

    def area(self) -> float:
        """Рассет площади цилиндра"""
        return 2 * math.pi * self.radius * self.height

    @staticmethod
    def get_area(radius: float, height: float) -> float:
        """Рассет площади цилиндра"""
        return 2 * math.pi * radius * height

    @staticmethod
    def print_figure():
        return "Пока нет фигуры в базе =("

class Calculate:
    rectangle = Rectangle
    triangle = Triangle
    circle = Circle
    rommb = Rommb
    trapezoid = Trapezoid
    sphere = Sphere
    cube = Cube
    cylinder = Cylinder


def print_any():
    sys.exit()


def run_calc(figure: str) -> None:
    numb = figure[0]  # номер фигуры
    params = [float(n) for n in figure[1:].split()]  # параметры передаваемые в методы

    OPTIONS = {
        '1': {
            'title': Rectangle.title,
            'calculation_area': Calculate.rectangle.get_area,
            'calculation_perimetr': Calculate.rectangle.get_perimetr,
            'draw': Calculate.rectangle.print_figure
        },
        '2': {
            'title': Triangle.title,
            'calculation_area': Calculate.triangle.get_area,
            'calculation_perimetr': Calculate.triangle.get_perimetr,
            'draw': Calculate.triangle.print_figure
        },
        '3': {
            'title': Circle.title,
            'calculation_area': Calculate.circle.get_area,
            'calculation_perimetr': Calculate.circle.get_perimetr,
            'draw': Calculate.circle.print_figure
        },
        '4': {
            'title': Rommb.title,
            'calculation_area': Calculate.rommb.get_area,
            'calculation_perimetr': Calculate.rommb.get_perimetr,
            'draw': Calculate.rommb.print_figure
        },
        '5': {
            'title': Trapezoid.title,
            'calculation_area': Calculate.trapezoid.get_area,
            'calculation_perimetr': Calculate.trapezoid.get_perimetr,
            'draw': Calculate.trapezoid.print_figure
        },
        '6': {
            'title': Sphere.title,
            'calculation_area': Calculate.sphere.get_area,
            'calculation_perimetr': Calculate.sphere.get_perimetr,
            'draw': Calculate.sphere.print_figure
        },
        '7': {
            'title': Cube.title,
            'calculation_area': Calculate.cube.get_area,
            'calculation_perimetr': Calculate.cube.get_perimetr,
            'draw': Calculate.cube.print_figure
        },
        '8': {
            'title': Cylinder.title,
            'calculation_area': Calculate.cylinder.get_area,
            'calculation_perimetr': Calculate.cylinder.get_area,
            'draw': Calculate.cylinder.print_figure
        },
        '0': {
            'title': "Выход",
            'calculation_area': print_any
        }
    }

    print(OPTIONS[numb]['title'])

    try:
        print(f"Площадь: {OPTIONS[numb]['calculation_area'](*params)} Периметр: {OPTIONS[numb]['calculation_perimetr'](*params)}")
        print(OPTIONS[numb]['draw']())
    except TypeError:
        print(OPTIONS[numb]['title'], ": Вы передаете не верное количество сторон")

    q = input("Продолжить? Y/n")
    if q.upper() == 'N':
        print(OPTIONS['0']['calculation_area']())

if __name__ == "__main__":
    os.system('clear')
    print('Калькулятор геометрических фигур')
    print('для решения введите номер фигуры и паредаваемые параметры')

    while True:
        print(' (1) Квадрат/ прямоугольник\n' +
              ' (2) Треугольник\n' +
              ' (3) Круг\n' +
              ' (4) Ромб\n' +
              ' (5) Трапеция\n' +
              ' (6) Сфера\n' +
              ' (7) Куб\n' +
              ' (8) Цилиндр\n' +
              ' (0) Выход их программы')
        run_calc(input())


