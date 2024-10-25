import math

def funcao(x):
    z = 1
    n = 1
    for num in range(x):
        valor = z + (1/math.factorial(n))
        z = valor
        n = n+1
    return valor