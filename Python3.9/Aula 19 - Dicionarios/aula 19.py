filme = {'titulo':'Star Wars', 'ano':'1977'}

filme['diretor'] = 'Jorge Lucas'

print(filme['diretor'])

pessoas={ 'nome':'Marcelo', 'idade':29}

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['idade']

print(pessoas)

