"""Digite 5 valores e cadastreos na posição correta. mostre
a lista."""
lista = []
valor = 0
for c in range(0, 5):
    valor = (int(input('Digite um valor: ')))
    if len(lista) == 0:
        lista.append(valor)
    elif valor > max(lista):
        lista.append(valor)
        print('Adicionado ao final da lista...')
    elif valor < min(lista):
        lista.insert(0, valor)
        print('Adicionado a posição 0 da lista')
    elif min(lista) < valor < max(lista):
        if lista[1] > valor > lista[0]:
            lista.insert(1, valor)


    print(lista)

