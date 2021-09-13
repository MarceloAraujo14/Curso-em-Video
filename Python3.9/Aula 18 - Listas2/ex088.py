#gerar palpites mega sena, perguntar quantos jogos serao criados
#gerar 6 numeros entre 1 e 60 para cada
from random import randint

palpites = [] #criar uma lista onde armazenar cada lista de jogo
jogo = [] #gerar uma lista auxiliar para armazenar os jogos
print('MEGA SENA DA VIRADA')
n = int(input('Quantos jogos deseja gerar? ')) #perguntar quantos jogos para ter n.jogos

#criar um laço que insira 6 numeros aleatorios na lista jogos e dps inserir em palpites
for j in range(0, n):
    while len(jogo) < 6:
        num = randint(0, 60)
        if num not in jogo:
            jogo.append(num)
    palpites.append(jogo[:])
    jogo.clear()

print(f'Os palpites para os jogos são:')
for n in range(len(palpites)):
    print(f'Jogo {n+1}: {palpites[n]}')

print('Boa sorte!')