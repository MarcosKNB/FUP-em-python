qtd_alunos = int(input())
dados_alunos = []

for i in range(qtd_alunos):
    alunos = {}
    alunos['nome'] = input()
    alunos['matricula'] = int(input())
    alunos['curso'] = input()
    dados_alunos.append(alunos)

for i in range(qtd_alunos):
    print(dados_alunos[i])