def funcao(x):
    z = 0
    for num in range(x):
        num = num+1
        final = ((num**2 + 1)/(num+3)) + z
        z = final
    return final