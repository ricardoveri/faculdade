quantParesPositivos = 0

tentativas = 0

while(tentativas < 5):
   
    num = int(input("Número: "))
    if(num % 2 == 0) and (num > 0):
        quantParesPositivos += 1
    
    tentativas += 1 

print("Quantidade: {}".format(quantParesPositivos))
