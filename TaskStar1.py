# *****(3)Напишите программу, которая принимает на вход две строки и
# # определяет, являются ли они анаграммами. Знаки препинания,
# # пробелы и регистр при этом игнорируются.
# # Пример ввода:
# # Цари, вино и сало.
# # Лисица и ворона.
# # Пример вывода:
# # YES
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

