def funcao(x):
    if x <= 0:
        print(0)
    else:
        funcao(x-2)
        print(x)