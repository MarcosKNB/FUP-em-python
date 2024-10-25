agenda = []

for i in range(5):
    marcado = {}
    marcado['compromisso'] = input('Descricao: ')
    marcado['data'] = {}
    marcado['data']['dia'] = int(input('Dia: '))
    marcado['data']['mes'] = int(input('Mes: '))
    marcado['data']['ano'] = int(input('Ano: '))
    agenda.append(marcado)

m = 1
while True:
    m = int(input())
    if m == 0:
        break
    a = int(input())
    ordem = []
    for marcado in agenda:
        if marcado['data']['mes'] == m and marcado['data']['ano'] == a:
            ordem.append(marcado)
    for i in range(len(ordem)):
        for j in range(len(ordem)-1-i):
            if ordem[j]['data']['dia'] > ordem[j+1]['data']['dia']:
                ordem[j], ordem[j+1] = ordem[j+1], ordem[j]
    for compromisso in ordem:
        print(compromisso)