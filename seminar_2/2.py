# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ]


def Input_numbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Введите целое число ")
    return number


def Mult(n):
    if n == 1:
        return 1
    else:
        return n * Mult(n - 1)


num = Input_numbers("Введите число: ")

list = []
for e in range(1, num + 1):
    list.append(Mult(e))

print(f"Произведения чисел от 1 до {num}:  {list}")