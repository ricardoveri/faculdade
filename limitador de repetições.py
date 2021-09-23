quantRepeticoes = int(input("Quantas partidas você quer? "))
contador = 0

while(contador < quantRepeticoes):
    num = int(input("Número: "))
    if(num % 2 == 00):
        print("Par")
    else:
        print("Ímpar")

    contador = contador + 1
