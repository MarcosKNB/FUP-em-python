contador = 0
arq = input()
with open(arq, 'r') as arquivo:
    for linha in arquivo:
        contador += 1
    arquivo.close()
print(contador)