aproveitamento = {}
partida = []
aproveitamento['Nome'] = str(input('Digite o nome do Jogador: '))
partidas = int(input(f'Quantas partidas {aproveitamento["Nome"]} jogou? '))
for n in range(0, partidas):
    partida.append(int(input(f'Quantos gols na {n+1}ª partida? ')))

aproveitamento['partidas'] = partidas
aproveitamento['total'] = sum(partida)
aproveitamento['média'] = sum(partida) / partidas
print(f'O jogador {aproveitamento["Nome"]} jogou {partidas} partidas')

for p in range(len(partida)):
    print(f'=> Na {p+1}ª partida: {partida[p]} gols')

print(f'No total foram {aproveitamento["total"]} gols.')
print(f'A média de gols por partida foi de {aproveitamento["média"]}.')
