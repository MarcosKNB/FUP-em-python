def funcao(x1, x2):
    if x1 > x2:
        for i in range(1, x1+1):
            if x1%i == 0 and x2%i == 0:
                resultado = i
    elif x2 >= x1:
        for i in range(1, x2+1):
            if x1%i == 0 and x2%i == 0:
                resultado = i
    return resultado