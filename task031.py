# 31.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n = input('Введите натуральное число N: ')
while n.isdigit() != True:
    n = input('Вы ввели что-то не то. Повторите ввод: ')

if n.isdigit() == True:
    n=int(n)

list = []  
for i in range(2, n):
    while n % i == 0:
        list.append(i)
        n = n/i
    if n == 1:
        break

if len(list) == 0:
    print("Число является простым")
else:
    print('Cписок простых множителей числа N: ', list)    
