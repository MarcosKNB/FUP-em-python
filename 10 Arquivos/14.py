arq = input()
diaatual = int(input())
mesatual = int(input())
anoatual = int(input())

def calcular_idade(d, m, a):
    d = int(d)
    m = int(m)
    a = int(a)
    idade = anoatual - a
    if (mesatual, diaatual) < (m, d):
        idade -= 1
    return idade
    
with open(arq, 'r') as arquivo:
    for linha in arquivo:
        nome, data = linha.split('\t')
        d, m, a = data.split()
        idade = calcular_idade(d, m, a)
        with open(f'{arq}.out', 'a') as arquivo2:
            linha2 = f'{nome}\t{idade}\n'
            arquivo2.write(linha2)
            
with open(f'{arq}.out', 'r') as arquivo:
    for linha in arquivo:
        print(linha, end = '')