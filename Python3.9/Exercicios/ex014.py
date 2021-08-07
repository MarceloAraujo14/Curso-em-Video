"""Leia a largura e a altura de uma parede em metros, calcule a área
e quantidade de tinta necessária para pintá-la, sabendo que
cada litro de tinta pinta uma área de 2m²"""

print('Insira a altura e largura da sua parede')
x = float(input('Altura: '))
y = float(input('Largura: '))
a = x*y
t = a/2
print(f'A área da sua parede é de:{a}m²')
print(f'Será necessário {t} litros de tinta para pintá-la por completo')