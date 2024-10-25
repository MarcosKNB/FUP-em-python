for i in range(1000, 10000):
    num1 = i//100
    num2 = i %100
    elevado = (num1+num2)**2
    if elevado == i:
        print(i)