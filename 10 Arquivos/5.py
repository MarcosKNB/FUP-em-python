arq = input()
caractere = input()
contador = 0

with open(arq, 'r') as arquivo:
    for linha in arquivo:
        for letra in linha:
            if letra == caractere:
                contador += 1
    arquivo.close()

print(contador)