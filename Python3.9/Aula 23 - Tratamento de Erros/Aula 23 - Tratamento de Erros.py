# um mesmo try pode ter varios excepts
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

# o except pode aceitar tipos de erros
except (ValueError, TypeError):
    print('Tipo de dado inválido')

except Exception as erro:
    print(f'Erro encontrado: {erro.__class__}')

else:
    print(f'O resultado é {r:.1f}')

finally:
    print('Volte sempre!')
