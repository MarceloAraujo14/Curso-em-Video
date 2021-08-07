"""
Leia um numero e mostre o seu fatorial.
5! = 5x4x3x2x1 = 120
"""
"""from math import prod
num = int(input('Digite um número:'))
print(f'O Fatorial de {num} é: ')
n = []
while num >= 1:
    if num > 1:
        print(num, end=' x ')
    n.append(num)
    num -= 1

print(f'={prod(n)}')"""
n = int(input('Digite um numero: '))
c = n
f = 1
print(f'Calculando {n}!', end=' ')
while c > 0:
