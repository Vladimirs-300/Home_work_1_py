# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('x = '))
y = int(input('y = '))


if x == 0 and y == 0:
    print('Не соответствует ТЗ')

if x > 0 and y > 0:
    print('Точка находится в плоскости 1')

if x < 0 and y > 0:
    print('Точка находится в плоскости 2')

if x < 0 and y < 0:
    print('Точка находится в плоскости 3')

if x > 0 and y < 0:
    print('Точка находится в плоскости 4')
