continuar = 1
while continuar == 1:
    num = float(input())
    if num <= 0:
        continuar = 0
    else:
        quadrado = num**2
        cubo = num**3
        raiz = num ** (1/2)
        print(f'{quadrado:.2f}')
        print(f'{cubo:.2f}')
        print(f'{raiz:.2f}')