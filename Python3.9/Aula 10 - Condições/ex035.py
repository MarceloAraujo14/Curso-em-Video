"""
Leia o comprimento de 3 retas e diga ao usuaria se elas podem ou não
formar um trigangulo
"""
print('Os seguimentos podem formar um triângulo?')
print('Digite o valor de cada lado')
x = float(input('x: '))
y = float(input('y: '))
z = float(input('z: '))

if (x - y) < z < (x + y) and (y - z) < x < (y + z) and (z - x) < y < (z + x):
    print(f'\033[0;32mOs valores podem formar um triângulo\033[m')
else:
    print('\033[0;31mOs valores não podem formar um triângulo\033[m')
