taxa = 150
decisaoOficina = str.lower(input("Você quer oficina? "))
if(decisaoOficina == "sim"):
    nomeOficina = str.lower(input("Qual oficina? "))
    if(nomeOficina == "aplicativos moveis"):
        taxaO = 130
    elif(nomeOficina == "jogos 3d"):
        taxaO = 80
    total = taxaO + taxa    
    periodo = int(input("Qual período você está matrículado? "))
    if(periodo == 2):
        total = taxaO + taxa - 20
    print("Total a pagar: R$ {0:.2f}".format(total))
else:
 total = taxa
 print("Total a pagar: R$ {0:.2f}".format(total))