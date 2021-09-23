def BuscaAtletasFemPorEsporte (nome, lista):
    novaLista = []
    for i in range (len(lista)):    
        if(lista[i][2] == "f") and (lista[i][3] == nome):
            novaLista.append(lista[i][0])
    return novaLista