num = int(input())
resultado = 0

for i in range(2, num+1):
    teste = num%i
    if teste == 0:
        parte = num / i
        resultado += parte
        
print(resultado)