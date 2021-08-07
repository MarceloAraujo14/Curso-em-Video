from time import sleep
count = 0
for count in range(0, 5):
    print('caminhando...')
    sleep(1)
    count = count + 1
    if count == 3:
        print('Você achou uma moeda!')
        pega = str(input('Digite PEGAR: ')).upper()
        if pega == 'PEGAR':
            print('Você pegou uma moeda!')
        else:
            print('Você passou direto...')
        sleep(2)
print('Chegou!')

#aula pratica
"""
Teoria - Estrutura de repetição com variavel de controle.
for = estrutura
x = variavel
in = estrutura interna (dentro de)
range = estrutura de alcance (i , f , p)
i = inicio
f = fim
p = passo a passo (lê o numero a cada n2) 
"""
"""i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')"""
