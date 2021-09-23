quantJovens = 0
maiorIdadeAdulto = 0
somaIdosos = 0
quantIdosos = 0

idade = int(input("Idade: "))
while(idade >= 0):

    if(idade < 20):
        quantJovens += 1
    elif(idade < 60):
        if(idade > maiorIdadeAdulto):
            maiorIdadeAdulto = idade
    else:
        quantIdosos += 1
        somaIdosos += idade

    idade = int(input("Idade: "))

#Exibição Jovens
if(quantJovens == 0):
    print("Não há jovens")
else:
    print("Quantidade de jovens -->", quantJovens)

#Exibição Adultos
if(maiorIdadeAdulto == 0):
    print("Não há adultos")
else:
    print("Maior idade adulto -->", maiorIdadeAdulto)

#Exibição Idosos
if(quantIdosos == 0):
    print("Não há idosos")
else:
    mediaIdosos = somaIdosos / quantIdosos
    print("Média de idade idosos -->", mediaIdosos)
