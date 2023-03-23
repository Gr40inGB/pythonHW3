# *****(4)Напишите функцию, которая принимает словарь с параметрами и
# возвращает строку запроса, сформированную из отсортированных
# в лексикографическом порядке параметров.
#
# Пример:
# Код print(query({'course': 'python', 'lesson': 2, 'challenge': 17})) должен возвращать строку:
# challenge=17&course=python&lesson=2

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
