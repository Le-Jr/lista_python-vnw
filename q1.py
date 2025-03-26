def soma_par(lista_num):
    soma =  0   
    for numero in lista_num:
        if numero % 2 == 0:
            soma += numero

    return soma

lista = [3,5,7,9,6,2]

print(soma_par(lista))