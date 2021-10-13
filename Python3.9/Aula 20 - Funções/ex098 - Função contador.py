from time import sleep


def contador(i, f, p):
    cont = i
    if p == 0:
        p = 1
    elif p < 0:
        p *= -1

    if i < f:
        while cont <= f:
            print(cont, end=' ')
            sleep(0.5)
            cont += p
        print('Fim!')

    elif i > f:
        while cont >= f:
            print(cont, end=' ')
            cont -= p
            sleep(0.5)
        print('Fim!')

    elif i >= f:
        while cont >= f:
            print(cont, end=' ')
            cont -= p
            sleep(0.5)
        print('Fim!')


def linha(x):
    print('-'*x)


def titulo(txt):
    print('-' * (len(txt) + 10))
    print(f'{txt:^{len(txt) + 10}}')
    print('-' * (len(txt) + 10))


titulo("CONTADOR PROGRESSIVO")
sleep(0.5)

print('Contagem de 1 até 10 de 1 em 1')
sleep(0.5)
contador(1, 10, 1)
linha(40)
sleep(0.5)
print('Contagem de 10 até 0 de 2 em 2')
sleep(0.5)
contador(10, 0, 2)
linha(40)
sleep(0.5)
print('Agora é sua vez de personalizar a contagem!')
sleep(0.5)
contador(i=int(input('Ínicio: ')), f=int(input('Fim: ')), p=int(input('Passo: ')))
