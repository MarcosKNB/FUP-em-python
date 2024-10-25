pessoas = []
def menu():
    print('1: Inserir uma pessoa')
    print('2: Buscar por primeiro nome')
    print('3: Buscar por mes de nascimento')
    print('4: Buscar por dia e mes de nascimento')
    print('5: Imprimir agenda')
    print('0: Sair')
    opcao = int(input('Opcao: '))
    return opcao

def inserir_pessoa():
    pessoa = {}
    endereco = {}
    telefone = {}
    nascimento = {}
    pessoa['nome'] = input('Nome: ')
    pessoa['email'] = input('E-mail: ')
    endereco['rua'] = input('Rua: ')
    endereco['numero'] = int(input('Numero: '))
    endereco['complemento'] = input('Complemento: ')
    endereco['bairro'] = input('Bairro: ')
    endereco['cep'] = input('CEP: ')
    endereco['cidade'] = input('Cidade: ')
    endereco['estado'] = input('Estado: ')
    endereco['pais'] = input('Pais: ')
    telefone['ddd'] = int(input('DDD: '))
    telefone['numero'] = input('Telefone: ')
    nascimento['dia'] = int(input('Dia do nascimento: '))
    nascimento['mes'] = int(input('Mes do nascimento: '))
    nascimento['ano'] = int(input('Ano do nascimento: '))
    pessoa['endereco'] = endereco
    pessoa['telefone'] = telefone
    pessoa['nascimento'] = nascimento
    pessoa['observacao'] = input('Observacao: ')
    return pessoa
    
def buscar_pessoa(pessoas):
    busca = input('Primeiro nome: ')
    lista = []
    for pessoa in pessoas:
        primeiro_nome = pessoa['nome'].split()[0].lower()
        if primeiro_nome.startswith(busca.lower()):
            lista.append(pessoa)
    return lista

def buscar_mes(pessoas):
    mes = int(input('Mes de nascimento: '))
    aniversariantes = []
    for pessoa in pessoas:
        if pessoa['nascimento']['mes'] == mes:
            aniversariantes.append(pessoa)
    return aniversariantes

def buscar_dia_mes(pessoas):
    dia = int(input('Dia do nascimento: '))
    mes = int(input('Mes do nascimento: '))
    aniversariantes = []
    for pessoa in pessoas:
        if pessoa['nascimento']['dia'] == dia and pessoa['nascimento']['mes'] == mes:
            aniversariantes.append(pessoa)
    return aniversariantes

def imprimir_agenda(pessoas, opcao):
    lista = []
    if opcao == 1:
        for pessoa in pessoas:
            dados = {}
            dados['nome'] = pessoa['nome']
            dados['telefone'] = pessoa['telefone']
            dados['email'] = pessoa['email']
            lista.append(dados)
    elif opcao == 2:
        for pessoa in pessoas:
            lista.append(pessoa)
    return lista
    
def imprimir_lista(lista):
    for i in lista:
        print(i)
while True:
    opcao = menu()
    lista = []
    if opcao < 0 or opcao > 5:
        print('Opcao invalida')
        continue
    elif opcao == 0:
        break
    
    elif opcao == 1:
        pessoas.append(inserir_pessoa())
    
    elif opcao == 2:
        lista = buscar_pessoa(pessoas)
    
    elif opcao == 3:
        lista = buscar_mes(pessoas)
    
    elif opcao == 4:
        lista = buscar_dia_mes(pessoas)
    elif opcao == 5:
        print('1: Imprimir apenas nome, telefone e email')
        print('2: Imprimir todos os dados')
        opcao = int(input('Opcao: '))
        if opcao < 1 or opcao > 2:
            print('Opcao invalida')
            continue
        lista = imprimir_agenda(pessoas, opcao)
    
    imprimir_lista(lista)