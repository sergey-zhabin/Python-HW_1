# # 1 Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# # Пример:
# # - 6 -> да
# # - 7 -> да
# # - 1 -> нет

print('введите число обозначающее день недели')
a = int(input())
if a>=1 and a <=5:
    print('нет, работаем')
elif a>=6 and a<=7:
    print('да, выходной')
else: print('вы ввели некоретное число')

# # 2 Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('x y z; 1 Логическое утверждение; 2 Логическое утверждение')
for x in range(2):
    for y in range(2):
        for z in range(2):
            result = not x and not y and not z
            result2 = not(x or y or z)
            print(x,y,z,'      ',result,'        ',result2)
if result == result2:
    print('равенство истинно')
else:
    print('равенство ложно')

# # 3 Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# # Пример:
# # - x=34; y=-30 -> 4
# # - x=2; y=4-> 1
# # - x=-34; y=-30 -> 3

print('введите координаты точки X')
x = int(input())
print('введите координаты точки Y')
y = int(input())
if x>0 and y >0:
    print('точка расположена в 1 четверти')
elif x<0 and y>0:
    print('точка расположена во 2 четверти')
elif x<0 and y<0:
    print('точка расположена во 3 четверти')
elif x>0 and y<0:
    print('точка расположена в 4 четверти')
else: print('точка расположена на координатной прямой')

# # 4 Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

print('введите номер четверти от 1 до 4')
a = int(input())
if a == 1:
    print('диапазон возможных координат точек 0< x < inf')
    print('диапазон возможных координат точек 0< y < inf')
elif a == 2:
    print('диапазон возможных координат точек 0< x < -inf')
    print('диапазон возможных координат точек 0< y < inf')
elif a == 3:
    print('диапазон возможных координат точек 0< x < -inf')
    print('диапазон возможных координат точек 0< y < -inf')
elif a == 4:
    print('диапазон возможных координат точек 0< x < inf')
    print('диапазон возможных координат точек 0< y < -inf')
else: print('вы ввели некоретное число')

# # 5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# # Пример:
# # - A (3,6); B (2,1) -> 5,09
# # - A (7,-5); B (1,-1) -> 7,21

print('введите координаты точки A')
pointA=[]
for i in range(2):
    pointA.append(int(input()))
print('введите координаты точки B')
pointB=[]
for i in range(2):
    pointB.append(int(input()))
distance = ((pointB[0] - pointA[0]) ** 2 + (pointB[1] - pointA[1]) ** 2)**(0.5) 
print(f"Длина отрезка: {format(distance, '.2f')}")
