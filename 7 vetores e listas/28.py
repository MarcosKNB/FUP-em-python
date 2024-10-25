vetorf = []

while len(vetorf) < 12:
    num = int(input())
    if num not in vetorf:
        vetorf.append(num)
    else:
        print(f'Numero {num} ja existe, escreva outro')
print(vetorf)