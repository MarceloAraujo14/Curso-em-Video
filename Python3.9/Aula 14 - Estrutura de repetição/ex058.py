"""Melhore o desafio 28, Jogo em que o jogador deve acertar o numero
que o computador está pensando. Tentando adiviinhar até acertar."""
from random import randint
pc = randint(0, 10)
tentativas = 1
print('Eu estou pensando em um número de 0 a 10.')
p = int(input('Você consegue adivinhar qual é? '))
while p != pc:
    p = int(input('Errou! Tente novamente! '))
    tentativas += 1
if tentativas == 10:
    print('Você é muito ruim nesse jogo! hahaha!')
print(f'Parabéns! Você acertou na {tentativas}ª tentativa que eu pensei no {pc}!')
