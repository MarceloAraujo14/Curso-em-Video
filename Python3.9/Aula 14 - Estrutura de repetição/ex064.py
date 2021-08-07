"""
leia varios num inteiros. o programa so para quando digitar 999.
depois mostre quantos foram digitados e qual foi a soma entre eles.
"""
print('Digite vários números e depois digite [999] para encerrar.')
num = 0
soma = 0
n = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma = soma + num
    n += 1
print(f'{n} valores foram digitados e a soma entre eles é {soma}')
