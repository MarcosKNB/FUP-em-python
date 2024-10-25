num = int(input())
matriz = []

for i in range(num):
    linha = []
    for j in range(num):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)

for i in range(num):
    for j in range(num):
        print(matriz[i][j], end = ' ')
    print()