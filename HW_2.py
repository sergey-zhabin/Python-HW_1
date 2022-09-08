# 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# float_num = input('Введи вещественное число: ')
# print(type(float_num))
# sum = 0
# for i in float_num:
#     if i != '.':
#        sum += int(i)
# print(sum)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# number = int(input('Введите целое число: '))
# print(type(number))
# factor = 1
# list = []
# for i in range(1, number + 1):
#     factor = factor * i
#     list.append(factor) 
# print(f"Произведения чисел от 1 до {number}:  {list}")

# 3 Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# n = int(input('Введите целое число = '))
# sum = 0
# for i in range(1, n + 1):
#     print(i, ')', (1 + 1/i)**i)
#     sum = sum + ((1 + 1/i)**i)
# print('\nСумма: ', sum, '\n')

# 5 Реализуйте алгоритм перемешивания списка.

import random
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
result = random.sample(list, len(list))
print ('\n', str(list), ' получаем случайный список ', str(result), '\n')