num1 = int(input())
num2 = int(input())
soma = 0
mult = 1
if num2> num1:
    for i in range(num1, num2+1):
        if i % 2 == 0:
            soma += i
        if i % 2 != 0:
            mult *= i
else:
    for i in range(num2, num1+1):
        if i % 2 == 0:
            soma += i
        if i % 2 != 0:
            mult *= i
print(soma)
print(mult)