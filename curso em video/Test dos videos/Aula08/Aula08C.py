import  math
angulo = float(input('digite o valor de seu ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'o valor do seno será: {seno:.2f}')
print(f'o valor do cosseno é de: {cosseno:.2f}')
print(f' o tangente de seu ângulo é: {tangente:.2f}')