"""
Calcule imc de uma pessoa e mostre
- <18.5 = abaixo do peso
- 18.5 a 25 = peso ideal
- 25 a 30 = sobrepeso
- 30 a 40 = obesidade
- acima 40 = obesidade morbida
"""
print('Vamos calcular seu IMC?')
peso = float(input('Por favor digite seu peso atual em kilogramas: '))
altura = float(input('Por favor digite a sua altura em metros: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f}kg/m². Isto indica que você está abaixo do peso.')
elif imc <= 25:
    print(f'Seu IMC é de {imc:.2f}kg/m². Isto indica que você está no peso ideal.')
elif imc <= 30:
    print(f'Seu IMC é de {imc:.2f}kg/m². Isto indica que você está com sobrepeso.')
elif imc <= 40:
    print(f'Seu IMC é de {imc:.2f}kg/m². Isto indica que você está com obesidade.')
else:
    print(f'Seu IMC é de {imc:.2f}kg/m². Isto indica que você está com obesidade mórbida.')
