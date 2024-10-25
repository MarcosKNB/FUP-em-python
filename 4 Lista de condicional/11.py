num1 = float(input())
operacao = input()
num2 = float(input())

if operacao == '+':
    print (num1 + num2)
if operacao == '-':
    print (num1 - num2)
if operacao == '*':
    resultado = num1 * num2
    print (f'{resultado:.2f}')
if operacao == '/':
    resultado = num1/num2
    print (f'{resultado:.2f}')