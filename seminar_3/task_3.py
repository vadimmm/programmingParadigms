#  Контекст
# И наконец, последняя задача - по аналогии с кругом создать класс для треугольника и расчета его
# характеристик.
# ● Задача
# Реализовать дочерний от Shape класс Triangle, включая следующие работающие методы:
# ○ конструктор класса __init__ - метод инициализации класса.
# ○ get_area - метод для расчета площади
# ○ get_perimeter - метод для расчета периметра

# Task 1
class Shape:
    def get_area(self):
        pass

    def get_perimeter(self):
        pass


# Task 3
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        return (self.a * self.b) / 2

    def get_perimeter(self):
        return self.a + self.b + self.c
    