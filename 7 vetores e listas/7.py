vetor = []
contador = 0
for i in range(15):
    num = int(input())
    vetor.append(num)
    if num % 2 == 0:
        contador += 1
print(contador)
for i in range(15):
    if vetor[i]%2 == 0:
        print(vetor[i])