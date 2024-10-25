def formarmatriz():
    matriz = []
    for i in range(4):
        linha = []
        for j in range(5):
            linha.append(int(input()))
        matriz.append(linha)
    return matriz
matrizA = formarmatriz()
matrizB = formarmatriz()
matrizS = []

for i in range(4):
    linha = []
    for j in range(5):
        linha.append(matrizA[i][j]+matrizB[i][j])
    matrizS.append(linha)

for i in range(4):
    for j in range(5):
        print(matrizS[i][j], end = ' ')
    print()