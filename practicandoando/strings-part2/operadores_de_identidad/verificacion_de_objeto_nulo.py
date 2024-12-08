def es_objeto_nulo(objeto: any) -> bool:
    if objeto is None:
        return True
    else:
        return False

print(es_objeto_nulo(None))