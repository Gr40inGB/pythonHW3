# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к
# заданному числу X. Пользователь в первой строке вводит натуральное число N –
# количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# # *Пример:*
#  5
#  1 2 3 4 5
#  6
#  -> 5

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


def search_near(l: list, x_l: int) -> int:
    near = l[0]
    for i in l:
        if abs(abs(x_l) - abs(i)) < abs(abs(x_l) - abs(near)):
            near = i
    return near


size = input_num('Please input size of list: ')
n = random_list(size)
print(n)
x = input_num('Please input X for search: ')
print(f'We find nearest for {x} number  - {search_near(n, x)}')
