"""Crie um programa que leia o nome de uma cidade e diga se ela
começa ou não com a palavra SANTO"""

nome = str(input('Digite o nome da sua cidade: ')).strip()
div = nome.upper().split()
santo = 'SANTO' in div[0]
print(f'Sua cidade começa com Santo no nome?: {santo}')
