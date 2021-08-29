"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая принимает список целых чисел и возвращает минимальное

Нельзя пользоваться функциями sorted, list.sort, min, max

ПРИМЕРЫ
--------------------------------------------------------------------------------
min_in_list([1, 2, 3, -2, 3, 5]) -> -2
min_in_list([7, 2, 4, 6, 1, 4]) -> 1
"""


def min_in_list(some_list: list) -> int:
    length = len(some_list)
    if length == 1:
        return some_list[0]
    elif length == 0:
        return None
    min_value = some_list[0]
    for i in range(1, length):
        if some_list[i] < min_value:
            min_value = some_list[i]
    return min_value


if __name__ == '__main__':
    assert min_in_list([1, -1, 5, 7, -2, 4]) == -2
    print('Решено!')
