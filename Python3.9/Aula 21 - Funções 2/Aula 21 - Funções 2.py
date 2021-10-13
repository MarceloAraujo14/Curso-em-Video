from time import sleep

#criando docstring da função
def contador(i, f, p):
    """
    -> faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
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

#função com parametro opcional
def soma(a, b, c=0):
    """

    :param a: recebe valor
    :param b: recebe valor e soma com a
    :param c: opcional => recebe valor e soma com a e b
    :return: null
    """
    s = a + b + c
    print(s)
    return s

a1 = soma(3, 2)
print(f'A soma entre esses numeros é {a1}')