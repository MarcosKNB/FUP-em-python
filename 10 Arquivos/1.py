with open('arq.txt', 'w') as arquivo:
    while True:
        linha = input()
        if linha == '0':
            break
        arquivo.write(linha + '\n')
    arquivo.close()
    
with open('arq.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha, end = '')
    arquivo.close()