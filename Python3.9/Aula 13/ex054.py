"""
Leia o ano de nascimento de 7 pessoas e mostre quantas são e nao são maiores (21)
"""
from datetime import date
maior = 0
menor = 0
for n in range(0, 7):
    ano = int(input('Digite o seu ano de nascimento: '))
    if date.today().year - ano >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas são maiores de idade.')
print(f'{menor} pessoas são menores de idade.')
