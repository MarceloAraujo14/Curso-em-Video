"""Digite 5 valores e cadastreos na posição correta. mostre
a lista.
1 - inserir um valor

2 - se a lista nao possuir nenhum valor, adicionar valor a lista

3 - inserir outro valor

	3.1 - se o valor for o maior da lista
		3.1.1 - adicionar ele no ultimo lugar da lista

	3.2 - se o valor for o menor da lista
		3.2.1 - adicionar valor no primeirolugar da lista

	3.3 - se o valor for maior que lista[n] e menor que lista[n-1]
		3.3.1 - inserir valor apos lista[n]
"""
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
        for n in range(len(lista)):
            if lista[n+1] > valor > lista[n]:
                lista.insert(n+1, valor)
                print(f'O valor foi inserido na posição {n+1}')

    print(lista)
