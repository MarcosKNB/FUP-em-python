def funcao(x):
    z = 1
    for i in range(max(1, x), 0, -1):
        fat = i*z
        z = fat
    return fat