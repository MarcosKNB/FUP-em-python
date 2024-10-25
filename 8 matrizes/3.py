matriz = []
num = int(input())
for i in range(num):
    linha = []
    for j in range(num):
        linha.append(i*j)
    matriz.append(linha)

for i in range(num):
    for j in range(num):
        print(matriz[i][j], end=' ')
    print()