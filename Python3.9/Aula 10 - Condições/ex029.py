"""
Escreva um programa que leia a velocidade de um carro
Diga que foi multado se passar de 80km/h
A multa vai custar R$7,00 por cada km acima do limite
"""

vel = float(input('Qual a velocidade do veículo?: '))
if vel > 80:
    print(f'Você ultrapassou 80km/h e foi multado em R${(vel - 80)*7.00:.2f}')
else:
    print(f'Parabéns por se manter dentro do limite seguro de velocidade!')
print('Boa viagem!')
