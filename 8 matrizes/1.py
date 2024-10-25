matriz = []
contador = 0
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input()))
    matriz.append(linha)
for i in range(4):
    for j in range(4):
        if matriz[i][j]> 10:
            contador += 1
print(contador)