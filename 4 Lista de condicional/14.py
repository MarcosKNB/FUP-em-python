while True:
    print('1 - Adicao\n2 - Subtracao\n3 - Multiplicacao\n4 - Divisao\n5 - Saida')
    operacao = int(input())
    if operacao == 5:
        break
    num1 = float(input())
    num2 = float(input())
    if operacao == 1:
        print(f'{(num1 + num2):.2f}')
    if operacao == 2:
        print(f'{(num1-num2):.2f}')
    if operacao == 3:
        print(f'{(num1 * num2):.2f}')
    if operacao == 4:
        print(f'{(num1/num2):.2f}')