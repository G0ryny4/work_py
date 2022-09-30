# Реализовать алгоритм перемешивания списка.

from random import randrange, shuffle

original = [randrange(0, 11) for i in range(10)]
shffl = original [:]
shuffle(shffl)

print(original)
print(shffl)