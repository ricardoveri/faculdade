def FuncaoA(primeiro, segundo):
    if (primeiro - segundo > 0):
        resultado = segundo % 3

    elif (primeiro - segundo < 0):
        resultado = primeiro % 3
        
    else:
        resultado = 3 * (primeiro + segundo)

    return resultado

def funcaoB(numero):
    total = 0
    for i in range(1, numero, 2):
        total += 2 * i
    return total