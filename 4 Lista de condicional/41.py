num1 = input('')
num2 = ''
for num in num1:
    if num == '0':
        num2 += '1'
    else:
        num2 += num
print (num2)