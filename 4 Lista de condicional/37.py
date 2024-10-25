def simplificar(x,y):
    if y > x:
        for i in range(1, y):
            if x%i == 0:
                if y%i == 0:
                    x = x/i
                    y = y/i
    elif x > y:
        for i in range(1, x):
            if x%i == 0:
                if y%i == 0:
                    x = x/i
                    y = y/i
    elif x == y:
        x = 1
        y = 1
    if x%2 == 0:
        if y%2 == 0:
            x = x/2
            y = y/2
    x = int(x)
    y = int(y)
    return x, y