n = int(input())
maior = float("-inf")
menor = float("inf")
for i in range (n):
    num = float(input())
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print (f'{menor:.2f}')
print (f'{maior:.2f}')