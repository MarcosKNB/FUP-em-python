num1 = float(input())
num2 = float(input())
operacao = int(input())

if operacao == 1:
    resultado = (num1+num2)/2
    print (f'{resultado:.2f}')
elif operacao == 2:
    if num2>num1:
        print(num2-num1)
    elif num1>num2:
        print(num1-num2)
    else:
        print(num1-num2)
elif operacao == 3:
    resultado = num1*num2
    print (f'{resultado:.2f}')
elif operacao == 4:
    if num2 != 0:
        resultado = num1/num2
        print (f'{resultado:.2f}')
    elif num2 == 0:
        print('Erro')
else:
    print('Erro')