carros = {}

for i in range(5):
    modelo = input('')
    consumo = float(input())
    carros[modelo] = consumo

economico = [0, 0]
for modelo, consumo in carros.items():
    if consumo > economico[1]:
        economico = [modelo, consumo]
print(f'Carro mais economico: {economico[0]}')

for modelo, consumo in carros.items():
    print(f'Carro {modelo} percorre {consumo*50:.2f} kms com 50 litros')
for modelo, consumo in carros.items():
    print(f'Carro {modelo} precisa de {1000/consumo:.2f} litros para percorrer 1000 kms')