stri = input('')
vogais = 'AEIOUaeiou'
strf = ''
for letra in stri:
    if letra not in vogais:
        strf += letra
print(strf)