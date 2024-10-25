dados = []

for i in range(5):
    dado = {}
    dado['nome'] = input()
    dado['endereco'] = input()
    dado['telefone'] = input()
    dados.append(dado)
    
for i in range(5):
    for j in range(5):
        dado1 = dados[i]
        dado2 = dados[j]
        if dado2['nome'] > dado1['nome']:
            dados[i],dados[j] = dados[j], dados[i]
for i in range(5):
    print(dados[i])