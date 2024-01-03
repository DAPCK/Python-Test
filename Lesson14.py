# l = [1, 2, 3, 'hello', ['test', 10], 'world', True]
# l2 = list('hello')
# print(l,l2, sep='\n')

for i in range(1, 10):
    print(f'Умножение #{i}', end= '\n')
    for j in range(1, 10):
        print(f'\t{i} x {j} = {i * j}', end= '\t')

# # Создаем диапазон чисел для таблицы умножения
# numbers = range(1, 10)
#
# # Функция для вывода таблицы умножения
# def print_multiplication_table():
#     for i in numbers:
#         for j in numbers:
#             print(f"{i} x {j} = {i*j}", end="\t")
#         print("\n")
#
# # Вызываем функцию для вывода таблицы умножения
# print_multiplication_table()
