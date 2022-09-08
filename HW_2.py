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

number = int(input('Введите целое число: '))
print(type(number))
factor = 1
list = []
for i in range(1, number + 1):
    factor = factor * i
    list.append(factor) 
print(f"Произведения чисел от 1 до {number}:  {list}")