palavra = "banana maçã banana laranja maçã maçã"

def conta_palavra(palavra):
    lista_palavras = palavra.split()
    dicionario = {}
    
    for palavra in lista_palavras:
      
        contagem = lista_palavras.count(palavra)
        dicionario[palavra] = contagem
        
    return dicionario

print(conta_palavra(palavra))