import cores


def menu(n):
    escolha = n

    if escolha == 1:
        print('-'*50)
        print('Listagem Cadastrada'.center(50))
        print('-' * 50)
        abrirLista()

        esc = False
        return esc

    elif escolha == 2:
        print('-' * 50)
        print('Cadastro de novos clientes'.center(50))
        print('-' * 50)
        Cadastrar()

        esc = False
        return esc

    elif escolha == 3:
        limpar()

        esc = False
        return esc


    elif escolha == 4:
        esc = True
        print('Finalizando programa. Volte sempre!')
        return esc

    else:
        esc = False
        return esc


def abrirLista():
    try:
        lista = open('Lib/Arquivo/Cadastro.txt', 'r')
        for linha in lista:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<35}{dado[1]:>10} anos')
        lista.close()

    except (FileExistsError, FileNotFoundError):
        print(f'{cores.verde}A listagem foi criada.{cores.clear}')
        print()
        print()
        try:
            lista = open('Lib/Arquivo/Cadastro.txt', 'a')
            lista.close()
        except:
            print(f'{cores.red}Pasta "Lib/Arquivo/" não encontrada.{cores.clear}')


def Cadastrar():
    try:
        nome = cadastroNome()
        idade = cadastroIdade()
        lista = open('Lib/Arquivo/Cadastro.txt', 'a')
        lista.write(f'{nome};{idade}\n')
        lista.close()
        print(f'{cores.verde}Cadastro realizado com sucesso.{cores.clear}')
        print()
    except:
        print(f'{cores.red}Houve um erro ao cadastrar o cliente.{cores.clear}')


def limpar():
    try:
        lista = open('Lib/Arquivo/Cadastro.txt', 'w')
        lista.close()
        print(f'{cores.verde}Lista limpa com sucesso.{cores.clear}')
    except:
        print(f'{cores.red}O arquivo solicitado não foi encontrado.{cores.clear}')


# Validadores de cadastro:


def cadastroNome():
    while True:
        nome = str(input('Nome do cliente: '))
        se = nome.strip()
        se = se.split()
        se = ''.join(se)
        if se.isalpha():
            return nome
        else:
            print(f'{cores.red}Digite um nome válido.{cores.clear}')


def cadastroIdade():
    while True:
        idade = input('Idade do cliente: ')
        if idade.isnumeric():
            return idade
        else:
            print(f'{cores.red}Digite uma idade válida.{cores.clear}')