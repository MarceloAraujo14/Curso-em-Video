maior = homens = mulheres = pessoas = 0
print('CADASTRO DE PESSOAS')
while True:
    print('_______________________________')
    idade = int(input('Digite a idade: '))
    if idade > 18:
        maior += 1
    pessoas += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo:[M/F] ')).upper().strip()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 21:
        mulheres += 1
    esc = ' '
    while esc not in 'SN':
        esc = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    if esc == 'S':
        continue
    if esc == 'N':
        break

print('----------------------------')
print('CADASTRO FINALIZADO')
print(f'Foram cadastradas {pessoas} pessoas.')
print(f'{maior} são maiores de 18 anos.')
print(f'Ao todo são {homens} homens cadastrados.')
print(f'{mulheres} mulheres tem menos de 21 anos.')
