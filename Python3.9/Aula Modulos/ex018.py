import math

angulo = float(input('Digite o valor do ângulo:'))
se = math.sin(math.radians(angulo))
co = math.cos(math.radians(angulo))
ta = math.tan(math.radians(angulo))
print(f'O seno de {angulo}° é {se:.4f}')
print(f'O cosseno de {angulo}° é {co:.4f}')
print(f'A tangente de {angulo}° é {ta:.4f}')
