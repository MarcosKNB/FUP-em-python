def funcao(x):
    if x == 2:
        return 2
    elif x == 1:
        return 1
    else:
        return 2*funcao(x-1) + 3 * funcao(x-2)