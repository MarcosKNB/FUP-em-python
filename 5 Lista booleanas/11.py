def funcao (x):
    dia, mes, ano = x.split('/')
    d = a = m = 0
    if dia.isnumeric() and mes.isnumeric() and ano.isnumeric() and len(ano) == 4:
        d = int(dia)
        m = int(mes)
        a = int(ano)
        if d > 31 or d < 1 or m>12 or m<1:
            d = m = a = 0
    return d, m, a