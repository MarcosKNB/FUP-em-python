x = float(input())
if x > 0:
    y = x**(1/2)
    print(f'{y:.2f}')
elif x <= 0:
    print("Numero invalido")