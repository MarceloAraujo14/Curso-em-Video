"""
Escreva um programa que leia o salario e calcule o valor do aumento
para maiores que 1250 calcule 10%
para menor ou igual a 1250 calcule 15%
"""
sal = float(input('Digite so seu salário: '))
if sal > 1250:
    aum = sal + (sal*(10/100))
else:
    aum = sal + (sal*(15/100))

print(f'Seu aumento será de R$ {aum:.2f}')
