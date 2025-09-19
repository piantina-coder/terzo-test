def moltiplica_lista(lista):
    prodotto = 1
    for numero in lista:
        prodotto *= numero

    if prodotto < 0:
        raise ValueError("Errore il risultato della moltiplicazione è inferiore a 0")
    
    return prodotto

try:
    print(moltiplica_lista([4,6,8]))
    print(moltiplica_lista([-5,2,6]))
except ValueError as e:
    print(e)