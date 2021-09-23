maiorPontuacao = 0
quantParticipantes = 4

cont = 0
while(cont < quantParticipantes):
    
    nome = input("Nome: ")
    pontos = int(input("Pontos: "))

    while(pontos < 0):
        pontos = int(input("Pontuação inválida. Digite novamente: "))

    if(pontos > maiorPontuacao):
        maiorPontuacao = pontos
        nomeMaiorPontuacao = nome


    cont += 1

print("A pessoa que teve maior pontuação foi", nomeMaiorPontuacao)
