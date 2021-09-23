informar = "SIM"
entradasGrat = 0

while(informar != "NÃO"):
    idade = int(input("Qual a sua idade? "))
    if(idade > 0) and (idade <= 10):
        entradasGrat += 1
    elif(idade > 60):
        entradasGrat += 1
    informar = str.upper(input("Deseja informar mais números? "))
    
print("Total de entradas gratuitas: %i" %entradasGrat)
        

    
