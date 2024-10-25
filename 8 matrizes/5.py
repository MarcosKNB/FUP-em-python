matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        linha.append(int(input()))
    matriz.append(linha)
x = int(input())
def funcao(x):
    for i in range(5):
        for j in range(5):
            if matriz[i][j] == x:
                return i, j
    return -1, -1
pos1, pos2 = funcao(x)
if pos1 != -1:
    print(pos1)
    print(pos2)
else:
    print('Nao encontrado')