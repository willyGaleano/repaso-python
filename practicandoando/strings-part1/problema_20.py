def detectar_caracteres_validos(cadena: str, caracteres_especiales:str) -> str:
    for caracter in cadena:
        if caracter in caracteres_especiales:
            return "Ingrese caracteres válidos."

    return "Los caracteres son válidos."



caracteres_especiales = "!@#$%"

cadena = input("Ingrese un texto: ")

resultado = detectar_caracteres_validos(cadena, caracteres_especiales)
print(resultado)


