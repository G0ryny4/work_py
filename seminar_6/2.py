# Напишите программу, удаляющую из текста все слова, содержащие "абв".

# Было:

# txt = input("Введите текст через пробел:\n")
# print(f"Исходный текст: {txt}")
# find_txt = "абв"
# lst = [i for i in txt.split() if find_txt not in i]
# print(f'Результат: {" ".join(lst)}')

# Стало:

stroka = 'шла абвгдейка в магазин и абвашла весь магабвин'
sorted_list = [x for x in stroka.split() if "абв" not in x]
list_sorted = " ".join(sorted_list)
print(list_sorted)