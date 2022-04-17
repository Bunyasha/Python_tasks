#Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
x=1 
y=1 
z=1
print('при X = 1, Y = 1, Z = 1', not (x or y or z) == (not x and not y and not z))
x=1
y=0
z=1
print('при X = 1, Y = 0, Z = 1', not (x or y or z) == (not x and not y and not z))
x=0
y=1
z=1
print('при X = 0, Y = 1, Z = 1', not (x or y or z) == (not x and not y and not z))
x=1
y=1
z=0
print('при X = 1, Y = 1, Z = 0', not (x or y or z) == (not x and not y and not z))
x=0
y=0
z=1
print('при X = 0, Y = 0, Z = 1', not (x or y or z) == (not x and not y and not z))
x=1
y=0
z=0
print('при X = 1, Y = 0, Z = 0', not (x or y or z) == (not x and not y and not z))
x=0
y=1
z=0
print('при X = 0, Y = 1, Z = 0', not (x or y or z) == (not x and not y and not z))
x=0
y=0
z=0
print('при X = 0, Y = 0, Z = 0', not (x or y or z) == (not x and not y and not z))
