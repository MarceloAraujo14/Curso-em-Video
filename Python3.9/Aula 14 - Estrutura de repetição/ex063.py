"""
leia num N inteiro e mostre os elementos de uma sequencia de fibonacci.
"""
print('Sequência de Fibonacci')
termos = int(input('Quantos termos deseja mostrar? '))
n = 1
t = 0
c = 1
while c <= termos:
    print(t, end=' > ')
    n = t + n
    print(n, end=' > ')
    t = t + n
    c+= 1
print('FIM')