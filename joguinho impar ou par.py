pontosJogador1 = int(input("Número 1: "))
pontosJogador2 = int(input("Número 2: "))

while(pontosJogador1 != 5) and (pontosJogador2 != 5):
    print("####Nova partida####")
    jogador1 = int(input("Número 1: "))
    jogador2 = int(input("Número 2: "))

    soma = jogador1 + jogador2

    if(soma % 2 == 0):
        pontosJogador1 = pontosJogador1 + 1
    else:
        pontosJogador2 = pontosJogador2 + 1
        
    print("Placar parcial: Jogador 1:", pontosJogador1, "x Jogador 2:", pontosJogador2)
if(pontosJogador1 > pontosJogador2):
    print("Jogador 1 ganhou o jogo")
else:
    print("Jogador 2 ganhou")
