"""Crie um programa que leia o nome de uma pessoa e diga se ela
tem SILVA no nome."""

nome = str(input('Digite seu nome completo: ')).strip()
up = nome.upper()
silva = 'SILVA' in up
print(f'Você possui Silva no seu nome?: {silva}')
