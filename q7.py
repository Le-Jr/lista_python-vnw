def conta_freq(lista):
    dicionario = {}

    for num in lista:
        if num in dicionario:
            dicionario[num] += 1
        else:
            dicionario[num] = 1

    return dicionario

def top_3_frequentes(lista):
    frequencias = conta_freq(lista)

    top_3 = sorted(frequencias, key=frequencias.get, reverse=True)[:3]

    return top_3  

lista_num = [1, 3, 3, 2, 1, 1, 4, 4, 4, 2, 2, 2, 5, 5]
resultado = top_3_frequentes(lista_num)
print(resultado)
