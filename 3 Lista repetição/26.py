import math
def funcao(x, y):
    z = 0
    for i in range(y+1):
        seno = ((-1)**i)*((x**(2*i+1))/ (math.factorial(2*i+1)))  +  z
        z = seno
    return seno