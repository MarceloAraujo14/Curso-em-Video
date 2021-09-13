#crie um programa q crie uma matrix 3x3 e preencha com valor lido
# no fim mostre ela com formatação correta

matrix = [[], [], []]

for n in range(0, 3):
    matrix[0].append(input(f'Digite um valor para 0x{n}: '))
for n in range(0, 3):
    matrix[1].append(input(f'Digite um valor para 1x{n}: '))
for n in range(0, 3):
    matrix[2].append(input(f'Digite um valor para 2x{n}: '))

print('='*10)
for n in range(0, 3):
    print(f'[{matrix[0][n]}]', end='')
print()
for n in range(0, 3):
    print(f'[{matrix[1][n]}]', end='')
print()
for n in range(0, 3):
    print(f'[{matrix[2][n]}]', end='')