"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
com a idade:
- Se ele vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou o tempo do alistamento
- Mostrar o tempo que falta ou que passou do prazo
"""
from datetime import date

print('Bem vindo ao sistema das Forças Armadas!')
ano = int(input('Por favor digite o seu ano de nascimento: '))
alistar = date.today().year - ano
quando = 18 - alistar
perdeu = alistar - 18
plusing = 'ano'
if quando > 1:
    plusing = 'anos'
if alistar <= 17:
    print('Parabéns, você deverá se alistar.')
    print(f'Fique atento! Você deverá se alistar daqui a {quando} {plusing}.')
elif alistar == 18:
    print('Atenção! Esse é seu ano de alistamento!')
elif alistar > 18:
    print(f'Você perdeu seu ano de alistamento!')
    print(f'Você passou {perdeu} {plusing} do prazo.')
