"""
desenvolva o programa q leia o primeiro termo e a razao de uma PA e mostre
os 10 primeiros termos dessa progressão
"""
a = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
n = 0
t = 0
for n in range(1, 11):
    t = a + (n - 1)*r
    print(t, end=', ')
