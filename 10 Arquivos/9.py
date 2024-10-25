arq1 = input()
arq2 = input()
arq3 = arq1 + arq2
with open(arq1, 'r') as arquivo:
    for linha in arquivo:
        with open(arq3, 'a') as arquivo3:
            arquivo3.write(linha)
            arquivo3.close()
    arquivo.close()

with open(arq2, 'r') as arquivo:
    for linha in arquivo:
        with open(arq3, 'a') as arquivo3:
            arquivo3.write(linha)
            arquivo3.close()
    arquivo.close()

with open(arq3, 'r') as arquivo3:
    for linha in arquivo3:
        print(linha, end = '')
    arquivo3.close()