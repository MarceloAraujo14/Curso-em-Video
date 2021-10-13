from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}

print('Jogando...')
for n in range(1, 5):
    jogadores[f'jogador{n}'] = randint(1, 6)
    print(f'Jogador{n} tirou {jogadores[f"jogador{n}"]}')
    sleep(0.5)
ranking = list()
print("Ranking")
cont = 1
for i in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'{cont}° Lugar:{i} com {jogadores[i]} ')
    cont += 1
    sleep(0.5)

#segunda forma de se fazer
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar com {v[0]} com {v[1]}')