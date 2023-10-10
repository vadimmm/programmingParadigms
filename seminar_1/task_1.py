# Контекст
# Предположим, что нам хочется для любого массива чисел array и любого числа target узнать содержится
# ли target в array. Такую процедуру будем называть поиском.
# Задача
# Реализовать императивную функцию поиска элементов на языке Python.
# Решение: .. ?


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def search(array, target):
    """
    для любого массива чисел array и любого числа target узнать содержится ли target в array.
    :param array:
    :param target:
    :return:
    """
    return target in array


print(search(array, 55))
