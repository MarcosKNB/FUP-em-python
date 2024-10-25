n = int(input())

for linha in range(n):
    coeficiente = 1
    for j in range(1, linha + 2):
        print(coeficiente, end=" ")
        coeficiente = coeficiente * (linha - j + 1) // j
    print()