def imprimirmatriz(matriz):
    for i in range(12):
        for j in range(13):
            print(f'{matriz[i][j]:.2f}', end = ' ')
        print()
    print()

def primo(num):
    contador = 0
    for i in range(2, num):
        if num%i == 0:
            contador += 1
    if contador != 0 or num == 0:
        return False
    else:
        return True

matriz = []
for i in range(12):
    linha = []
    for j in range(13):
        linha.append(int(input()))
    matriz.append(linha)

matrizf = []    
for i in range(13):
    divisor = float('-inf')
    teste = float('-inf')
    menor = float('inf')
    linha = []
    for j in range(12):
        if matriz[j][i] > divisor and primo(abs(matriz[j][i])) == True:
            divisor = matriz[j][i]
            
        if matriz[j][i] < menor:
            menor = matriz[j][i]
    if divisor != teste:
        for j in range(12):
            linha.append(matriz[j][i]/divisor)
    else:
        for j in range(12):
            linha.append(matriz[j][i]/menor)
    matrizf.append(linha)

matrizf2 = []
for i in range(12):
    linha = []
    for j in range(13):
        linha.append(matrizf[j][i])
    matrizf2.append(linha)
        
imprimirmatriz(matriz)
imprimirmatriz(matrizf2)