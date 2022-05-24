
#14. Подсчитать сумму цифр в вещественном числе.
import random

a = random.uniform(1, 10)
print('Сгенерировано число:', a)
b = str(a).replace('.', '')
#print(a)
result = sum(map(int, b))
print(f'Сумма всех цифр числа {a} равна {result}')
