# importando modulos
from lib import cadastro
from lib import validador
from lib import interface

# Programa principal
def main():
    esc = False
    while esc == False:

        interface.cabeçalho('CADASTRO DE CLIENTES')

        # criando lib
        interface.menu(['Abrir listagem cadastrada', 'Cadastrar novo cliente', 'Limpar listagem Cadastrada', 'Sair'])

        # Validando entradas do lib
        esc = cadastro.menu(validador.valMenu())


# Iniciando o programa
if __name__ == '__main__':
    main()
