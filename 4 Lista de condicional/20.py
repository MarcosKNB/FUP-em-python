def funcao(x):
    i = x**(1/2)
    if i%1 != 0:
        y = 'False'
    elif i%1 == 0:
        y = 'True'
    return y