"""lanche = 'hamburguer', 'suco', 'pizza', 'pudim'
for cont in range(0, len(lanche)):
    print(lanche[cont])
#for comida in lanche:
#    print(f'Eu vou comer {comida}')
for pos, comida in enumerate(lanche):
    print(f'{pos+1}° eu vou comer {comida}')
print('Comi muito!')
print(sorted(lanche))#ordem alfanumerica"""
"""a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.count(8))# quantos x tem nessa lista
print(c.index(5, 1))#5 > o que vou buscar | 1 > a partir de onde"""
pessoa = 'Gustavo', 39, 'M', 99.88
print(pessoa) #pode se adicionar elementos de tipos variados
del(pessoa)#pode-se apagar uma tupla
print(pessoa)
