import random

n = int(input())
m = int(input())
random.seed(int(input()))
i1 = int(input())
i2 = int(input())


matriz = []
for i in range(n):
    linha = []
    for j in range(m):
        linha.append(random.randint(i1, i2))
    matriz.append(linha)

for i in range(n):
    for j in range(m):
        print(matriz[i][j], end = ' ')
    print()

for i in range(n):
    somapar = []
    contadorimpar = 0
    for j in range(m):
        if i%2 == 0:
            somapar.append(matriz[i][j])
        else:
            if matriz[i][j]%3 == 0 and matriz[i][j] < 0:
                contadorimpar += 1
    if i%2 == 0:
        print(f'{sum(somapar)/len(somapar):.2f}')
    else:
        print(contadorimpar)