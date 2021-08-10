"""
crie um prog com uma tupla total preenchida com contage entr 0 e 20 por extenso.
leia um numero 0-20 e escreva ele por extenso
"""
numeros = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', \
          'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', \
          'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', \
          'dezenove', 'vinte'

'''num = int(input('Digite um número entre 0 e 20: '))
while num not in range(0, 21):
    num = int(input('Erro. Digite novamente um número entre 0 e 20: '))
    if num in range(0, 21):
        break
print(f'Você digitou {numeros[num]}')'''
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            print(numeros[num])
            break
        else:
            continue
    while True:
        esc = str(input('Deseja continuar?[S/N]: ')).upper().strip()[0]
        if esc == 'S':
            break
        elif esc =='N':
            break
        else:
            continue

    if esc == 'S':
        continue
    else:
        break
print('Fim do programa')