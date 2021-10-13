aluno = {'Nome':'', 'Média':'', 'Sitação':''}

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input('Média: '))
if aluno['Média']>= 7 :
    aluno['Sitação'] = 'Aprovado'
else:
    aluno['Sitação'] = "Reprovado"

for k, v in aluno.items():
    print(f'{k} é igual a {v}')