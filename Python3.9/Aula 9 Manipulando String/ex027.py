"""Faça um programa que leia o nome completo de uma pessoa, mostrando
em seguida o primeiro e o ultimo nome separadamente.
Ex:Ana Maria de Souza
primeiro:Ana
Último: Souza
"""

nome = str(input('Digite seu nome completo: '))
div = nome.split()
pri = div[0]
ult = div[len(div)-1]
print(f'Primeiro: {pri}')
print(f'Último: {ult}')
