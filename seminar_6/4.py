# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# Было:

# def Input_numbers(inputText):
#     is_OK = False
#     while not is_OK:
#         try:
#             number = float(input(f"{inputText}"))
#             is_OK = True
#         except ValueError:
#             print("Это не число!")
#     return number


# def Sum_nums(num):
#     sum = 0
#     for i in str(num):
#         if i != ".":
#             sum += int(i)
#     return sum


# num = Input_numbers("Введите число: ")

# print(f"Сумма цифр = {Sum_nums(num)}")

# Стало:

from functools import reduce

my_num = float(input('Введите число: '))
if my_num < 0:
    my_num *= -1
Float_Num_Summ = reduce(lambda a, b: int(a)+int(b),
                        list(filter(lambda x: x != '.', str(my_num))))
print(f'Сумма чисел равна: {Float_Num_Summ}')