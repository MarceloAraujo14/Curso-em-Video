"""
Fatiamento
frase = 'Curso em Vídeo Python'
frase(9:14) = 'Video'
frase(9:21:2) = 'VdoPto'
frase(:5) = 'Curso'
frase(15:) = 'Python'
frase(9::3) = 'VePh'

Análise
len(frase) = 21 caracteres
frase.count('o') = 3 letras 'o'
frase.count('o',0,13) = 1 letra 'o' do '0' até o '13'
frase.find('deo') = 'deo' dentro da frase iniciado posição 11
frase.find('Android') = -1 (não foi encontrado
'Curso' in frase = True (existe a palavra dentro da string 'frase')

Transformação
frase.replace('Python','Android') = Substituir a palavra 'Python' pela palavra 'Android'
frase.upper() = transforma todas as letras minusculas em maiuscula.
frase.lower() = transforma todas as letras maiusculas em minusculas.
frase.capitalize() = Transforma todos os caracteres para minusculos
                    e a primeira letra em maiusculo.
frase.title() = analisa quantas palavras tem na frase e transforma as primeiras
                letras de uma palavra em maiuscula.

frase.rstrip() = Remove os espaços sobrando a direita
frase.lstrip() = Remove os espaços sobrando a esquerda
frase.strip() = Remove os espaços no inicio e fim da strip

Divisão
frase.split() = Divide a string em strings considerando os espaços entre palavras
                e gerando uma nova list.
'-'.join(frase) = Une strings em uma unica string unindo por '-'

"""
frase = 'Curso em Vídeo Python'
print(frase)
print(len(frase))
print(frase.count('e'))
print(frase.upper())
print(len(frase))
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.split())
dividido = frase.split()
print(dividido[2][3])