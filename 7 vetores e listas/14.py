import random
x = int(input())
vetor = []
contador = 0
soma = 0
random.seed(x)
for i in range(12):
    vetor.append(random.uniform(-10, 10))
for i in range(12):
    if vetor[i] < 0:
        contador += 1
    if vetor[i] > 0:
        soma += vetor[i]
print(contador)
print(f'{soma:.2f}')