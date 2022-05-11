# 31.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n = input('Введите натуральное число N: ')
while n.isdigit() != True:
    n = input('Вы ввели что-то не то. Повторите ввод: ')

if n.isdigit() == True:
    n=int(n)
list = []  

i = 2
while i * i <= n: 
    while n % i == 0: 
        n //= i 
        list.append(i)
        i += 1
    if n > 1:
        list.append(n)
   
print('Cписок простых множителей числа N: ', list)    
