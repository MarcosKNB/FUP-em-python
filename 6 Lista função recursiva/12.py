def h(x1, x2):
    if x2 == 1:
        return x1 + 1
    elif x1 == 1:
        return x2 + 1
    else:
        return h(x1 -1, x2) + h(x1, x2 -1)