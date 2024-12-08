def es_elemento_permitido(elemento: int, lista_permitidos: list[int]) -> bool:
    if elemento in lista_permitidos:
        return True
    else:
        return False

print(es_elemento_permitido(2, [1, 3, 5, 7, 9]))
