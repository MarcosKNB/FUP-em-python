matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input()))
    matriz.append(linha)
matrizf = []
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(matriz[j][i])
    matrizf.append(linha)
for i in range(4):
    for j in range(4):
        print(matrizf[i][j], end = ' ')
    print()