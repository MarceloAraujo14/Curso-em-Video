"""Leia uma frase e diga se é um palindromo"""
frase = str(input('Digite uma frase:')).upper().strip()
sem = ''
tamanho = len(frase)
inverso = ''
for n in range(0, tamanho):
    if frase[n] !=' ':
        inverso = frase[n] + inverso
        sem += frase[n]

if sem == inverso:
    print(f'A frase "{frase}" invertida fica:\n"{inverso}".\nPortanto ela é um PALÍNDROMO.')
else:
    print(f'A frase "{frase}" invertida fica:\n"{inverso}".\nPortanto ela não é um PALÍNDROMO.')