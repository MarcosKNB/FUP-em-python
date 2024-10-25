livros = []

for i in range(5):
    dadoslivros = {}
    dadoslivros['titulo'] = input()
    dadoslivros['autor'] = input()
    dadoslivros['ano'] = int(input())
    livros.append(dadoslivros)
    
pesquisa = input()

for livro in livros:
    if pesquisa.lower() in livro['titulo'].lower():
        print(livro)