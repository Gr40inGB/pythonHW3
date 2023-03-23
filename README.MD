 Задача 16: Требуется вычислить, сколько раз
 встречается некоторое число X в массиве A[1..N].
 Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
 В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
 *Пример:*
     5
     1 2 3 4 5
     3
     -> 1
 ```python
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
 ```
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к
заданному числу X. Пользователь в первой строке вводит натуральное число N –
количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
Последняя строка содержит число X
 *Пример:*
 5
 1 2 3 4 5
 6
 -> 5
```python
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
```
Задача 20:  В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка;
B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков;
Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу,
которая вычисляет стоимость введенного пользователем слова. Будем считать,
что на вход подается только одно слово, которое содержит либо только английские,
либо только русские буквы.

Пример: ноутбук 12

```python
def word_cost(w: str) -> None:
    d = {'AEIOULNSTRАВЕИНОРСТ': 1,
         'DGДКЛМПУ': 2,
         'BCMPБГЁЬЯ': 3,
         'FHVWYЙЫ': 4,
         'KЖЗХЦЧ': 5,
         'JXШЭЮ': 8,
         'QZФЩЪ': 10}

    cost = 0
    for ch in w:
        if ch.isalpha():
            for keys in d:
                if ch in keys:
                    cost += d[keys]
    print('cost of your word -', cost)

word_cost(input('Please input word: ').upper())
```
*****(3)Напишите программу, которая принимает на вход две строки и
определяет, являются ли они анаграммами. Знаки препинания,
пробелы и регистр при этом игнорируются.
Пример ввода:
Цари, вино и сало.
Лисица и ворона.
Пример вывода:
YES
```python
def anagram(s_1: str, s_2: str) -> bool:
    for c1 in s_1:
        if c1.isalpha():
            if s_1.count(c1) != s_2.count(c1):
                return False
    return True

s1 = input('Please input 1 string: ').upper()
s2 = input('Please input 2 string: ').upper()

if anagram(s1, s2):
    print('Yes')
else:
    print('No')
```
*****(4)Напишите функцию, которая принимает словарь с параметрами и
возвращает строку запроса, сформированную из отсортированных
в лексикографическом порядке параметров.

Пример:
Код print(query({'course': 'python', 'lesson': 2, 'challenge': 17})) должен возвращать строку:
challenge=17&course=python&lesson=2
```python
def query(d: dict) -> str:
    s = []
    for key, value in d.items():
        s.append(f'{str(key)}={str(value)}')
    s.sort()
    text = ''
    for w in s[:-1]:
        text += w + '&'
    return text + str(s[-1])

print(query({'course': 'python', 'lesson': 2, 'challenge': 17, 'geekBrains': 2023}))
```