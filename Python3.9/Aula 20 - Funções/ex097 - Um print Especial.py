def titulo(txt):
    print('-'*(len(txt)+10))
    print(f'{txt:^{len(txt) + 10}}')
    print('-' * (len(txt) + 10))

titulo("Digite o texto aqui")