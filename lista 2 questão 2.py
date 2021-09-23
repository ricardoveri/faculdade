numero = int(input("Digite o número: "))
quantPares = 0
paresDigi = 0
while(numero != 100):
    if(numero % 2 == 0):
        quantPares += 1
        paresDigi = paresDigi + numero
        print("Continue digitando")
    else:
        print("Continue digitando")
             
    numero = int(input("Digite o número: "))

if(quantPares > 0):
    mediaPar = paresDigi // quantPares
    print("A média dos números pares é: %i" %mediaPar)
else:
    print("Não foram lidos números pares")

