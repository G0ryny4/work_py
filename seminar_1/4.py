# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).



def checkCoordinates(quarter):
    quarter = int (input(f"Введите четверть: "))
    if quarter == 1:
        print(f"Диапазон точек в {quarter} четверти X > 0 и Y > 0")
    elif quarter == 2:
        print(f"Диапазон точек в {quarter} четверти X < 0 и Y > 0")
    elif quarter == 3:
        print(f"Диапазон точек в {quarter} четверти X < 0 и Y < 0")
    elif quarter == 4:
        print(f"Диапазон точек в {quarter} четверти X < 0 и Y < 0")
    



checkCoordinates(1)