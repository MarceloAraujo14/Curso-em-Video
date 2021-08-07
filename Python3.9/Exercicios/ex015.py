"""Faça um algoritimo que leia o preço do produto e
mostre o seu novo preço com 5% de desconto"""

print('Shopping Dasquina')
x = float(input('Digite o preço do produto:R$'))
y = float(input('Digite o desconto:'))
print(f'Preço atual:R${x}')
print(f'Preço com desconto:R${x-(x*(y/100))}')
