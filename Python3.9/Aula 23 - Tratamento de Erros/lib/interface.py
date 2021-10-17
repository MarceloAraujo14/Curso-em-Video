import cores


def linha(tam=50):
    print(f'-' * tam)


def cabeçalho(txt):
    print(f'{cores.verde}', end='')
    linha()
    print(txt.center(50))
    linha()
    print(f'{cores.clear}', end='')

def menu(lista):
    c = 1
    for item in lista:
        print(f'[{c}] {item}')
        c += 1
    print(f'{cores.verde}', end='')
    linha()
    print(f'{cores.clear}')