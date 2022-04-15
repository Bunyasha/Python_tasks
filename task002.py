#Найти максимальное из пяти чисел

numbers = [12,34,77,11,5]
print(numbers)
max = numbers[0]
for i in numbers:
    if i>max:
        max=i
print('Максимальное из пяти чисел', max)
