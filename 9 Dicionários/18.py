produtos = []
codigos = []
for i in range(5):
    produto = {}
    produto['codigo'] = int(input())
    produto['nome'] = input()
    produto['preco'] = float(input())
    produto['quantidade'] = int(input())
    codigos.append(produto['codigo'])
    produtos.append(produto)

while True:
    for i in range(5):
        print(produtos[i])
    cod = int(input())
    if cod == 0:
        break
    qtd = int(input())
    if not cod in codigos:
        print('Impossivel atender ao pedido, codigo nao encontrado')
    for prod in produtos:
        if prod['codigo'] == cod:
            if qtd <= prod['quantidade']:
                prod['quantidade'] = prod['quantidade'] - qtd
            else:
                print('Impossivel atender ao pedido, produto sem estoque suficiente')