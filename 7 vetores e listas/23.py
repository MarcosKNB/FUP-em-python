vetor = []

for i in range(10):
    vetor.append(int(input()))
for i in range(10):
    contador = 0
    if vetor [i]> 0:
        for j in range(1, vetor[i]):
            if vetor[i]%j == 0:
                contador += 1
    if vetor[i] < 0:
        for j in range(vetor[i], -1):
            if vetor[i]%j == 0:
                contador += 1
    if contador == 1:
        print (vetor[i])
        print (i)