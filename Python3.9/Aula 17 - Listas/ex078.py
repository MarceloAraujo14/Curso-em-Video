'''
faça um programa q leia 5 valores num e guarde numa lista.
mostre qual maior e menor digitado e as posicoes de cada.
'''
valor = []
for c in range(0, 5):
    valor.append(int(input(f'Digite o valor na posição {c}:')))
print(f'você digitou os valores: {valor}')
print(f'O maior valor digitado foi {max(valor)} na posição ', end='')
for n in range(0, 5):
    if valor[n] >= max(valor):
        print(f'{n}...', end='')

print(f'\nO menor valor digitado foi {min(valor)} na posição ', end='')
for n in range(0, 5):
    if valor[n] <= min(valor):
        print(f'{n}...', end='')