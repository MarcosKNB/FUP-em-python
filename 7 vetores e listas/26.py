def funcao(x, y):
    vetorf = []
    
    for i in range(len(x)):
        if x[i] not in y and x[i] not in vetorf:
            vetorf.append(x[i])
    return vetorf