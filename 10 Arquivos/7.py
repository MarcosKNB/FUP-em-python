arq = input()
vogais = 'AEIOUaeiou'
with open(arq, 'r') as arquivo:
    arq2 = f'{arq}.out'
    for linha in arquivo:
        for letra in linha:
            with open(arq2, 'a') as arquivo2:
                if letra in vogais:
                    arquivo2.write("*")
                else:
                    arquivo2.write(letra)
                arquivo2.close()
arquivo.close()

with open(arq2, 'r') as arquivo:
    for linha in arquivo:
        print(linha, end = '')
    arquivo.close()