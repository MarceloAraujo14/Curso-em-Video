""" analise uma expressão q use parenteses e diga se ela tem parenteses fechados
e abertos na ordem correta

1 - inserir valores na lista como string de forma separada
2 - identificar se a mesma quantidade de '(' e ')' é igual
3 - identificar se
"""
parenteses = []
lista = list(str(input('Insira uma expressão: ')))

for n in lista:
    if n in '(':
        parenteses.append(n)

    elif n in ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(n)
            break


if len(parenteses) == 0:
    print('Expressão válida')
else:
    print('Expressão Inválida.')
