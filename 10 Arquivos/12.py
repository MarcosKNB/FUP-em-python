letras = 'abcdefghijklmnopqrstuvwxyz'
contletras = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
arq = input()
contlinhas = 0
contcaracteres = 0
contpalavras = 0
with open(arq, 'r') as arquivo:
    for linha in arquivo:
        palavras = linha.split()
        contpalavras += len(palavras)
        contlinhas += 1
        for letra in linha:
            contcaracteres += 1
            cont = 0
            for letra2 in letras:
                if letra.lower() == letra2:
                    contletras[cont] += 1
                else:
                    cont += 1
    arquivo.close()
print(contcaracteres)
print(contlinhas)
print(contpalavras)
for i in range(26):
    print(f'{letras[i]}: {contletras[i]}')