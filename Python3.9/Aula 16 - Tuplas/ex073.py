"""Crie uma tupla com os 20 colocados no camp bras fut.
mostre apenas os 5 primeiros, os ultimos 4, ordem alfabetica, posicao chapecoense.
"""
lista = 'Palmeiras', 'Atlético-MG', 'Bragantino', 'Fortaleza', 'Flamengo', \
        'Athletico-PR', 'Ceará', 'Santos', 'Atlético-GO', 'Bahia', \
        'Corinthians', 'Fluminense', 'Juventude', 'Sport', 'Internacional', \
        'Cuiabá', 'São Paulo', 'América-MG', 'Grêmio', 'Chapecoense'
print(len(lista))
print(lista[0:5])
print(lista[-5:])
print(sorted(lista))
print(f'O Chapecoense está na {lista.index("Chapecoense")+1}ªcolocação.')