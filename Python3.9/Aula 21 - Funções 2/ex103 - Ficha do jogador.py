def ficha(nome='', gols=''):
    if nome == '':
        nome = '<desconhecido>'
    if gols not in '1234567890':
        print(f'O jogador {nome} marcou 0 gols no campeonato.')
    elif gols in '':
        print(f'O jogador {nome} marcou 0 gols no campeonato.')
    else:
        print(f'O jogador {nome} marcou {gols} gols no campeonato.')


ficha(input('Nome do Jogador: '), input('Número de Gols:'))
"""
n = str(input())
g = str(input())
if g.isnumeric(): #consegue verificar se é um numero
    g = int(g)
else:
    g = 0


n = ''
n.isnumeric()
n.isalnum()
n.isdigit()
n.isdecimal()
"""