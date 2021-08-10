"""leia varios e ponha na lista.
quantos num foram digitados, valores ordenados decrescente, se 5 foi digitado.
1 - inserir valor
2 - perguntar se quer continuar (while)
3 - se for sim, inserir valor (continue)
3.1 - se for nao, finalizar.(break)
4 - armazenar a quantidade de elementos digitado (len)
5 - mostrar a lista em forma descescente [::-1]
6 - buscar na lista o valor 5 (if /in)
 """
lista = []
while True:
    lista.append(int(input()))