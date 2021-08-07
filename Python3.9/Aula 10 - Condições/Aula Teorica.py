"""
Método: Comando com () no final
Objeto: Algo que você da comandos ou utiliza pra algo

ex:
carro.siga() -
'carro' = objeto
'siga()' = comando(metodo)

Estrutura sequencial: Passo a passo em sequencia de cima para a baixo em comandos.

Indentação = inserir um comando ou comandos dentro de um comando.

carro.siga()
se carro.esquerda()
    carro.siga()
    carro.direita()
senao carro.
    carro.esquerda()
    carro.siga()
carro.pare()

Condicional simples = Execução de um comando dependendo da informação recebida pelo
                programa.
Condicional composta = Execução de uma opção de comando dependendo da informação recebida
                    pelo programa

if carro,esquerda():
    bloco True
else:
    bloco False

ex:
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('Seu carro é novo')
else:
    print('Seu carro é velho')
print('Fim')

"""