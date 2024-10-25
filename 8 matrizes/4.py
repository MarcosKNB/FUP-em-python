matriz = []
maior = float('-inf')

for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input()))
    matriz.append(linha)
for i in range(4):
    for j in range(4):
        print(matriz[i][j], end=' ')
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            x = i
            y = j
    print()
print(x)
print(y)
print(maior)