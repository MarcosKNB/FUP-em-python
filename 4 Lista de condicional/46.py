str1 = input('')
str1_invertida = str1[::-1]

stringzinha = ''
strfinal_invertida = ''
for i in str1_invertida:
    if i.isalpha():
        strfinal_invertida += i
for f in str1:
    if f.isalpha():
        stringzinha += f

strfinal_invertida = strfinal_invertida.lower()
stringzinha = stringzinha.lower()

if strfinal_invertida == stringzinha:
    print('True')
else:
    print('False')