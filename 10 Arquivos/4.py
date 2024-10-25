arq = input()
vogais ='aeiouAEIOU'
consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
contadorv = 0
contadorc = 0

with open(arq, 'r') as arquivo:
    for linha in arquivo:
        for letra in linha:
            if letra in vogais:
                contadorv += 1
            elif letra in consoantes:
                contadorc += 1
    arquivo.close()
print(contadorv)
print(contadorc)