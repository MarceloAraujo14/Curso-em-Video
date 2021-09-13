#crie um programa q crie uma matrix 3x3 e preencha com valor lido
# no fim mostre ela com formatação correta
# aprimore mostrando a soma dos valores pares, a soma da 3 coluna,o + da 2 linha
pares = 0
soma3 = 0
matrix = [[], [], []]

for n in range(0, 3):
    matrix[0].append(int(input(f'Digite um valor para 0x{n}: ')))
for n in range(0, 3):
    matrix[1].append(int(input(f'Digite um valor para 1x{n}: ')))
for n in range(0, 3):
    matrix[2].append(int(input(f'Digite um valor para 2x{n}: ')))

print('='*10)
for n in range(0, 3):
    print(f'[{matrix[0][n]}]', end='')
print()
for n in range(0, 3):
    print(f'[{matrix[1][n]}]', end='')
print()
for n in range(0, 3):
    print(f'[{matrix[2][n]}]', end='')
print()

for n, c in enumerate(matrix): #c representa as listas internas
    for num in c: #num representa o valor dentro de cada lista
        if int(num) % 2 == 0: #int torna a string em um num inteiro
            pares = num + pares

for n in range(0, 3):
    soma3 = soma3 + matrix[n][2]

print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {soma3}.')
print(f'O maior valor da terceira linha é {max(matrix[2])}.')
