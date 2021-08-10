'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.remove(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')'''
'''
valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite o valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''

a = [2, 3, 4, 7]
b = a[:]
c = a
c[2] = 8
b[2] = 8
print(a)
print(b)
print(c)