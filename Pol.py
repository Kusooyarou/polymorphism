from abc import ABC, abstractmethod

class GeometricFigures(object):
    @abstractmethod
    def get_perimeter(self):
        pass

class Triangle(GeometricFigures):
    #all sides are 0 by default because no shape exists yet when created
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return f'периметр равен {self.a + self.b + self.c}'

    def __str__(self):
        return f'Треугольник со сторонами {self.a}, {self.b}, {self.c}'

class Square(GeometricFigures):
    #all sides are 0 by default because no shape exists yet when created
    def __init__(self, a=0):
        self.a = a

    def get_perimeter(self):
        return f'периметр равен {self.a * 4}'

    def __str__(self):
        return f'Квадрат со стороной {self.a}'

class Rectangle(GeometricFigures):
    #all sides are 0 by default because no shape exists yet when created
    def __init__(self, h=0, w=0):
        self.h = h
        self.w = w

    def get_perimeter(self):
        return f'периметр равен {(self.h + self.w) * 2}'

    def __str__(self):
        return f'Прямоугольник со сторанами {self.h}, {self.w}'

figures = [Triangle(1,2,3), Triangle(4,5,6),
           Square(10), Square(20),
           Rectangle(6,7), Rectangle(7,8)]

for figure in figures:
    print(figure, figure.get_perimeter())
