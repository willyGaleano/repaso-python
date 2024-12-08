def es_lista_vacia(lista: list) -> bool:
    return bool(lista)

codigo_lista = input("Ingresa tu lista: ")
resul = es_lista_vacia(codigo_lista)
print(resul)