"""
Teoria - Estrutura de repetição com teste lógico.

Enquanto (algo (não) acontecer:
    Faça isso.
Fim.

While x == False(True):
    Faça isso.
Fim

import time
x = 0
morreu = 'n'
while x < 5:
    print('Passo...')
    x += 1
    time.sleep(1)
    if x == 2:
        comando = input('Existe um buraco:[PULAR/SEGUIR]:').upper()
        if comando == 'PULAR':
            print('Pulou!')
        else:
            morreu = 's'
            break
if morreu == 'n':
    print('Você chegou ao seu Destino!')
if morreu == 's':
    print('Você caiu... GAME OVER')"""


while True:
    while True:
        sexo = str(input('Digite o sexo[M/F]: ')).upper()
        if sexo == 'F':
            print('Feminino')
            break
        elif sexo == 'M':
            print('Masculino')
            break
        else:
            print('Dado inválido.')
    while True:
        esc = str(input('Deseja continuar?[S/N]')).upper()
        if esc == 'S':
            break
        elif esc == 'N':
            break
        else:
            print('Dado inválido.')
    if esc == 'S':
        continue
    else:
        break
print('Fim')
