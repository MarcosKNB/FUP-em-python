def funcao(x, y):
    vetorf = []

    for i in range(len(x)):
        if x[i] % y == 0:
            vetorf.append(x[i])
    return vetorf