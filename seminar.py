#1.Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

#day = int(input('Введите число дня: '))
#if day>7 or day<1:
#    print('Ошибка')
#elif day==6 or day==7:
#    print('Выходной')
#else:
#    print('Не выходной')

#1.Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#for x in range(2):
#        for y in range(2):
#            for z in range(2):
#                print(not (x or y or z) == (not x and not y and not z))
#                print(x, y, z)

#2. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#x = int(input('Введите x: '))
#y = int(input('Введите y: '))
#if x == 0 and y == 0:
#    print('Error')
#if x == 0 and y!=0:
#    print('Error')
#if x!= 0 and y==0:
#    print('Error')
#if x > 0 and y > 0:
#     print('1')
#if x < 0 and y > 0:
#     print('2')
#if x < 0 and y < 0:
#     print('3')
#if x > 0 and y < 0:
#     print('4')

# 3. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# n = int(input('Введите число: '))
# if n < 1 or n > 4:
#     print('Error')
# elif n == 1:
#     print('x > 0 and y > 0')
# elif n == 2:
#     print('x < 0 and y > 0')
# elif n == 3:
#     print('x < 0 and y < 0')
# elif n == 4:
#     print('x > 0 and y < 0')

# 4. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

x1 = int(input('Введите координату х1: '))
y1 = int(input('Введите координату y1: '))
x2 = int(input('Введите координату х2: '))
y2 = int(input('Введите координату y2: '))
import math
sqrt = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2),2)
print(f'Расстояние: (A - ({x1}, {y1}) между B - ({x2}, {y2}) = {sqrt}')