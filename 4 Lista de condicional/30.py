maior = float("-inf")
n = int(input())
contador = 0
for i in range(n):
    num = int(input())
    if num == maior:
        contador += 1
    elif num > maior:
        maior = num
        contador = 1
print(maior)
print(contador)