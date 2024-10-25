matriz = []
for i in range(12):
    linha = []
    for j in range(13):
        linha.append(int(input()))
    matriz.append(linha)

matrizf = []
for i in range(12):
    maior = float('-inf')
    linha = []
    for j in range(13):
        if abs(matriz[i][j]) > maior:
            maior = abs(matriz[i][j])
    for k in range(13):
        linha.append(matriz[i][k]/maior)
    matrizf.append(linha)

for i in range(12):
    for j in range(13):
        print(f'{matriz[i][j]:.2f}', end = ' ')
    print()
print()
for i in range(12):
    for j in range(13):
        print(f'{matrizf[i][j]:.2f}', end = ' ')
    print()