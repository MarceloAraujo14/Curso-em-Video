""" Faça um programa q leia um numero de 0 a 9999 e mostre
cada um dos digitos separados
unidade, dezena, centena e milhar"""

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidades:{u}')
print(f'Dezenas:{d}')
print(f'Centenas:{c}')
print(f'Milhar:{m}')
