matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input()))
    matriz.append(linha)
soma = 0
for i in range(4):
    soma += matriz[i][i]
print(soma)