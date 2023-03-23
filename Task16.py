# Задача 16: Требуется вычислить, сколько раз
# встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
#     5
#     1 2 3 4 5
#     3
#     -> 1
import random


def input_num(message: str) -> int:
    input_error: bool = True
    while input_error:
        try:
            temp = int(input(message))
        except ValueError:
            print("Вы ввели не число!")
        else:
            input_error = False
            return temp


def random_list(size_l: int) -> list:
    return [random.randint(1, 10) for i in range(size_l)]


def search_x(l: list, x_l: int) -> int:
    return l.count(x_l)


size = input_num('Please input size of list: ')
n = random_list(size)
print(n)
x = input_num('Please input X for search: ')
print(f'We have {search_x(n, x)} X({x}) in list')
