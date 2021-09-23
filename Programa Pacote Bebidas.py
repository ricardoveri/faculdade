pacoteTropical = 9.00
pacoteSensacao = 12.50
pacoteCaliente = 15.80

pacoteBebida = str.upper(input("Temos: \nPacote Tropical = Coquetéis sem alcóol\nPacote Sensação = Drinks com Rum e Gin\nPacote Caliente = Drinks com vodka\nQual pacote de bebida você quer? "))

quantPessoas = int(input("Quantos convidados irão na festa? "))

if(pacoteBebida == "PACOTE TROPICAL"):
    if(quantPessoas > 50):
         mesaDrink = pacoteTropical * quantPessoas
         desconto = mesaDrink * 0.1
         total = mesaDrink - desconto
         print("O pacote tropical custa R${0:.2f} por pessoa, e vieram mais de 50 pessoas então tem desconto de 10% que vai ser equivalente a R${1:.2f}, O valor total ficará R${2:.2f}".format(pacoteTropical,desconto,total))
    else:
        mesaDrink = pacoteTropical * quantPessoas
        total = mesaDrink
        print("O pacote tropical custa R${0:.2f}, não vieram mais de 50 pessoas, então não tem desconto, o valor total é de R${1:.2f}".format(pacoteTropical,total))

elif(pacoteBebida == "PACOTE CALIENTE"):
    if(quantPessoas > 100):
        mesaDrink = pacoteCaliente * quantPessoas
        desconto = mesaDrink * 0.15
        total = mesaDrink - desconto
        print("O pacote caliente custa R${0:.2f} por pessoa, e vieram mais de 100 pessoas então tem desconto de 15%, que vai ser equivalente a R${1:.2f}, O valor total ficará R${2:.2f}.".format(pacoteCaliente,desconto,total))
    else:
        total = pacoteCaliente
        print("O pacote caliente custa R${0:.2f}, não vieram mais de 100 pessoas, então não tem desconto, o valor total é de R${1:.2f}".format(pacoteCaliente,total))
        
else:
    mesaDrink = pacoteSensacao * quantPessoas
    total = mesaDrink
    print("O pacote sensação custa R${0:.2f} por pessoa, e não tem desconto, o valor total vai ser R${1:.2f}".format(pacoteSensacao,total))
