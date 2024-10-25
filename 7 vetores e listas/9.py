vetor = []
maior = float('-inf')
menor = float('inf')

for i in range(10):
    num = int(input())
    vetor.append(num)
for i in range(10):
    if vetor[i] > maior:
        maior = vetor[i]
    if vetor[i] < menor:
        menor = vetor[i]

print(maior)
print(menor)