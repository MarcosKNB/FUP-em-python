contador = 0
alunos = []
while contador < 5:
    alunos.append(input('Aluno: '))
    contador += 1
    if contador < 5:
        decisao = input('Deseja inserir novo aluno? [S/N] ')
    if decisao == 'N':
        break
aluno = input('Aluno para pesquisa: ')
for i in range(contador):
    if aluno in alunos[i]:
        print(alunos[i])
        print(i)