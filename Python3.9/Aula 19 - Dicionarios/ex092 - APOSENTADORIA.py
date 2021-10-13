from datetime import date
cadastro = {}
cadastro['Nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
cadastro['Idade'] = date.today().year - ano
cadastro['CTPS'] = int(input('Número da CTPS[0] caso não exista: '))
if cadastro['CTPS'] != 0:
    cadastro['Ano de contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário: R$'))
    if (date.today().year - cadastro['Ano de contratação']) < 35:
        cadastro['Aposentadoria'] = cadastro['Idade'] + (35 - (date.today().year - cadastro['Ano de contratação']))

for k, v in cadastro.items():
    print(f'{k}: {v}')