matriz = []

for i in range(20):
    linha = []
    for j in range(20):
        linha.append(int(input()))
    matriz.append(linha)
    
maior = float('-inf')

for i in range(20):
    for j in range(17):
        num = matriz[j - 1][i] * matriz[j][i] * matriz[j + 1][i] * matriz[j + 2][i]
        if num > maior:
            maior = num
            coordenadax = j - 1
            coordenaday = i
            direcao = 'baixo'

        num2 = matriz[i][j-1] * matriz[i][j] * matriz[i][j+1] * matriz[i][j+2]
        if num2 > maior:
            maior = num2
            coordenadax = i
            coordenaday = j-1
            direcao = 'direita'

for i in range(17):
    for j in range(17):
        num = matriz[i-1][j-1] * matriz[i][j] * matriz[i+1][j+1] * matriz[i+2][j+2]
        if num > maior:
            maior = num
            coordenadax = i-1
            coordenaday = j-1
            direcao = 'direita baixo'

for i in range(17):
    for j in range(3, 20):
        num = matriz[i][j] * matriz[i+1][j-1] * matriz[i + 2][j - 2] * matriz[i + 3][j - 3]
        if num > maior:
            maior = num
            coordenadax = i
            coordenaday = j
            direcao = 'esquerda baixo'

print(maior)
print(coordenadax)
print(coordenaday)
print(direcao)