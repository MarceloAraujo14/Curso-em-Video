"""
Faça um programa que calcule a soma de todos os impares multiplos de 3 entre 1
e 500
"""
soma = 0
for num in range(1, 501):
    if num % 3 == 0 and num % 2 != 0:
        soma = soma + num
        print(num, end=' ')
        print(soma)
print(soma)
