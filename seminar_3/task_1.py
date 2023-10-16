#  Контекст
# Предположим, что мы хотим написать программу для исследования геометрических фигур. Для того
# чтобы это сделать мы решили начать с создания абстрактного класса - “Фигура”.
# ● Задача
# Реализовать класс Shape, содержащий пустые методы get_area и get_perimeter. Использовать библиотеку
# абстрактных классов “ABC” в данном случае - не обязательно.



from abc import ABCMeta, abstractmethod


class Shape:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass