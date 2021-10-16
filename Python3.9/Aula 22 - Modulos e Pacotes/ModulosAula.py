# Arquivo com todos os múdulos de cada desafio

# 107 - Modulo Moeda.py


def aumentar(n=0, p=0, f=True):
    n *= 1+(p/100)
    if f:
        return formatar(n)
    else:
        return n


def diminuir(n=0, p=0, f=True):
    n *= p/100
    if f:
        return formatar(n)
    else:
        return n


def dobro(n=0, f=True):
    n *= 2
    if f:
        return formatar(n)
    else:
        return n


def metade(n=0, f=True):
    n /= 2
    if f:
        return formatar(n)
    else:
        return n


# 108 -

def formatar(n):
    f = f"R${n:.2f}".replace('.', ',')
    return f


# 109 -

# 110 -


def resumo(n, a, d):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20}{formatar(n):<15}')
    print(f'{"Dobro do preço:":<20}{dobro(n):<15}')
    print(f'{"Metade do preço:":<20}{metade(n):<15}')
    print(f'{f"{a}% de aumento:":<20}{aumentar(n, a):<15}')
    print(f'{f"{d}% de desconto:":<20}{diminuir(n, d):<15}')


# 111 -

# 112 -
