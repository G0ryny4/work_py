# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:* - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def diff_max_min(my_list):
    fraction_list = []
    for item in my_list:
        if isinstance(item, float):
            fraction_list.append(round(abs(item) % 1, 5))

    max_value = max(fraction_list)
    print(f'Максимальное значение дробной части {max_value}')
    min_value = min(fraction_list)
    print(f'Миниимальное значение дробной части {min_value}')
    result = max_value - min_value
    return result

my_list = [1.1, 1.2, 3.1, 5, 10.01]
print(f'Список из вещественных чисел {my_list}')
print(f'Разница между и значением дробной части элементов {diff_max_min(my_list)}')