def funcao(x):
    d, m, a = x.split('/')
    d = int(d)
    m = int(m)
    meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    strf = f'{d} de {meses[m-1]} de {a}'
    return strf