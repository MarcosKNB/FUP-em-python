def funcao(inicial):
    n = 1
    valoranterior = 1
    for i in range(inicial-1):
        n = n * valoranterior
        valoranterior += 1
    return inicial**n
