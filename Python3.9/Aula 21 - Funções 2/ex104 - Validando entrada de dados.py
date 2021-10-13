def leiaInt(num):
    print(num)
    try:
        x = int(input())
        return x
    except:
        return leiaInt(num)

def leiainteiro(num):
    n = input(num)
    while True:
        if n.isnumeric():
            return n
            break
        else:
            n = input(f'Digite um número válido:')


n = leiainteiro('Digite um numero: ')
print(f'Você digitou o numero {n}')