dados = []

for i in range(10):
    dado = {}
    dado['nome'] = input()
    dado['matricula'] = int(input())
    dado['media'] = float(input())
    dados.append(dado)

aprovados = []
reprovados = []

for aluno in dados:
    if aluno['media'] < 5:
        reprovados.append(aluno)
    else:
        aprovados.append(aluno)
for aluno in aprovados:
    print(aluno)
for aluno in reprovados:
    print(aluno)