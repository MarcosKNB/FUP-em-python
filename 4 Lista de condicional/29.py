num = int(input())
contador = 0
for i in range(1, num):
    if num%i == 0:
        contador += 1
if contador == 1:
    print ('Primo')
else:
    print('Nao primo')