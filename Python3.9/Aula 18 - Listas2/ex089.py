#nome e 2 notas de varios alunos, mostre o boletim com media
#opcao de mostrar a nota individual

boletim = []  #criar uma lista
dados = []
resp = ''
#criar um laço
while True:
    # criar o input de nome, 2 notas e a media
    dados.append(str(input('Digite o nome do aluno: ')))
    dados.append(float(input('Digite a 1ª nota: ')))
    dados.append(float(input('Digite a 2ª nota: ')))
    dados.append((dados[1] + dados[2])/2)
    boletim.append(dados[:])
    dados.clear()
    while True:
        resp = str(input('Deseja continuar?[S/N]')).strip().capitalize()[0]
        if resp in 'SN':
            break
    if resp in 'N':
        break

while True:
    print('='*30)
    print('Digite a opção do aluno que deseja visualizar o boletim.')
    for n in range(len(boletim)):
        print(f'[{n+1}]', boletim[n][0])
    print('Digite [0] para finalizar: ')
    resp = int(input())
    if resp == 0:
        break
    elif resp-1 not in (range(len(boletim))):
        resp = input('Resposta inválida. Digite novamente: ')
    else:
        print('='*30)
        print(f'Boletim de :{boletim[resp-1][0]}')
        print(f'Português:{boletim[resp-1][1]}')
        print(f'Matemática:{boletim[resp-1][2]}')
        print(f'Média:{boletim[resp-1][3]}')

print('Finalizando...')