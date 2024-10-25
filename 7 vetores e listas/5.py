vetor = []
quadrados = []
for i in range(10):
    num = float(input())
    vetor.append(num)
for i in range(10):
    quadrados.append(vetor[i]**2)
    print(f'{vetor[i]:.2f}')
for i in range(10):
    print(f'{quadrados[i]:.2f}')