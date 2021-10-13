def titulo(txt):
    print('-'*(len(txt)+10))
    print(f'{txt:^{len(txt) + 10}}')
    print('-' * (len(txt) + 10))


def Area(altura, largura):
    area =float(altura * largura)
    print(f'A área de um retangulo com {altura}m de altura e {largura}m de largura é {area}m²')

#Programa Principal
titulo("CÁLCULO DE ÁREA")
Area(altura=float(input('Digite a altura (m): ')), largura=float(input('Digite a largura (m): ')))
