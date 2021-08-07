"""Faça um algoritimo que leia o salário atual de um funcionário
e calcule o novo salário com 15% de aumento"""

print('Que bom que você deixou de ser mão de vaca')
x = float(input('Salário atual: R$ '))
y = float(input('Aumento em %: '))
print(f'O salário do seu funcionário com aumento será {x+(x*(y/100))}')
