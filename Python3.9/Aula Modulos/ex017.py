import math
oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipo = math.hypot(oposto, adjacente)
print(f'O comprimento da hipotenusa é: {hipo:.3f}')
