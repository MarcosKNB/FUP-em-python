carros = []

for i in range(5):
    carro = {}
    carro['modelo'] = input()
    carro['ano'] = int(input())
    carro['preco'] = float(input())
    carros.append(carro)

valor = 1
while valor != 0:
    valor = float(input())
    
    for carro in carros:
        if carro['preco'] < valor:
            print(carro)