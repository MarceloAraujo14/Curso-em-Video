total = maisdemil = barato = 0
nome = ''
n = 0
preco = 0
while True:
    produto = str(input('Nome do produto: '))
    n = preco
    preco = float(input('Preço do produto: R$ '))
    total += preco
    if preco < n:
        barato = preco
        nome = produto
    if preco > 1000:
        maisdemil += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Fim da compra.')
print(f'O total da compra foi de R${total}.')
print(f'{maisdemil} produtos custaram mais de R$1000,00.')
print(f'O item mais barato da lista foi {nome}.')
