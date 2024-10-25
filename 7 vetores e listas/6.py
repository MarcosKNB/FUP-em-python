vetor = []

for i in range(8):
    num = float(input())
    vetor.append(num)
x = int(input())
y = int(input())
result = vetor[x] + vetor[y]
print(f'{result:.2f}')