vetor = []

for i in range(20):
    num = int(input())
    vetor.append(num)
for i in range(20):
    if vetor[i] < 0:
        vetor[i] = 0
        print(vetor[i])
    else:
        print(vetor[i])