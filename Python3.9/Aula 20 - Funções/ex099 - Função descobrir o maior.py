def maior(*num):
    maior = 0
    print('Analisando os valores passados...')
    for n in (num):
        for i in n:
            print(i, end=', ')
            if i > maior:
                maior = i

    print(f'Foram informados {len(*num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


resp = 'S'
lista = list()

while resp in 'S':
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar[S/N]? '))[0].upper().strip()
    while resp not in 'SN':
        resp = str(input('Deseja continuar[S/N]? '))[0].upper().strip()

maior(lista)
