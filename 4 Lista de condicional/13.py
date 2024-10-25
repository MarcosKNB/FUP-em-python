import math

a = float(input())
b = float(input())
c = float(input())

delta = b**2 -(4*a*c)
if a != 0:
    if delta < 0:
        print('Nao existe raiz real')
    elif delta == 0:
        x = -b/ (2*a)
        print(f'{x:.2f}\nRaiz unica')
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print(f'{x1:.2f}')
        print(f'{x2:.2f}')
else:
    print('Nao eh equacao do 2o grau')
