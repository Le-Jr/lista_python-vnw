d1 = {"a": 2, "b": 3, "c": 5}
d2 = {"a": 1, "b": 4, "d": 7}
dic_final = {}

def soma_dicionario(d1, d2):
    for chave in d1:
        dic_final[chave] = d1[chave] + d2.get(chave, 0)
    
    for chave in d2:
        if chave not in dic_final:
             dic_final[chave] = d2[chave]
    
        
    return dic_final

print(soma_dicionario(d1, d2))
    