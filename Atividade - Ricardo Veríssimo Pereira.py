#RegrasDoNegócio
ovoTrad = 20
ovoTruf = 30

#Entrada
tipoOvo = str.upper(input("Escolha qual ovo você quer: "))
quantOvos = int(input("Quantos ovos você quer: "))

#Processamento
if(tipoOvo == "TRUFADO"):
    valorTotal = quantOvos * ovoTruf
elif(tipoOvo == "TRADICIONAL"):
    valorTotal = quantOvos * ovoTrad
if(quantOvos >= 3):
    print("A taxa de entrega é gratuita")
else:
    print("O valor do frete é R$ 7")
    valorTotal += 7

#Saída
print("O valor total a ser pago é: R$ ", valorTotal)
