x = int(input())
valor = 1
for num in range(1 , x+1):
    for y in range(num):
        print(valor, end=" ")
        valor = valor + 1
    print()