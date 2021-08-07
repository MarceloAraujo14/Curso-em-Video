"""
Refaça o desafio 35 (e ou nao triangulo)
se puder diga se é
- equilatero - 3 lados iguais
- isoiceles - 2 lados iguais
- escaleno - nenhum lado igual
"""
print('Vamos avaliar se os segmentos formam um triângulo.')
a = float(input('Digite o valor do segmento a = '))
b = float(input('Digite o valor do segmento b = '))
c = float(input('Digite o valor do segmento c = '))
tipo = 'escaleno'
if a == b == c:
    tipo = 'equilatero'
elif a == b or a == c or b == c:
    tipo = 'isoiceles'
if a < b + c and b < a + c and c < a + c:
    print(f'Essas medidas formam um triângulo {tipo}.')
else:
    print('Essas medidas não podem formar um triângulo.')
