# Условие
# На вход подается: список целых чисел arr
# ● Задача
# Реализовать декларативную функцию, которая возвращает три числа:
# ○ Долю позитивных чисел
# ○ Долю нулей
# ○ Долю отрицательных чисел
# ● Решение: .. ?


def declarative_numbers(arr: list) -> (int, int, int):
    """
    Реализовать декларативную функцию, которая возвращает три числа:
    ○ Долю положительных чисел
    ○ Долю нулей
    ○ Долю отрицательных чисел
    :param arr:
    :return:
    """
    len_arr = len(arr)
    positive = sum(num > 0 for num in arr)
    zero = sum(num == 0 for num in arr)
    negative = sum(num < 0 for num in arr)
    return positive/len_arr, zero/len_arr, negative/len_arr


if __name__ == "__main__":
    arr = [-1, -4, 0, 4, 6]
    print(declarative_numbers(arr))
