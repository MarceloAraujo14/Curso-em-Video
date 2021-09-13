"""Leia nome e peso de varias pessoas guardando numa lista
mostre: quantas foram cadastradas, listagem com as mais pesadas,
mais leves"""

pessoas = []
dados = []
maior = menor = 0

while True:
    dados.append(str(input('Digite o nome: ')).strip())
    dados.append(float(input('Digite o peso[kg]: ')))
    #se for o primeiro da lista
    if len(pessoas) == 0:
        pessoas.append(dados[:])
        maior = menor = dados[1]

    #se nao for o primeiro
    #verifique se o peso digitado é maior ou menor que o maximo e minimo
    else:
        for n in pessoas:
            if dados[1] >= maior:
                maior = dados[1]
                pessoas.append(dados[:])   #se for maior que o maior peso adicionar no fim da lista
                break
            elif dados[1] <= menor:
                menor = dados[1]
                pessoas.insert(0, dados[:])   #se for menor que o menor valor, adicionar no inicio da lista
                break
            else: #se estiver entre dois valores, adicionar após o menor que ele
                for c in pessoas:
                    if dados[1] > c[1]:
                        pessoas.insert(pessoas.index(c), dados[:])
                        break

                break

    dados.clear()
    resp = str(input('Deseja continuar?[S/N]: ')).strip()[0]
    while resp not in 'SsNn':
        resp = str(input('Deseja continuar?[S/N]: ')).strip()[0]
    if resp in 'Nn':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas.')
for n in range(len(pessoas)):
    print(f'Nome: {pessoas[n][0]} | Peso: {pessoas[n][1]}')
print(f'O maior peso registrado foi: {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end='.')
print(f'O menor peso registrado foi: {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end='.')
