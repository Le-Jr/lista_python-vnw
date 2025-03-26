def ordenar_por_idade(lista):
    return sorted(lista, key=lambda x: x[1])

pessoas = [("João", 25), ("Maria", 20), ("Pedro", 30)]
print(ordenar_por_idade(pessoas))
