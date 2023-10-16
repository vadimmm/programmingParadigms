# Контекст
# Теперь, когда у вас есть абстрактный класс Shape, ваша следующая задача - получить класс Circle.
# ● Задача
# Реализовать дочерний от Shape класс Circle, включая следующие работающие методы:
# ○ конструктор класса __init__ - метод инициализации класса Circle.
# ○ get_area - метод для расчета площади круга
# ○ get_perimeter - метод для расчета периметра окружности


import math


class Shape:
    def get_area(self):
        pass

    def get_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.radius = r
        self.pi = math.pi

    def get_area(self):
        return self.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * (self.pi * self.radius)

    def get_radius(self):
        return self.radius

    @property
    def radius(self):
        return self.radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        