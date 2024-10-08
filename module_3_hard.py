data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", [4]]
# print(len(data_structure))
j = 0
while j < len(data_structure):
    print(data_structure[j])
#    print(isinstance(data_structure[j], list))
    k = 0
    if isinstance(data_structure[j], list):
        for i in data_structure[j]:
            k = k + i
    else:
        print('stop')
    print(k, 'расчет суммы первого блока')
    k = k + len(data_structure[j])
    print(k, 'рсчет суммы с длинной блока')

    j = j + 1




# x = [1, 2, 3]
# print(isinstance(x, (int, float, list, dict, str)))  # Output: True
# n = len(x)
# print(type(n))
# i = x[0]
# print(type(i))
# print(i)
# k = 0
# if isinstance(x, list):
#     for i in x:
#         k = k + i
# else:
#     print('stop')
# print(k)
# k = k + len(x)
# print(k)



# y = "Hello"
# print(isinstance(y, (int, str)))  # Output: True
#
# z = 3.14
# print(isinstance(z, (int, str)))  # Output: False

# data_structure = [
# [1, 2, 3],                              # список, list, int
# {'a': 4, 'b': 5},                       # словари dict, str
# (6, {'cube': 7, 'drum': 8}),            # словари
# "Hello",
# ((), [{(2, 'Urban', ('Urban2', 35))}])   # кортеж
# ]
# Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые). Тем не менее, даже после сна, его код остался рабочим и выглядел следующим образом:
#
# data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?"
# Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по-разному.
#
# Ученику пришлось каждый раз использовать индексацию и обращение по ключам - универсального решения для таких структур он не нашёл.
#
# Помогите сокурснику осуществить его задумку.
#
# Что должно быть подсчитано:
#
#     Все числа (не важно, являются они ключами или значениям или ещё чем-то).
#     Все строки (не важно, являются они ключами или значениям или ещё чем-то)
#
#
# Для примера, указанного выше, расчёт вёлся следующим образом:
# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
#
# Входные данные (применение функции):
# data_structure = [
# [1, 2, 3],
# {'a': 4, 'b': 5},
# (6, {'cube': 7, 'drum': 8}),
# "Hello",
# ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# result = calculate_structure_sum(data_structure)
# print(result)
#
#
# Выходные данные (консоль):
# 99
#
#
# Примечания (рекомендации):
#
#     Весь подсчёт должен выполняться одним вызовом функции.
#     Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
#     Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
#     Для определения типа данного используйте функцию isinstance.