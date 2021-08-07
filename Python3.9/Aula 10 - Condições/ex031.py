"""
Desenvolva um programa que mostre a distancia de uma viagem em km
Calcule o preço da passagem cobrando R$0,50 por km para viagens de até
200km e R$0,45 para viagens mais longas
"""
dist = float(input('Qual a distância que pretende viajar?: '))
if dist <= 200:
    print(f'Sua passagem custará R$ {dist*0.50}')
else:
    print(f'Sua passagem custará {dist*0.45}')
print('Boa viajem!')
