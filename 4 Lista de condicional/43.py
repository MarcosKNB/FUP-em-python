continuar = 1
idade_menor = float("inf")
idade_maior = float("-inf")
while continuar == 1:
    nome = input('')
    idade = int(input())
    
    if idade <= 0:
        continuar = 0
    if idade > 0:
        if idade < idade_menor:
            nome_menor = nome
            idade_menor = idade
        if idade > idade_maior:
            nome_maior = nome
            idade_maior = idade
        
print(nome_menor)
print(idade_menor)
print(nome_maior)
print(idade_maior)