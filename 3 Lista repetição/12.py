def funcao(n, k):
    z = 1
    t = 1
    y = n - k
    uru = 1
    for i in range(1, n+1):
        z *= i
    for i in range(1, k+1):
        t *= i
    
    for i in range (1, y+1):
        uru *= i
    
    c = z/(t*uru)
    return c