"""Digite 7 valores e cadastrar numa lista
separar par de impar. no fim mostrar os pares eimpares em ordem cresc"""
numeros = [[], []] #inserir as 2 listas criadas dentro da lista principal

for n in range(1, 7): #laço de repetição
    num = int(input(f'Digite o {n}° número:')) #inputar um numero
    if num % 2 == 0: #verificar se é par
        numeros[0].append(num) #se for, inserir na primeira lista da lista numeros
    else:
        numeros[1].append(num) #se nao, inserir na segunda lista

print(sorted(numeros[0])) #mostrando as listas em ordem
print(sorted(numeros[1]))
