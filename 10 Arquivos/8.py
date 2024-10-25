arq = input()
arq2 = input()

with open(arq, 'r') as arquivo:
    for linha in arquivo:
        for letra in linha:
            with open(arq2, 'a') as arquivo2:
                arquivo2.write(letra.upper())
                arquivo2.close()
    arquivo.close()

with open(arq, 'r') as arquivo:
    for linha in arquivo:
        print(linha, end = '')
    arquivo.close()
with open(arq2, 'r') as arquivo:
    for linha in arquivo:
        print(linha, end = '')
    arquivo.close()