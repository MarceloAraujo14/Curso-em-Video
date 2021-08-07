"""
Leia o sexo da pessoas mas só aceite se for M ou F. Caso esteja errado
peça para digitar novamente.
"""
s = str(input('Qual o seu sexo?[M/F]: ')).upper().strip()
while s != 'M' and s != 'F':
    s = str(input('Incorreto.\nDigite "M" para Masculino e "F" para Feminino[M/F]: ')).upper().strip()
if s == 'M':
    print('Você é do sexo Masculino.')
if s == 'F':
    print('Você é do sexo Feminino.')
