"""
Leia 2 valores e mostre um menu
1 - somar
2 - multiplicar
3 - maior
4 - novos numeros
5 - sair do programa
"""
num1 = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))
esc = 0
while esc != 5:
    print('---::---' * 3)
    print('O que deseja fazer?')
    esc = int(input('1 - Somar\n2 - Multiplicar\n3 - Maior\n4 - Novos Números\n5 - Sair do programa\n'))

    if esc == 1:
        print(f'A soma entre {num1} e {num2} é {num1 + num2}.')

    elif esc == 2:
        print(f'A multiplicação entre {num1} e {num2} é {num1 * num2}')

    elif esc == 3:
        if num1 == num2:
            print('Os dois números são iguais.')

        else:
            print(f'O maior número entre {num1} e {num2} é {max(num1,num2)}')

    elif esc == 4:
        num1 = int(input('Digite o 1° número: '))
        num2 = int(input('Digite o 2° número: '))
    elif esc == 5:
        break
    elif esc != 1 or 2 or 3 or 4 or 5:
        print('Opção inválida. Tente novamente.')

print('Programa finalizado. Até mais!')
