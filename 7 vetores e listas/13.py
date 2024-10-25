def funcao(x):
    media = sum(x)/len(x)
    soma = 0
    contador = 0
    for i in range(len(x)):
        soma += (x[i]-media)**2
    resultado = soma/len(x)
    for i in range(len(x)):
        if x[i] < 7:
            contador += 1
    return media, resultado**(1/2), contador