"""Crie um programa para aprovar um emprestimo que:
- Leia o valor da casa, o salario da pessoa e em quantos anos ira pagar
- Calcule o valor da prestação
- Prestação nao pode exceder 30% do salario ou será negado
"""
print('Insira os dados para avaliação do empréstimo')
casa = float(input('Insira o valor do imóvel: R$ '))
salario = float(input('Insira o valor do seu salário: R$ '))
anos = float(input('Em quantos anos pretende pagar: '))
prest = casa / (anos*12)
if prest >= (salario*0.3):
    print('Desculpe, mas seu pedido de empréstimo foi negado.')
else:
    print(f'Parabéns, seu pedido de empréstimo foi aceito.')
    print(f'O valor da sua prestação será de R$ {prest:.2f}.\nObrigado por escolher o Banco do Barril')
