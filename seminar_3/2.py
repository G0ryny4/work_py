# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


import math

def multiplication_couples(arr):

    indx = len(arr)
    reslt = []
    inde = math.ceil(indx / 2)
    for i in range(inde):
        res = arr[i] * arr[(i + 1) * -1]
        reslt.append(res)
    return reslt

my_list1 = [2, 3, 4, 5, 6]
my_list2 = [2, 3, 5, 6]

print(multiplication_couples(my_list1))

