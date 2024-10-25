letras = 'abcdefghijklmnopqrstuvwxyz'
contletras = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
arq = input()

with open(arq, 'r') as arquivo:
    for linha in arquivo:
        for letra in linha:
            cont = 0
            for letra2 in letras:
                if letra.lower() == letra2:
                    contletras[cont] += 1
                else:
                    cont += 1
    arquivo.close()

for i in range(26):
    print(f'{letras[i]}: {contletras[i]}')