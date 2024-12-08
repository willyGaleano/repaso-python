def es_diccionario_vacio(diccionario: dict) -> bool:
    return bool(diccionario)

codigo_diccionario = input("Ingresa tu diccionario: ")
resul = es_diccionario_vacio(codigo_diccionario)
print(resul)