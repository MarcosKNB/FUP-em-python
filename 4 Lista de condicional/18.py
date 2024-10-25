def funcao (string):
    dia, mes, ano = string.split('/')
    dia = int(dia)
    if mes == '01':
        mes = 'janeiro'
    if mes == '02':
        mes = 'fevereiro'
    if mes == '03':
        mes = 'marco'
    if mes == '04':
        mes = 'abril'
    if mes == '05':
        mes = 'maio'
    if mes == '06':
        mes = 'junho'
    if mes == '07':
        mes = 'julho'
    if mes == '08':
        mes = 'agosto'
    if mes == '09':
        mes = 'setembro'
    if mes == '10':
        mes = 'outubro'
    if mes == '11':
        mes = 'novembro'
    if mes == '12':
        mes = 'dezembro'
    return(f'{dia}' +' de '+ mes +' de '+ano)