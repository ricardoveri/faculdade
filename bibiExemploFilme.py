def filmesAnoDuracao(lista, ano, duracao):
    resposta = []
    for i in range(len(lista)):
        if(Filmes[i][1] == ano) and (Filmes[i][2] < 120):
            resposta.append(lista[1][0])
    return resposta