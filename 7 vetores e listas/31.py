nome = input('')
nome2 = []
for carac in nome:
    if carac.isalpha() and carac not in nome2:
        nome2.append(carac)

print(len(nome2))