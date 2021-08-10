"""
Programa q le 4 valores e guarda na tupla
quantas vzs apareceu 9, em q posicao digitou 1° valor 3, quais sao pares.
"""
lista = [int(input('Digite um valor: ')), int(input('Digite um valor: ')),
         int(input('Digite um valor: ')), int(input('Digite um valor: '))]
print(f'Os valores digitados foram {lista}.')
print(f'O valor 9 apareceu {lista.count(9)} vezes.')
if lista.count(3) > 0:
    print(f'O número 3 apareceu primeiro na posição {lista.index(3)+1}')
else:
    print(f'O número 3 não apareceu nenhuma vez.')
print(f'Os números pares são: ', end='')
for c in lista:
    if c % 2 == 0:
        print(c, end=' ')
