matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        linha.append(int(input()))
    matriz.append(linha)
vetors = []
for i in range(5):
    soma = 0
    for j in range(5):
        soma += matriz[j][i]
    vetors.append(soma)
print(vetors)