def sort_list_imperative(numbers: list) -> list:
    """
    Функция в императивном стиле. Процедура для сортировки числа в списке в порядке убывания.
    Можно использовать любой алгоритм сортировки.
    :param numbers: Список чисел
    :return: Отсортированный список
    """
    if not numbers:
        raise ValueError("Список пуст")
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


if __name__ == '__main__':
    numbers = [0, 1, 9, 2, 8, 3, 7, 4, 6, 5]
    print(sort_list_imperative(numbers))
