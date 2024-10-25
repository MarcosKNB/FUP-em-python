eletrodomesticos = []

for i in range(5):
    eletrodomestico = {}
    eletrodomestico['nome'] = input()
    eletrodomestico['potencia'] = float(input())
    eletrodomestico['tempo ativo por dia'] = float(input())
    eletrodomesticos.append(eletrodomestico)
tempo = int(input())
soma = 0

for eletro in eletrodomesticos:
    unico = eletro['potencia'] * eletro['tempo ativo por dia'] * tempo
    eletro['consumo'] = unico
    soma += unico
    
print(f'{soma:.2f}')    

for eletro in eletrodomesticos:
    nome = eletro['nome']
    consumo = eletro['consumo']
    consumo_relativo = (consumo/soma) *100
    print(f'{nome}: {consumo_relativo:.2f}')