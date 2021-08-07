"""
desenvolva um programa q leia 6 numeros e mostre a soma apenas dos pares
"""
soma = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}° número:'))
    if num % 2 == 0:
        soma = soma + num
print(soma)
