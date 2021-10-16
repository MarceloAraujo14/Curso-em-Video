from ModulosAula import aumentar, diminuir, dobro, metade
from ModulosAula import formatar
#Main Program

n = float(input('Digite um valor em R$'))
print(f'{formatar(n)} + 10% é {formatar(aumentar(n, 10, False))}')
print(f'{formatar(n)} - 10% é {formatar(diminuir(n, 10, False))}')
print(f'O dobro de {formatar(n)} é {formatar(dobro(n, False))}')
print(f'A metade de {formatar(n)} é {formatar(metade(n, False))}')
