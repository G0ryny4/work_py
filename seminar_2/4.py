# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов
# на указанных позициях. Позиции хранятся в списке positions - создайте этот список (например:
# positions = [1, 3, 6]).


def Input_numbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Введите целое число ")
    return number


num = Input_numbers("Введите число: ")
pos1 = Input_numbers("Введите индекс первого числа: ")
pos2 = Input_numbers("Введите индекс второго числа: ")
pos3 = Input_numbers("Введите индекс третьего числа: ")


def New_list(num, n1, n2, n3):
    sequence = []
    positions = [n1, n2, n3]
    result = 1
    for i in range(-num, num + 1):
        sequence.append(i)
    for n in positions:
        result *= sequence[n]
    return print(f' В списке {sequence} произведение элементов на позициях {n1}, {n2}, {n3}  = {result}')        

    
New_list(num, pos1, pos2, pos3)

