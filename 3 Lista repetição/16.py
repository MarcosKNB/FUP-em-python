z = 1
n = 1
opa = 0
for num in range(50):
    valor = n/z + opa
    n = n + 2
    z = z + 1
    opa = valor
print(f'{valor:.10f}')