pecaporRoupa = 7.00
kgRoupa = 5.00

lavagemASeco = 3.50
quantLavagensASeco = 0

contador = 0
valorArrecadado = 0
for quantPedidos in range(50):
    lavagemRoupa = str.upper(input("Deseja lavar as roupas por peça ou quilo? "))
    if(lavagemRoupa == "PEÇA"):
        quantPecas = int(input("Quantas peças você quer lavar? "))
        formaLavar = str.upper(input("Quer lavagem a seco? "))
        if(formaLavar == "SIM"):
            valorTotal = (pecaporRoupa * quantPecas) + lavagemASeco
            quantLavagensASeco += 1
        else:
            valorTotal = pecaporRoupa * quantPecas
            
    elif(lavagemRoupa == "QUILO"):
        quantKgPecas = int(input("Quantos quilos de roupa você quer lavar? "))
        formaLavar = str.upper(input("Quer lavagem a seco? "))
        if(formaLavar == "SIM"):
            valorTotal = (kgRoupa * quantKgPecas) + lavagemASeco
            quantLavagensASeco += 1
        else:
            valorTotal = kgRoupa * quantKgPecas
    valorArrecadado += valorTotal
    
    for c in range(1):
        print(f"O valor do {contador + 1} pedido é: R${valorTotal:.2f}")
        contador += 1
        
print("O valor total arrecado foi: R${:.2f}".format(valorArrecadado))
print("Quantidade de lavagens a seco foi: {}".format(quantLavagensASeco))
            
        
