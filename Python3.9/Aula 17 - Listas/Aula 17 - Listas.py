''' Teoria:
As listas são variáveis compostas que permitem armazenar vários
valores em uma mesma estrutura, acessíveis por chaves individuais.

Tuplas - imutaveis
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche[2]) = pizza

Listas - mutáveis
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
lanche[3] = picole
print(lanche) = ['hamburguer', 'suco', 'pizza', 'picole']

adicionar elementos
lanche.append('cookie') - utilize para adicionar elementos ao final da lista
print(lanche) = ['hamburguer', 'suco', 'pizza', 'picole', 'cookie']

'''
lanche = ['hamburguer', 'suco', 'pizza', 'picole', 'cookie']
lanche.insert(3, 'cachorro quente')
print(lanche)
'''
apagar elementos
del.lanche[3]
lanche.pop[3]
lanche.remove('pizza')
print(lanche) = ['cachorro quente', 'hamburguer', 'suco', 'picole', 'cookie']

if 'pizza' in lanche:
    lanche.remove('pizza')

Criar uma lista com comando 'list'.
valores = list(range(4,11))
valores = [4, 5, 6, 7, 8, 9, 10]

valores.sort() - organizar a lista em ordem alfanum
valores.sort(reverse=True) - organizar em ordem ao contrario
'''
