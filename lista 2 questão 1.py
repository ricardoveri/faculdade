letras = str.upper(input("Letra: "))
letrasEspec = 0
while(letras != "X"):
    if(letras == "K") or (letras == "Y") or (letras == "W"):
        letrasEspec += 1
        print("continue digitando")
    else:
        print("continue digitando")
        
    letras = str.upper(input("Letra: "))
                           
print("A quantidade de letras especiais lidas foram: %i" %letrasEspec)
         
    
