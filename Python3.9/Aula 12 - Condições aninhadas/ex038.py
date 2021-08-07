"""
Escreva um programa que leia dois numeros inteiros e compare-os mostrando
na tela a seguinte mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior, os dois são iguais
"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print(f'O número {n1} é maior')
elif n2 > n1:
    print(f'O número {n2} é maior')
else:
    print('Não existe valor maior. Os dois são iguais.')
