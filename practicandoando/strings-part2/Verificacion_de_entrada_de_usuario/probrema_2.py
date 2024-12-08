def es_entrada_valida(entrada: str) -> bool:
    return bool(entrada)

entrada = input("Ingresa tu entrada de usuario: ")
resultado = es_entrada_valida(entrada)
print(resultado)
