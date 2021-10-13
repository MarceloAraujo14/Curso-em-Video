from random import randint
from time import sleep

lista = list()


def sortear():
    for n in range(0, 5):
        valor = randint(0, 10)
        print(valor, end=' ')
        lista.append(valor)
        sleep(0.5)


def somaPar():
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'A soma entre os números pares é: {soma}')

sleep(0.5)
print('Sorteando 5 valores da lista:', end=' ')
sortear()
print()
print('Somando os 5 valores...')
sleep(0.5)
somaPar()
