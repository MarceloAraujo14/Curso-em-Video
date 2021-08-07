"""
melhore o 61 perguntando se quer mostrar mais alguns termos. finalize programa
quando digitar 0.
"""
a = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
termo = a
t = 1
tr = 11
while t < tr:
    if t < tr-1:
        print(termo, end=' -> ')
    else:
        print(termo, end='. PAUSA')
        print()
        x = int(input('Quantos termos deseja mostrar a mais? '))
        if x == 0:
            break
        tr += x
    termo += r
    t += 1
print(f'Progressão finalizada com {tr} termos mostrados.')