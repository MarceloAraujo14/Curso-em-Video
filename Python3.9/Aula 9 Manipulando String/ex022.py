"""Crie um programa que leia o nome completo de uma pessoa
- nome com todas maiusculas
- nome com todas minusculas
- quantas letras ao todo sem espaços
- quantas letras primeiro nome
"""
nome = str(input('Insira o seu nome completo: ')).strip()
dividido = nome.split()
junto = ''.join(dividido)
print(f'Seu nome todo em maiúsculo é: {nome.upper()}')
print(f'Seu nome todo em minúsculo é: {nome.lower()}')
"""print(f'Quantas letras seu nome tem?: {len(junto)}')"""
print(f'Quantas letras seu nome tem?: {len(nome) - (nome.count(" "))}')
"""print(f'Quantas letras tem seu primeiro nome?: {len(dividido[0])}')"""
print(f'Quantas letras tem seu primeiro nome?: {nome.find(" ")}')
