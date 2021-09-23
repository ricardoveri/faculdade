vacinasApli = 0
informar = "SIM"
while(informar != "NÃO"):
    idade = int(input("Qual a idade da criança? "))
    if(idade >= 3) and (idade <= 6):
        vacinasApli += 1
    informar = str.upper(input("Deseja informar mais idades? "))
    
print("Total de vacinas aplicas: {}".format(vacinasApli))
        
