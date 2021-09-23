tamLista = 3
filmes = []
cont = 0
cont1 = 0
for i in range(tamLista):
    titulo = input("Título do filme: ")
    ano = int(input("Ano do filme: "))
    duracaoFilme = int(input("Duração de filme em minutos: "))
    print("")
    f = [titulo, ano, duracaoFilme]
    filmes.append(f)
    
print("\na) Lista com título de filmes lançados em 2019 com menos de 120 minutos:", end = " ")
for i in range(tamLista):
    if(filmes[i][1] == 2019) and (filmes[i][2] < 120):
        print([filmes[i][0]])
        cont += 1

if(cont == 0):
        print("Não existem filmes lançados em 2019 com menos de 120 minutos") 

somaTempo = 0
for i in range(tamLista):
    if(filmes[i][1] >= 1990) and (filmes[i][1] <= 2000):
        somaTempo += filmes[i][2]
        cont1 += 1
        media = somaTempo / cont1

if(cont1 == 0):
    print("Não existem filmes lançados entre 1990 e 2000")
else:
    print("\nb) A duração média dos filmes em minutos lançados entre 1990 e 2000: {:.2f} horas".format(media))
    
