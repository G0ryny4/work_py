# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Было:

# my_list = [2, 3, 5, 9, 3]

# def sum_odd(input_list):
#     res = 0
#     for i in range(1, len(input_list), 2):
#         res += input_list[i]
#     return res    

# print(sum_odd(my_list))


# Стало:

my_list = [2, 3, 5, 9, 3]

res =[my_list[x] for x in range(len(my_list)-1) if x % 2 != 0]

print(f'сумма элементов списка, стоящих на нечётной позиции составляет {sum(list(res))}')