"""Faça um programa que leia a frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A"
- Em que posição ela aparece a primeira vez
- Em que posição ela aparece pela ultima vez.
"""

frase = str(input('Digite uma frase: ')).strip()
a = frase.upper().count('A')
a1 = frase.upper().find('A')
a2 = frase.upper().rfind('A')
print(f'Quantas vezes aparece a letra "A"?: {a}')
print(f'Em que posição ela aparece a primeira vez? {a1+1}')
print(f'Em que posição ela aparece pela última vez? {a2+1}')
