"""
Faça um programa que leia um ano e mostre se ele é bissexto
"""
from datetime import date

ano = int(input('Digite o ano que deseja analisar.\nDigite 0 se deseja analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
bis = ano % 4
cent = ano % 100
if bis == 0:
    if cent != 0:
        print(f'O ano de {ano} é bissexto')
    else:
        print(f'O ano de {ano} não é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')
