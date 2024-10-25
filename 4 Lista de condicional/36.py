def funcao(x):
    maior = float("-inf")
    contador = 0
    for i in range(1, x+1):
        if x%i == 0:
            for k in range(1, i):
                if i%k == 0:
                    contador += 1
            if contador <= 1:
                maior = i
        contador = 0        
    return maior