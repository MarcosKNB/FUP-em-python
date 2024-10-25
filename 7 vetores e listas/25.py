def funcao(x ,y):
    vetorf = []
    
    for i in range(len(x)):
        if x[i] not in vetorf:
            vetorf.append(x[i])
    for i in range(len(y)):
        if y[i] not in vetorf:
            vetorf.append(y[i])
    
    return vetorf