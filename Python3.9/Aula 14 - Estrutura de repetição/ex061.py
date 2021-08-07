"""
refaça o 51. ler o primeiro termo e a razao pa.
mostrando os 10 primeiros termos usando while.
"""
a = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
t = 1
while t < 11:
    if t < 10:
        print(a, end=',')
    else:
        print(a, end='')
    a = a + r
    t += 1
