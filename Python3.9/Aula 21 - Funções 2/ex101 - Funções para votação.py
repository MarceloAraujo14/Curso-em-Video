from datetime import date


def voto(ano):
    global vt, idade
    idade = date.today().year - ano
    if idade < 16:
        vt = 'Negado'
    elif ((idade < 18) and (idade > 15)) or (idade > 60):
        vt = 'Opcional'
    else:
        vt = 'Obrigatório'

    return vt, idade



vt = ''
idade = 0
voto(int(input('Digite a sua Idade: ')))
print(f'Com {idade} anos o voto é {vt}')
