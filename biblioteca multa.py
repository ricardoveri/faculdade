#Regras do Negócio
multaDiaria = 0.75

#Entrada
diasAtraso = int(input("Quantos dias de atraso: "))

#Processamento
multa = diasAtraso * multaDiaria


#Saida
print("A multa a ser paga é R$ %.2f" %multa)
