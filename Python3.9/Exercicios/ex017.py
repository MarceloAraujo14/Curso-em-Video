"""Calcule o valor de um aluguel de carro sabendo que custa R$60,00
por dia e R$0,15 por Km rodado"""

dias = int(input('Quantos dias o carro ficou alugado?: '))
km = float(input('Quantos km o carro rodou?: '))
preco = (dias*60)+(km*0.15)
print(f'O valor a ser pago é pelo aluguel:\nR${preco:.2f}')
