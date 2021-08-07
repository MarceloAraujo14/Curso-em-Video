"""
Leia nome, idade e sexo de 4 pessoas. mostrar media de idade, nome do homem
mais velho e quantas mulheres tem menos de 21
"""
listan = [0, 0, 0, 0]
listai = [0, 0, 0, 0]
listas = [0, 0, 0, 0]
homemi = [0, 0, 0, 0]
mulher = 0
for p in range(0, 4):
    nome = str(input('Digite o seu nome: '))
    listan[p] = nome
    idade = int(input('Digite a sua idade: '))
    listai[p] = idade
    hm = str(input('Digite H para homem ou M para mulher: ')).upper()
    listas[p] = hm
    if hm == 'M' and listai[p] < 21:
        listas[p] = 'M'
        mulher = mulher + 1
    elif hm == 'H':
        homemi[p] = idade

idadeh = homemi.index(max(homemi))
nomeh = listan[idadeh]
media = sum(listai) / 4

print(f'A média de idade dessas pessoas é {media} anos.')
print(f'{nomeh} é o homem mais velho da lista.')
print(f'Existem {mulher} mulheres abaixo de 21 anos.')
