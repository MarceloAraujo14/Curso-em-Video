"""
Crie um programa que leia o ano de nascimento de um atleta e mostre a categoria
de acordo com idade
- ate 9 mirim
- 9 a 14 infantil
- 15 a 19 junior
- 19 a 20 senior
- acima master
"""
from datetime import date
print('Bem vindo ao sistema da Federação Brasileira de Atletismo!')
ano = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - ano
plu = 'anos'
if idade <= 1:
    plu = 'ano'
print(f'Você tem {idade} {plu}')

if idade < 5:
    print('Você ainda é um bebê...')
elif idade <= 9:
    print('Você está apto a categoria Mirim.')
elif idade <= 15:
    print('Você está apto a categoria Infantil.')
elif idade <= 20:
    print('Você está apto a categoria Junior')
elif idade <= 21:
    print('Você está apto a categoria Senior')
else:
    print('Você está apto a categoria Master')
