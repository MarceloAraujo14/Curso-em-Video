from ModulosAula import aumentar, diminuir, dobro, metade
#Main Program

n = float(input('Digite um valor em R$ '))
print(f'R${n} + 10% é R${aumentar(n)}')
print(f'R${n} - 10% é R${diminuir(n)}')
print(f'O dobro de R${n} é R${dobro(n)}')
print(f'A metade de R${n} é R${metade(n)}')
