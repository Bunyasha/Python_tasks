# 32.	Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

numbers=list(map(int,input('Введите последовательность чисел через пробел: ').split()))

print("Cписок неповторяющихся элементов исходной последовательности: ", list(set(numbers)))