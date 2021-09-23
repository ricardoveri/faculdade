#Regras do Negócio
valorCopia = 0.08
quantPaginasFolha = 2

#Entrada
quantFolhas = int(input("Quantas folhas tem o livro?: "))

#Processamento
valorPagar = (quantFolhas * quantPaginasFolha) * valorCopia
                  
#Saída
print("Valor total a ser pago é R$ %.2f" %valorPagar)
