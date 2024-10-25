str1 = input()
str_invertida = str1[::-1]
str_invertida_subs = ''
for letra in str_invertida:
    if letra == 'a':
        str_invertida_subs += '*'
    elif letra == 'A':
        str_invertida_subs += '*'
    else:
        str_invertida_subs += letra
print(str_invertida_subs)