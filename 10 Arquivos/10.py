arq = input()
cidades = []
maiorhabitantes = 0
with open(arq, 'r') as arquivo:
    for linha in arquivo:
        cidade = {}
        nome_cidade, habitantes = linha.split('\t')
        habitantes = int(habitantes)
        if habitantes > maiorhabitantes:
            maiorhabitantes = habitantes
            nomemaior = nome_cidade
        cidade['nome'] = nome_cidade
        cidade['habitantes'] = habitantes
        cidades.append(cidade)
    arquivo.close()

with open(f'{arq}.out', 'a') as arquivo:
    arquivo.write(f'{nomemaior}\t{maiorhabitantes}')
    arquivo.close()
for cidade in cidades:
    print(cidade)
with open(f'{arq}.out', 'r') as arquivo:
    for linha in arquivo:
        print(linha)
    arquivo.close()