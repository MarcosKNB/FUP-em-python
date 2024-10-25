import math
def sf(x):
    if x == 0:
        return 1
    else:
        return sf(x-1)* math.factorial(x)