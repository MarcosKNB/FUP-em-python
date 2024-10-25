def formarmatriz():
    matriz = []
    for i in range(4):
        linha = []
        for j in range(4):
            linha.append(int(input()))
        matriz.append(linha)
    return matriz
matriz1 = formarmatriz()
matriz2 = formarmatriz()
matrizf = []
for i in range(4):
    linha = []
    for j in range(4):
        if matriz1[i][j] > matriz2[i][j]:
            linha.append(matriz1[i][j])
        else:
            linha.append(matriz2[i][j])
    matrizf.append(linha)
for i in range(4):
    for j in range(4):
        print(matrizf[i][j], end = ' ')
    print()