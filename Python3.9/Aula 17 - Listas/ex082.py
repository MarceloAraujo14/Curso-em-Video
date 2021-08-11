""" ler varios valores, colocar numa lista.depois crie duas listas
extras com apenas pares e outra com impares. no fim mostre as 3
"""
lista = []
par = []
impar = []
while True:
    lista.append(int(input('Insira um valor: ')))
    esc =' '
    while True:
        esc = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
        if esc in 'SN':
            break
    if esc == 'S':
        continue
    else:
        break
for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f'Você inseriu os valores: {lista}.')
print(f'Os valores pares inseridos foram: {par}.')
print(f'Os valores impares inseridos foram: {impar}')
