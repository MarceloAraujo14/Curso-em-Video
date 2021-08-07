"""
Leia o peso de 5 pessoas e mostre o maior e menor
"""
lista = [0, 0, 0, 0, 0]
for n in range(0, 5):
    peso = float(input('Digite o peso: '))
    lista[n] = peso
print(f'O maior peso digitado é {max(lista)} kg.')
print(f'O menor peso digitado é {min(lista)} kg')
