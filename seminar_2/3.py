# Задать список из n чисел последовательности (1+ 1/n)^n и вывести на экран их сумму.



def Input_numbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Введите целое число ")
    return number


def Sequence(n):
    if n > 0:
        return (1 + 1 / n) ** n
   


num = Input_numbers("Введите число: ")

seqlist = []
for e in range(1, num + 1):
    list.append(Sequence(e))

print(f"Последовательность из {num} чисел:  {seqlist}")