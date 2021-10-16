from ModulosAula import aumentar, diminuir, dobro, metade
from ModulosAula import formatar
#Main Program

n = float(input('Digite um valor em R$'))
print(f'{formatar(n)} + 10% é {aumentar(n, 10)}')
print(f'{formatar(n)} - 10% é {diminuir(n, 10)}')
print(f'O dobro de {formatar(n)} é {dobro(n)}')
print(f'A metade de {formatar(n)} é {metade(n)}')