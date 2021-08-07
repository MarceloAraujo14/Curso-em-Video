"""
Escreva um programa que faça o computador pensar num numero entre 0 e 5.
Peça pro usuario tentar acertar o numero
Mostre se o usuario acertou ou errou.
"""
import time
from random import randint
n1 = randint(0, 5)
num = int(input('Tente acertar o número que eu estou pensando entre 0 e 5: '))
print('PROCESSANDO...')
time.sleep(2)
if num > 5:
    print('Você já foi alfabetizado? Leia novamente o enunciado...')
else:
    if num == n1:
        print(f'Parabéns! O número que eu pensei era o {n1}!\n Você é bom nisso!')
    else:
        print(f'Haha! Você errou! Eu estava pensando no {n1}')
        print('Mais sorte na próxima')
