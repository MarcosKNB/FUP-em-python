vetor = []

for i in range(100):
    vetor.append(float(input()))
x = -1
while x != 0:
    x = int(input())
    if x < 0 or x > 2:
        print('Codigo invalido')
    if x == 0:
        x = 0
    elif x == 1:
        for i in range(100):
            print(vetor[i])
    elif x == 2:
        vetori = vetor[::-1]
        for i in range(100):
            print(vetori[i])