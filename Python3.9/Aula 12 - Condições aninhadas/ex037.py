"""Escreva um programa que leia um num inteiro qq e peça pro
usuario escolher a base de conversão:
- 1 para binario
- 2 para octal
- 3 para hexadecimal
Mostre o resultado da conversão
"""
print('Digite um número e escolha o seu padrão de conversão')
num = int(input('Número: '))
base = int(input('Base de conversão:\n(1)Binário\n(2)Octal\n(3)Hexadecimal\n'))
bi = bin(num)
oc = oct(num)
hex = hex(num)
if base == 1:
    print(f'O resultado de {num} convertido para binário é: {bi[2:]}')
elif base == 2:
    print(f'O resultado de {num} convertido para Octal é: {oc[2:]}')
elif base == 3:
    print(f'O resultado de {num} convertido para hexadecimal é: {hex[2:]}')
else:
    print('O seu problema não é com números...')
