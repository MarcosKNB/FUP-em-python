alunos = []

for i in range(5):
    dados_alunos = {}
    dados_alunos['matricula'] = int(input())
    dados_alunos['nome'] = input()
    dados_alunos['nota1'] = float(input())
    dados_alunos['nota2'] = float(input())
    dados_alunos['nota3'] = float(input())
    alunos.append(dados_alunos)

maior_nota1 = -1
maior_media = -1
menor_media = 11
for aluno in alunos:
    if aluno['nota1'] > maior_nota1:
        maior_nota1  = aluno['nota1']
        aluno_maior_nota1 = aluno['nome']
    media = (aluno['nota1'] + aluno['nota2'] + aluno['nota3'])/3
    if media > maior_media:
        maior_media = media
        aluno_maior_media = aluno['nome']
    if media < menor_media:
        menor_media = media
        aluno_menor_media = aluno['nome']

print(f'Aluno {aluno_maior_nota1} tem a maior nota1: {maior_nota1:.2f}')
print(f'Aluno {aluno_maior_media} tem a maior media: {maior_media:.2f}')
print(f'Aluno {aluno_menor_media} tem a menor media: {menor_media:.2f}')

for aluno in alunos:
    media = (aluno['nota1'] + aluno['nota2'] + aluno['nota3'])/3
    nome = aluno['nome']
    if media < 7:
        print(f'Aluno {nome} esta reprovado com media {media:.2f}')
    else:
        print(f'Aluno {nome} esta aprovado com media {media:.2f}')