continuar = 1
maior = float('-inf')
menor = float('inf')
while continuar == 1:
    num = int(input())
    if num < 0:
        continuar = 0
    elif continuar == 1:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
if maior != float('-inf'):
    if menor != float('inf'):
        print(maior)
        print(menor)