notas = []
for i in range(15):
    num = float(input())
    notas.append(num)
soma = sum(notas)
print(f'{soma/15:.2f}')