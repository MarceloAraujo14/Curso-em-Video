"""
Condições aninhadas = inserir mais de 2 condições em uma if

carro.siga()
if carro.esquerda():
    comandos.até.chegar

elif carro.direita():
    comandos.até.chegar()
else:
    carro.siga():
carro.pare
"""
nome = str(input('Qual é seu nome? '))
if nome == 'Marcelo':
    print('Que nome lindo!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia {nome}!')
