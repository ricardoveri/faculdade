#RegrasDoNegócio
saborMorCer = 4.50
saborDamSir = 3.80
outroSabor = 2.75

#Entrada
saborSorvete = str.upper(input("Qual o sabor de sorvete você quer? "))                        
quantBolas = int(input("Quantas bolas de sorvete você quer? "))                        

#Processamento
if(saborSorvete == "MORANGO") or (saborSorvete == "CEREJA"):
    valorTotal = quantBolas * saborMorCer
elif(saborSorvete == "DAMASCO") or (saborSorvete == "SIRIGUELA"):
    valorTotal = quantBolas * saborDamSir
else:
    valorTotal = quantBolas * outroSabor
    
print("O valor total a ser pago vai ser: R$%.2f" %valorTotal)

if(quantBolas >= 2):
    print("Você ganhou uma calda de caramelo")
else:
    print("Vacilou em, não ganhou calda de caramelo")

#Saída

