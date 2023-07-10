"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers: int) -> [int]:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    [1, 4, 25, 49]
    """
    return [num ** 2 for num in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_even(number: int) -> bool:
    return number % 2 == 0


def is_odd(number: int) -> bool:
    return number % 2 != 0


def is_prime(number: int) -> bool:
    if number < 0:
        raise BaseException
    elif number <= 2:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def filter_numbers(numbers: [int], only_type: str | None) -> [int]:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    [2, 4]
    """
    if only_type == ODD:
        func = is_odd
    elif only_type == EVEN:
        func = is_even
    elif only_type == PRIME:
        func = is_prime
    return list(filter(func, numbers))