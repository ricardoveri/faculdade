tamLista = 3
escola = []
cont = 0
for i in range(tamLista):
    nome = input("Nome: ")
    bairro = str.upper(input("Qual o bairro? "))
    quantAlunos = int(input("Quantidade alunos: "))
    e = [nome, bairro, quantAlunos]
    escola.append(e)
    
print("\na) Nome das escolas do centro com mais de 500 alunos:", end = " ")
for i in range(tamLista):
    if(escola[i][2] > 500) and (escola[i][1] == "CENTRO"):
        print(escola[i][0])
        cont += 1
        
if(cont == 0):
    print("Não existem escolas do centro com mais de 500 alunos")

somaTotal = 0
for i in range(tamLista):
    if(escola[i][1] == "COLINAS"):
        somaTotal += escola[i][2]
        
print("\nb) Quantidade total de alunos do bairro Colinas: {}".format(somaTotal))
