"""Par ou impar consecutivo"""
from random import randint
print('Vamos jogar Par ou Impar?')
pc = randint(0, 11)
cont = 0
while True:
    jogadorn = int(input('Escolha um número: '))
    jogadorp = ' '
    while jogadorp not in 'PI':
        jogadorp = str(input('Par ou impar?[P/I]')).upper().strip()[0]
    soma = pc + jogadorn
    if soma % 2 == 0:
        print(f'Você jogou {jogadorn} e o computador {pc}.')
        print(f'{soma} é PAR.')
        if jogadorp in 'Pp':
            print('Você ganhou! Vamos jogar novamente!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    else:
        print(f'Você jogou {jogadorn} e o computador {pc}.')
        print(f'{soma} é IMPAR.')
        if jogadorp in 'Ii':
            print('Você ganhou! Vamos jogar novamente!')
            cont += 1
        else:
            print('Você perdeu!')
            break
print(f'Game Over! Você venceu {cont} vezes seguidas.')
