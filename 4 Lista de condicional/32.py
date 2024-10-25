num1 = int(input())
num2 = int(input())
contador = 0

if num1 > num2:
    for i in range(num2, num1+1, num2):
        contador += 1
else:
    for i in range(num1, num2+1, num1):
        contador += 1
print(contador)
        