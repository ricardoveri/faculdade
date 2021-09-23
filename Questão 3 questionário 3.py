#Regras do Negócio
precoGasolina = 2.53
precoEtanol = 2.09
precoDiesel = 1.92

#Entrada
tipoCombustivel = str.upper(input("Qual o tipo de combustível? "))
valor = float(input("Qual o valor em dinheiro? "))

#Processamento
if(tipoCombustivel == "GASOLINA"):
   totalLitros = valor / precoGasolina   
elif (tipoCombustivel == "ETANOL"):
   totalLitros = valor / precoEtanol
elif(tipoCombustivel == "DIESEL"):
    precoCombustivel = precoDiesel
    
totalLitros = valor / precoDiesel

#Saida
print("O total de litros é {0:.2f}".format(totalLitros))

if(tipoCombustivel == "ETANOL") and (totalLitros > 30):
    print("Ganhou troca de óleo")
else:
    print("Não ganhou troca de óleo")
