def sort_list_declarative(numbers: list) -> list:
    """
    Функция в декларативном стиле. Процедура для сортировки числа в списке в порядке убывания.
    :param numbers: Список чисел
    :return: Отсортированный список
    """
    if not numbers:
        raise ValueError("Список пуст")
    return sorted(numbers, reverse=True)


if __name__ == '__main__':
    numbers = [0, 1, 9, 2, 8, 3, 7, 4, 6, 5]
    print(sort_list_declarative(numbers))
