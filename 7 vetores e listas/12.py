def funcao(x):
    somamedia = 0
    soma = sum(x)
    media = soma/15
    for i in range(15):
        somamedia += (x[i] - media)**2
    somamedia = somamedia/15
    return media, somamedia**(1/2)