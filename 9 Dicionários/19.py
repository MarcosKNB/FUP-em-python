pessoamaioridade = {}
cadastros = []
homens = []
salario1000 = []
pessoamaioridade['idade'] = 0
for i in range(5):
    pessoa = {}
    endereco = {}
    pessoa['nome'] = input('Nome: ')
    endereco['rua'] = input('Rua: ')
    endereco['bairro'] = input('Bairro: ')
    endereco['cidade'] = input('Cidade: ')
    endereco['estado'] = input('Estado: ')
    endereco['cep'] = input('CEP: ')
    pessoa['endereco'] = endereco
    pessoa['salario'] = float(input('Salario: '))
    pessoa['identidade'] = input('Identidade: ')
    pessoa['cpf'] = input('CPF: ')
    pessoa['civil'] = input('Estado Civil: ')
    pessoa['telefone'] = input('Telefone: ')
    pessoa['idade'] = int(input('Idade: '))
    pessoa['sexo'] = input('Sexo: ')
    cadastros.append(pessoa)
    
for pessoa in cadastros:
    if pessoa['sexo'] == 'Masculino':
        homens.append(pessoa)
    if pessoa['idade'] > pessoamaioridade['idade']:
        pessoamaioridade = pessoa
    if pessoa['salario'] > 1000:
        salario1000.append(pessoa)

print('Pessoa com maior idade: ')
print(pessoamaioridade)
print('Pessoas do sexo masculino: ')
if len(homens) >= 1:
    for homem in homens:
        print(homem)
print('Pessoas com salario maior que 1000: ')
if len(salario1000) >= 1:
    for pessoa in salario1000:
        print(pessoa)
        
ident = input('Identidade: ')

for pessoa in cadastros:
    if pessoa['identidade'] == ident:
        print(pessoa)
        break