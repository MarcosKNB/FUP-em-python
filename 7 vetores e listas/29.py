def funcao(x):
    for i in range(10):
        for j in range(9):
            if x[j] < x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x
                