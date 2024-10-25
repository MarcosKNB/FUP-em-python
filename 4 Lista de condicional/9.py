a = int(input())
b = int(input())
c = int(input())
if a < b:
    if a < c:
        menor = a
    else:
        menor = c
elif b < c:
    menor = b
else:
    menor = c
if a > b:
    if a > c:
        maior = a
    else:
        maior = c
elif b > c:
    maior = b
else:
    maior = c
meio = a + b + c - menor - maior
print(menor)
print(meio)
print(maior)