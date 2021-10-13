"""
Função = Rotina
"""

#criando função. x é o parametro a ser passado pra função que altera o codigo dentro da function


def linhas(n):
    x = len(n) + 10
    print('-' * x)
    print(f'{n:^{x}}')
    print('-'*x)


def simnao():
    resp = str(input('Deseja continuar?[S/N]'))[0].strip().upper()
    while resp not in 'SN':
        resp = str(input('Deseja continuar?[S/N]'))[0].strip().upper()
    return resp


def contador(num):
    print(len(num))


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1




# O * desempacota informações de uma variavel e utiliza na função

#declarando variaveis
cont = []
resp = ''

#inicio do programa principal
linhas("Criando e aplicando funções")

linhas("Programa para dobrar valores")
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

linhas("Programa para contar quantos números foram lidos")
while True:
    cont.append(int(input('Digite um número: ')))
    contador(cont)
    print(cont)

