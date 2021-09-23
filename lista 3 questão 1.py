informar = "SIM"
somaMult = 0
while(informar != "NÃO"):
    num = int(input("Digite um número: "))
    if(num % 3 == 0):
        somaMult += num
    informar = str.upper(input("Deseja informar mais números? "))
print("A soma dos múltiplos de 3: %i" %somaMult)
