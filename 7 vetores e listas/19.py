def funcao(x, y):
    vetorf = []
    for i in range(len(x) * 2):
        if i % 2 == 0:
            vetorf.append(x[i//2])
        else:
            vetorf.append(y[i//2])
    return vetorf