def funcao(x, y):
    vetorf = []
    for i in range(len(x)):
        contador = 0
        for j in range (len(y)):
            if x[i] == y[j] and x[i] not in vetorf:
                vetorf.append(x[i])
                contador += 1
    return vetorf