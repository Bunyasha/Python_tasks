#Написать программу, получающую набор произведений чисел от 1 до N.
#Пример: пусть N = 4, тогда [1, 2, 6, 24]
from math import factorial 

while True:
    N = input('Введите число N: ')
    if N.isdigit():
        N = int(N)
        break
else:
    print('Некорректный ввод. Повторите: ')

def f(N):
    N = (0+factorial(1+N))
    return N

list = [f(i) for i in range(N)]
print(list)