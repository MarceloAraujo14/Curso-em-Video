def manual():
    global txt
    while True:
        txt = input('Função ou Biblioteca Python >> ')
        if txt in 'Fimfim':
            print('Até logo!')
            break
        help(txt)

manual()

