matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input()))
    matriz.append(linha)
soma = 0
for i in range(4):
    for j in range(4):
        if j > i:
            soma += matriz[i][j]
print(soma)