def AtletasMenores(lista):
    novaLista = []
    for i in range (len(lista)):    
        if(lista[i][1] < 18):
            novaLista.append(lista[i][0])

    return novaLista