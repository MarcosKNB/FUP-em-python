def funcao(x):
    y = []
    for ele in x:
        if x.count(ele) == 1:
            y.append(ele)
    return y