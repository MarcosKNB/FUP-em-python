n = int(input())
soma = 0
for i in range (1, n):
    if n%i == 0:
        soma += i
if soma == n:
    print('Perfeito')
else:
    print('Nao perfeito')