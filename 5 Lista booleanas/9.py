def funcao(x1, x2):
    if x1 > x2:
        maior = x1
    else: 
        maior = x2
    for i in range(maior, 0, -1):
        ass = x1 * i
        if ass % x1 == 0 and ass % x2 == 0:
            resultado = ass
    return resultado