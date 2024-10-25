matriz = []
for i in range(10):
    linha = []
    for j in range(10):
        if i < j:
            linha.append(2*i+7*j-2)
        elif i == j:
            linha.append(3*(i**2)-1)
        else:
            linha.append(4*(i**3)-5*(j**2)+1)
    matriz.append(linha)
for i in range(10):
    for j in range(10):
        print(matriz[i][j], end = ' ')
    print()