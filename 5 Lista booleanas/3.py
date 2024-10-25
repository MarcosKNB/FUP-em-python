stri = input()
vogais = 'AEIOUaeiou'
consoante = input()
frase = ''
contador = 0
for letra in stri:
    if letra not in vogais:
        frase += letra
    elif letra in vogais:
        frase += consoante
        contador += 1
print(contador)
print(frase)