def funcao(arq, busca):
    contador = 0
    with open(arq, 'r') as arquivo:
        for linha in arquivo:
            palavras = linha.split()
            for palavra in palavras:
                palavraf = ''
                for letra in palavra:
                    if letra.isalpha():
                        palavraf += letra
                if busca.lower() in palavraf.lower():
                    contador += 1
        arquivo.close()
    return contador