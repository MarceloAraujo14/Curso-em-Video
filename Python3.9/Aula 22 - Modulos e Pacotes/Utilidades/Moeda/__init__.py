def aumentar(n=0, p=0, f=True):
    n *= 1+(p/100)
    return formatar(n) if f else n


def diminuir(n=0, p=0, f=True):
    n *= p/100
    return formatar(n) if f else n


def dobro(n=0, f=True):
    n *= 2
    return formatar(n) if f else n


def metade(n=0, f=True):
    return formatar(n) if f else n


# 108 -

def formatar(n):
    f = f"R${n:.2f}".replace('.', ',')
    return f


# 109 -

# 110 -


def resumo(n=0, a=0, d=0):
    print('-'*30)
    print("RESUMO DO VALOR".center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{formatar(n)}')
    print(f'Dobro do preço: \t{dobro(n)}')
    print(f'Metade do preço: \t{metade(n)}')
    print(f'{a}% de aumento: \t{aumentar(n, a)}')
    print(f'{d}% de desconto: \t{diminuir(n, d)}')
