geral = []
jogador = {}
partida = []
#recebendo os dados e guardando no dicionario jogador
while True:
    jogador['Nome'] = str(input('Digite o nome do Jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for n in range(0,  jogador['partidas']):
        partida.append(int(input(f'Quantos gols na {n+1}ª partida? ')))

    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)
    jogador['média'] = round((sum(partida) / jogador['partidas']), 2)
    geral.append(jogador.copy()) #guardando copia do dicionario na lista geral
    partida.clear()

    resp = str(input('Deseja continuar? [S/N]')) #validador resposta
    while resp not in 'SNsn':
        resp = str(input('Deseja continuer? [S/N]'))
    if resp in 'Ss':
        continue
    else:
        break

#mostrando as propriedades de cada jogador
print('='*40)
print('Cod    ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(geral):
    print(f'{k+1:<5}  ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print()
print(f'='*40)
#mostrar analise especifica
while True:
    print('-'*40)
    cod = int(input(f'Digite o Código do jogador que deseja analisar:[0] para finalizar:'))
    while cod != len(geral) and cod != 0:
        print('Jogador não encontrado, por favor tente novamente.')
        cod = int(input(f'Digite o Código do jogador que deseja analisar:[0] para finalizar:'))
    if cod == 0:
        print('Finalizando...')
        break

    else:
        print(f'O jogador {geral[cod-1]["Nome"]} jogou {geral[cod-1]["partidas"]} partidas')

        for p in range(len(geral[cod-1]["gols"])):
            print(f'=> Na {p + 1}ª partida: {geral[cod-1]["gols"][p]} gols')

        print(f'No total foram {geral[cod-1]["total"]} gols.')
        print(f'A média de gols por partida foi de {geral[cod-1]["média"]}.')
