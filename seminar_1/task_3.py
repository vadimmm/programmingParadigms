# ● Условие
# На вход подается: список целых чисел arr
# ● Задача
# Реализовать императивную функцию, которая возвращает три числа:
# ○ Долю положительных чисел
# ○ Долю нулей
# ○ Долю отрицательных чисел
# ● Решение: .. ?


arr = [-1, -4, 0, 4, 6]


def imperative_numbers(arr) -> (int, int, int):
    """
    Реализовать императивную функцию, которая возвращает три числа:
    ○ Долю положительных чисел
    ○ Долю нулей
    ○ Долю отрицательных чисел
    :param arr:
    :return:
    """
    positive = 0
    zero = 0
    negative = 0
    len_arr = len(arr)
    for i in arr:
        if i > 0:
            positive += 1
        elif i == 0:
            zero += 1
        else:
            negative += 1
    return positive/len_arr, zero/len_arr, negative/len_arr


print(imperative_numbers(arr))
