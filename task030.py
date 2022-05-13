# Вычислить число π c заданной точностью d Пример: при d = 0.001,π = 3.141.
# 10^(-1)  ≤  d  ≤  10^(-10)  (до 10 знаков после запятой)

from math import pi

d = input('Введите точность вывода (вещественное число до 10 знаков после запятой) для числа π: ')

  
d1 = str(d).split('.') 
signs_amount = len(d1[1]) 
pi_string = str(pi) 

print('При d = ', d, ', π = ', (float(pi_string[:signs_amount+2])) )

#print('Пи = ', round(pi, d))