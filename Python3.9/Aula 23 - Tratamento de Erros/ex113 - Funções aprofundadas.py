import cores


def leiaInt():
    n = input('Digite um número inteiro: ')
    if n == '':
        print('O usuário não quis digitar um número.')
        n = 0
        return n
    try:
        n = int(n)
        return n
    except:
        print(f'{cores.red}Digite um número inteiro válido.{cores.clear}')
        return leiaInt()

def leiaReal():
    n = input('Digite um número real: ')
    if n == '':
        print('O usuário não quis digitar um número.')
        n = 0
        return n
    try:
        n = float(n)
        return n
    except:
        print(f'{cores.red}Digite um número real válido.{cores.clear}')
        return leiaReal()

# Main

i = leiaInt()
r = leiaReal()


print(f'O numero inteiro é {i} e o numero real é {r}')
