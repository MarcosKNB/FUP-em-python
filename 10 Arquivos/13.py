arq = input()
pessoas = []
with open(arq, 'r') as arquivo:
    for linha in arquivo:
        pessoa = {}
        nome, telefone = linha.split('\t')
        pessoa['nome'] = nome
        pessoa['telefone'] = telefone.replace('\n', '')
        pessoas.append(pessoa)
    arquivo.close()

for i in range(len(pessoas)):
    for j in range(len(pessoas)):
        if pessoas[i]['nome'] < pessoas[j]['nome']:
            pessoas[i], pessoas[j] = pessoas[j], pessoas[i]
for pessoa in pessoas:
    print(pessoa)