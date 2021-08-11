"""leia varios e ponha na lista.
quantos num foram digitados, valores ordenados decrescente, se 5 foi digitado.
1 - inserir valor
2 - perguntar se quer continuar (while)
3 - se for sim, inserir valor (continue)
3.1 - se for nao, finalizar.(break)
4 - armazenar a quantidade de elementos digitado (len)
5 - mostrar a lista em forma descescente [::-1]
6 - buscar na lista o valor 5 (if /in)
 """
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    esc = ' '
    while True:
        esc = str(input('Deseja continuar?[S/N]')).upper().strip()[0]
        if esc in 'SN':
            break
        else:
            continue
    if esc == 'S':
        continue
    else:
        break
print(lista)
print(f'Foram registrados {len(lista)} valores nessa lista.')
lista.sort(reverse=True)
print(f'A lista em forma decrescente é:{lista}.')

if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
