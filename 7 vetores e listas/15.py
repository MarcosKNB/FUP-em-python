vetor = []

for i in range(10):
    vetor.append(float(input()))
for i in range (10):
    for j in range(i+1, 10):
        if vetor[i] == vetor[j]:
            print(int(vetor[i]))