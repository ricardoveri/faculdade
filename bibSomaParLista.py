def SomaPares (lista):
    soma = 0
    novaLista = []
    for i in range (len(lista)):
        if(lista[i] % 2 == 0) and (lista.index(lista[i]) % 2 == 0):
            novaLista.append(lista[i])
    for i in range(len(novaLista)):
        soma += novaLista[i]
    return soma