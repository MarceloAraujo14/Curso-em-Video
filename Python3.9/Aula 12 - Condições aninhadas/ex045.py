"""
Crie um programa e faça o computador jogar jokenpo com você
"""
from random import choice

lista = ['Pedra', 'Papel', 'Tesoura']
print('Vamos jogar Jo-ken-pô?!')
print('Escolha Pedra, Papel ou Tesoura')
pc = choice(lista)
esc = str(input('Selecione sua arma! ')).capitalize()

if esc == 'Pedra' or 'Papel' or 'Tesoura':
    print(f'Você escolheu {esc} e o computador escolheu {pc}')
    if pc == 'Pedra' and esc == 'Pedra' or pc == 'Papel' and esc == 'Papel' or pc == 'Tesoura' and esc == 'Tesoura':
        print(f'{pc} empata com {esc}. Não houveram vencedores hoje...')

    elif pc == 'Pedra' and esc == 'Papel' or pc == 'Papel' and esc == 'Tesoura' or pc == 'Tesoura' and esc == 'Pedra':
        print(f'Ok,{esc} ganha de {pc}. Você venceu essa...')

    elif pc == 'Pedra' and esc == 'Tesoura' or pc == 'Papel' and esc == 'Pedra' or pc == 'Tesoura' and esc == 'Papel':
        print(f'Hahaha! {pc} ganha de {esc}! Eu ganhei dessa vez!')
else:
    print('Opção inválida')
