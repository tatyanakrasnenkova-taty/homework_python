# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

print("Введите номер плоскости для уточнения возможных координат")
ploskost = int (input ())

import math
math.inf

if ploskost == 1:
    print('x = [0, +', math.inf, ')')
    print('y = [0, +', math.inf, ')')
if ploskost == 2:
    print('x = [0, -', math.inf, ')')
    print('y = [0, +', math.inf, ')')
if ploskost == 3:
    print('x = [0, -', math.inf, ')')
    print('y = [0, -', math.inf, ')')
if ploskost == 4:
    print('x = [0, +', +math.inf, ')')
    print('y = [0, -', +math.inf, ')')