"""programa com tupla unica com nome de produto e respectivo preço
fim mostre listagem organizando de forma tabular
"""
lista = 'mouse', 50.00, 'teclado', 85.00, 'pen drive', 5.00, \
        'roteador', 45.00
print(f'{"lista de compras":-^30}')
for n in range(len(lista)):
    if n % 2 == 0:
        print(f'{lista[n]:.<20}' ' R$', end='')
    else:
        print(f'{lista[n]:>7.2f}')
