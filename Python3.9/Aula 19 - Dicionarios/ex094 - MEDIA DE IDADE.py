"Esse programa deve ler: nome, sexo e idade de varias pessoas"
"Ao fim do cadastro mostrar: Quantas pessoas foram cadastradas, A média da idade, " \
"Uma lista com todas a mulheres, uma lista com todas as pessoas com idade acima da média "

cadastro = {}
geral = []
soma = media = 0

print('CADASTRO DE PESSOAS')
while True:
    cadastro['Nome'] = str(input('Nome: '))
    cadastro['Idade'] = int(input('Idade: '))
    cadastro['Sexo'] = str(input('Sexo: [M/F] '))

    geral.append(cadastro.copy())
    cadastro.clear()
    resp = str(input('Deseja continuar?[S/N]'))
    while resp not in 'SNsn':
        resp = str(input('Deseja continuar?[S/N]'))
    if resp in 'Ss':
        continue
    else:
        break

for n in range(len(geral)):
    soma = geral[n]['Idade'] + soma

media = soma / len(geral)


print(f'O grupo tem {len(geral)} pessoas.')
print(f'A média da idade das pessoas é {media:5.2f}')
print(f'As mulheres cadastradas foram:', end='')
for n in range(len(geral)):
    if geral[n]['Sexo'] == 'F':
        print(geral[n]['Nome'])

print(f'As pessoas com idade acima da média são:')
for n in range(len(geral)):
    if geral[n]['Idade'] > media:
        print(geral[n])
