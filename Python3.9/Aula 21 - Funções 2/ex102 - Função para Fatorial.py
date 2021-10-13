def fatorial(num, show=''):
    """
    > calcula o fatorial de um número e mostra ou não o cálculo
    :param num: número a ser calculado
    :param show: (opcional) S ou N para mostrar ou não os cálculos
    :return: retorna o fatorial de num
    """
    global fact
    if show in 'sS':
        mostrar = True
    else:
        mostrar = False
    n = num
    fact = 1
    while n > 0:
        if n == 1:
            if mostrar:
                print(n, end=' = ')
        else:
            if mostrar:
                print(n, end=' x ')
        fact = fact * n
        n -= 1

    return fact

fact = 0
fatorial(int(input('Digite um número: ')), str(input('Deseja mostrar o calculo?[S/N]:')))
print(fact)
help(fatorial)