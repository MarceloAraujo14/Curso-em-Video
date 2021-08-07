"""Sortear os 4 alunos e mostar o nome em ordem"""
from random import shuffle
nome1 = input('Digite um nome: ')
nome2 = input('Digite um nome: ')
nome3 = input('Digite um nome: ')
nome4 = input('Digite um nome: ')
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print(f'A ordem de apresentação será: {lista}')
