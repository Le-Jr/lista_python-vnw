dicionario = {"Ana" : [8,7,9], "Bruno": [5,6,5], "Carlos": [10,9,10] }

def media_tupla(notas):
    lista_medias = []
    tuplas = ()
    for notas in dicionario:
        valores = dicionario[notas]
        media = round(sum(valores) / len(valores), 2 )
        tuplas = notas, media
        
        lista_medias.append(tuplas)
    return f"Estas sons las tuplas {lista_medias}"
        

print(media_tupla(dicionario))