def archivo_existe(ruta: str) -> bool:
    return bool(ruta)

codigo_ruta = input("Ingresa una entrada: ")
resultado = archivo_existe(codigo_ruta)
print(resultado)