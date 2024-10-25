import math

parte_real_z = float(input())
parte_imaginaria_z = float(input())
parte_real_w = float(input())
parte_imaginaria_w = float(input())

soma = {}
subtracao = {}
produto = {}

soma['real'] = parte_real_z + parte_real_w
soma['imaginario'] = parte_imaginaria_z + parte_imaginaria_w

subtracao['real'] = parte_real_z - parte_real_w
subtracao['imaginario'] = parte_imaginaria_z - parte_imaginaria_w

produto['real'] = parte_real_z * parte_real_w - parte_imaginaria_z * parte_imaginaria_w
produto['imaginario'] = parte_imaginaria_z * parte_real_w + parte_imaginaria_w*parte_real_z

moduloz = math.sqrt(parte_real_z**2 + parte_imaginaria_z**2)
modulow = math.sqrt(parte_real_w**2 + parte_imaginaria_w**2)
print(soma)
print(subtracao)
print(produto)
print(f'{moduloz:.2f}')
print(f'{modulow:.2f}')