def funcao(x):
    for num in range(1, x+1):
        esp = " " * (x - num)
        ast = "*" * (2*num -1)
        print(esp + ast)