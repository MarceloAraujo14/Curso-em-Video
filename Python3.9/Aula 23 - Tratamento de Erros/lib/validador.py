import cores


def valMenu():
    while True:
        try:
            n = int(input('Escolha uma das opções: '))
            if (n == 1) or (n == 2) or (n == 3) or (n == 4):
                return n
            else:
                print(f'{cores.red}Digite uma opção válida.{cores.clear}')
        except KeyboardInterrupt:
            n = 4
            print('Programa interrompido pelo usuário.')
            return n
        except:
            print(f'{cores.red}Digite uma opção válida.{cores.clear}')
