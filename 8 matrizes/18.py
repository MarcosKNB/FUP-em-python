import random
random.seed(int(input()))
matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        linha.append(random.randint(1,20))
    matriz.append(linha)

for i in range(5):
    for j in range(5):
        print(matriz[i][j], end = ' ')
    print()
print()

for i in range(4):
    for j in range(4, i, -1):
        matriz[i][j] = 0

for i in range(5):
    for j in range(5):
        print(matriz[i][j], end = ' ')
    print()