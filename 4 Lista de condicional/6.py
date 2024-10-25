somatotal = 0
validacao = 1
for i in range(3):
    nota = float(input())
    if nota < 0:
        print('Nota invalida')
        validacao = 0
        break
    elif nota > 10:
        print('Nota invalida')
        validacao = 0
        break
    else:
        somatotal += nota

media = somatotal/3
if validacao == 1:
    print(f'{media:.2f}')