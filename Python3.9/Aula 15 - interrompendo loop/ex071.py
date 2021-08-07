print('Caixa Eletrônico Automático')
print('Digite o valor que deseja sacar: R$')
print('Este caixa possui notas de R$50,00 / R$20,00 / R$10,00 / R$1,00')
n50 = n20 = n10 = n1 = 0
valor = int(input('R$'))
atual = valor
while True:
    while atual >= 50:
        atual -= 50
        n50 +=1
        if n50 > 20:
            break
        if atual < 50:
            break
    while atual >= 20:
        atual -= 20
        n20 +=1
        if n20 > 50:
            break
        if atual < 20:
            break
    while atual >= 10:
        atual -= 10
        n10 +=1
        if n10 > 100:
            break
        if atual < 10:
            break
    while atual >= 1:
        atual -= 1
        n1 +=1
        if n1 > 500:
            break
        if atual < 1:
            break
    break

print(f'R$50: {n50:.0f}\nR$20: {n20:.0f}\nR$10: {n10:.0f}\nR$1: {n1:.0f}')
print('fim')