def funcao(x):
    numanterior = 0
    y = 0
    a = 1
    for i in range(x):
        fator = 1/a
        y = fator + y
        a = a+1
    return y