livros = []
while True:
    livro = input("Digite o titulo do livro")
    if livro == "0":
        for livro in livros:
            print(livro)
        break
    livros.append(livro)