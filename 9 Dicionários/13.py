dados = {}
dados['nome'] = input()
dados['endereco'] = input()
dados['nascimento'] = input()
dados['cidade'] = input()
dados['cep'] = input()
dados['email'] = input()
deuruim = False
def verificar_data(data):
    if data.count('/') == 2:
        dia, mes, ano = data.split('/')
        if dia.isnumeric() and mes.isnumeric() and ano.isnumeric():
            dia = int(dia)
            mes = int(mes)
            ano = int(ano)
            if dia > 31 or dia < 1 or mes > 12 or mes < 1 or ano < 1:
                return False
            else:
                return True
        else:
            return False
    else:
        return False
        
def verificar_cep(cep):
    if '-' in cep and '.' in cep:
        parte1, resto = cep.split('.')
        parte2, parte3 = resto.split('-')
        if len(parte1) == 2 and len(parte2) == 3 and len(parte3) == 3:
            if parte1.isnumeric() and parte2.isnumeric() and parte3.isnumeric():
                return True
            else:
                return False
        else:
            return False
    else:
        return False


if verificar_data(dados['nascimento']) == False:
    print('Data errada')

elif verificar_cep(dados['cep']) == False:
    print('CEP errado')

elif '@yahoo.com.br' not in dados['email'] or dados['email'].count('@') != 1:
    print('E-mail errado')
else:
    print(dados)