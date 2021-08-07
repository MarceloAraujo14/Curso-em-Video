"""
Crie um programa que leia 2 notas e calcule a media
mostrando uma mensagem de acordo com a media
- abaixo de 5 reprovado
- media entre 5 e 6.9 recuperação
- media 7 ou acima aprovado
"""
n1 = float(input('Digite sua nota em Matemática: '))
n2 = float(input('Digite sua nota em Português: '))

media = (n1 + n2) / 2
if media < 5:
    print(f'Sua média foi {media}. Você foi reprovado.')
elif media > 4.9 and media <7:
    print(f'Sua média foi {media}. Você deverá fazer recuperação.')
elif media >= 7:
    print(f'Sua média foi {media}. Parabéns! Você foi aprovado!')
