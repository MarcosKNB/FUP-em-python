datas = []
datas_em_ordem = [0]
n_compromissos = int(input())

def data():
    data = {}
    data['dia'] = int(input('Dia: '))
    data['mes'] = int(input('Mes: '))
    data['ano'] = int(input('Ano: '))
    return data
    
def horario():
    horario = {}
    horario['hora'] = int(input('Hora: '))
    horario['minuto'] = int(input('Minuto: '))
    horario['segundo'] = int(input('Segundo: '))
    return horario
    
for i in range(n_compromissos):
    exato = {}
    exato['data'] = data()
    exato['horario'] = horario()
    exato['descricao'] = input('Descricao: ')
    datas.append(exato)

def ordem(data1, data2):
    d1, h1 = data1['data'], data1['horario']
    d2, h2 = data2['data'], data2['horario']
    if (d1['ano'], d1['mes'], d1['dia'], h1['hora'], h1['minuto'], h1['segundo']) < (d2['ano'], d2['mes'], d2['dia'], h2['hora'], h2['minuto'], h2['segundo']):
        return True
    else:
        return False

for i in range(n_compromissos):
    for j in range(n_compromissos -i -1):
        if ordem(datas[j], datas[j+1]) == False:
            datas[j], datas[j+1] = datas[j+1], datas[j]

for data in datas:
    print(data)