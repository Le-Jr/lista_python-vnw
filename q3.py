def arruma_dic(frase):
    dicionario = {}
    palavras = frase.split()
    print(palavras)
    for palavra in palavras:
        dicionario[palavra] = len(palavra)
        
        
    return dicionario
    



frase_grande = "Java Java Ruby Javascript Ruby"
print(arruma_dic(frase_grande))
