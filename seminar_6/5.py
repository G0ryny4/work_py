# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# Было:

# def inputNumbers(x):
#     xyz = ["X", "Y", "Z"]
#     a = []
#     for i in range(x):
#         a.append(input(f"Введите значение {xyz[i]}: "))
#     return a


# def checkPredicate(x):
#     left = not (x[0] or x[1] or x[2])
#     right = not x[0] and not x[1] and not x[2]
#     result = left == right
#     return result


# statement = inputNumbers(3)

# if checkPredicate(statement) == True:
#     print(f"Утверждение истинно")
# else:
#     print(f"Утверждение ложно")

# Стало:

print('Введите X, Y, Z через пробел:')
xyz_List = list(map(int, input().split(' ')))

statement = (lambda xyz: True if (not (xyz[0] or xyz[1] or xyz[2])) == (
    not xyz[0] and not xyz[1] and not xyz[2]) else False)(xyz_List)

if statement:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")