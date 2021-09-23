quantPgLivro = int(input("Quantidade de páginas por livro: "))
while(quantPgLivro > 0):
    quantDiaConcurso = int(input("Quantos dias faltam para o concurso? "))
    if((22 * quantDiaConcurso) >= quantPgLivro):
        print("\nConseguirá estudar\n")
    else:
        print("\nNão conseguirá estudar... Sinto muito\n")
    quantPgLivro = int(input("Quantidade de páginas por livro: "))

