custoMatricula = 120
custoIngles = 200
custoFrances = 170
custoAlemao = 185

idiomaEscolhido = str.upper(input("Qual o idioma você deseja? "))
totalSemanas = int(input("Quantas semanas você pretende estudar? "))

if(idiomaEscolhido == "INGLÊS"):
    valorTotal = (Ingles * totalSemanas) + Matricula
elif(idiomaEscolhido == "FRANCÊS"):
    valorTotal = (Frances * totalSemanas) + Matricula
else:
    valorTotal = (Alemao * totalSemanas) + Matricula

print("O valor total a ser pago juntamente com a matrícula vai ser: R$%.2f" %valorTotal)

