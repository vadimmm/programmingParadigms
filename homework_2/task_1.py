def multiplying(number):
    """
    Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
    :param number:
    :return:
    """
    for i in range(1, number + 1):
        print(f"{1} * {i} = {1 * i}")


multiplying(9)
