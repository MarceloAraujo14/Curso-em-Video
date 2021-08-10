"""
tenha 1 tupla com varias palavras sem acento.
mostrar pra cada palavra quais as suas vogais.
"""
lista = 'APRENDER', 'PRATICAR', 'PROGRAMAR', 'VIDEO', 'CURSO', 'GRATIS', 'ESTUDAR'

for c in range(len(lista)):
    print(f'\nNa palavra {lista[c]} temos:', end=' ')
    for n in range(len(lista[c])):
        if lista[c][n] in 'AEIOU':
            print(lista[c][n], end=' ')

print(f'\nFIM')