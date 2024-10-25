def formarmatriz():
    matriz = []
    for i in range(5):
        linha = []
        for j in range(5):
            linha.append(int(input()))
        matriz.append(linha)
    return matriz
matrizA = formarmatriz()
matrizB = formarmatriz()
matrizM = []

for i in range(5):
    linha = []
    for j in range(5):
        soma = 0
        for k in range(5):
            soma += matrizA[i][k]* matrizB[k][j]
        linha.append(soma)
    matrizM.append(linha)
for i in range(5):
    for j in range(5):
        print(matrizM[i][j], end = ' ')
    print()