"""Gere 5 num aleatorios e coloque numa tupla.
Dps mostre a listagem dos num gerados e indique o menor e mairo
"""
from random import randint
lista = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print(f'Os valores sorteados foram: {lista[0]} {lista[1]} {lista[2]} {lista[3]} {lista[4]} ')
print(f'O maior valor foi: {max(lista)}')
print(f'O menor valor foi: {min(lista)}')
