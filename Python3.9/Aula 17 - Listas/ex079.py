"""
Digite varios valores. Cadastre uma lista. caso ele ja exista ele nao adiciona.
no final exiba todos os valores em ordem crescente.
"""
lista = []
valor = 0
while True:
    valor = (int(input('Digite um valor: ')))
    while True:
        if valor in lista:
            print('Valor duplicado! Não vou adicionar...')
            valor = (int(input('Digite um valor: ')))
        else:
            lista.append(valor)
            print('Valor adicionado com sucesso.')
            break
    while True:
        esc = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
        if esc == 'S':
            break
        elif esc == 'N':
            break
        else:
            continue
    if esc == 'S':
        continue
    elif esc == 'N':
        break
print(f'Os valores adicionados foram: ', end='')
for n in range(len(lista)):
    print(f'{lista[n]}', end='.')
print(f'\nOs valores em ordem {sorted(lista)}')
