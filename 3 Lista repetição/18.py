def funcao(x):
    n = 1
    soma = 0

    for i in range(1, x+1):
        n *= i 

    for i in range(x):
        numfinal = n%10
        soma += numfinal
        n = n//10
    return soma