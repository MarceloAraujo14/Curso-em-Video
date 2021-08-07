"""
Faça um programa que mostre uma contagem regressiva pro estouro de fogos
de 10 a 0 com pausa de 1 seg.
"""
from time import sleep
contagem = 10
for c in range(0, 10):
    print(contagem)
    contagem = contagem - 1
    sleep(1)
print('FELIZ ANO NOVO!!')