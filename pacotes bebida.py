pacoteTropical = 9.00
pacoteSensacao = 12.50
pacoteCaliente = 15.80

pacoteBebida = str.upper(input("Temos: \nPacote Tropical = Coquetéis sem alcóol\nPacote Sensação = Drinks com Rum e Gin\nPacote Caliente = Drinks com vodka\nQual pacote de bebida você quer? "))    
while(pacoteBebida != "PACOTE TROPICAL") or (pacoteBebida != "PACOTE CALIENTE") or (pacoteBebida != "PACOTE SENSAÇÃO"):
    pacoteBebida = str.upper(input("Temos: \nPacote Tropical = Coquetéis sem alcóol\nPacote Sensação = Drinks com Rum e Gin\nPacote Caliente = Drinks com vodka\nQual pacote de bebida você quer? "))
    
while(pacoteBebida == "PACOTE TROPICAL") or (pacoteBebida == "PACOTE CALIENTE") or (pacoteBebida == "PACOTE SENSAÇÃO"):
    quantPessoas = int(input("Quantos convidados irão na festa? "))
    if(pacoteBebida == "PACOTE TROPICAL"):
        if(quantPessoas > 50):
            desconto = pacoteTropical * 0.1
            total = pacoteTropical - desconto
            print("Vieram mais de 50 pessoas então tem desconto de 10% que vai ser equivalente a R${0:.2f}, O valor total ficará R${1:.2f}.".format(desconto,total))
        else:
            total = pacoteTropical
            print("O pacote tropical custa R${0:.2f}, não vieram mais de 50 pessoas, então não tem desconto, o valor total é de R${1:.2f}".format(pacoteTropical,total))

    elif(pacoteBebida == "PACOTE CALIENTE"):
        if(quantPessoas > 100):
            desconto = pacoteCaliente * 0.15
            total = pacoteCaliente - desconto
            print("Vieram mais de 100 pessoas então tem desconto de 15%, que vai ser equivalente a R${0:.2f}, O valor total ficará R${1:.2f}.".format(desconto,total))
        else:
            total = pacoteCaliente
            print("O pacote caliente custa R${0:.2f}, não vieram mais de 100 pessoas, então não tem desconto, o valor total é de R${1:.2f}".format(pacoteCaliente,total))
        
    else:
        total = pacoteSensacao
        print("O pacote sensação não tem desconto, o valor total vai ser R${0:.2f}".format(total))
    pacoteBebida = str.upper(input("Temos: \nPacote Tropical = Coquetéis sem alcóol\nPacote Sensação = Drinks com Rum e Gin\nPacote Caliente = Drinks com vodka\nQual pacote de bebida você quer? "))    
