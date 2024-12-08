def contiene_palabra(texto: str, palabra: str) -> bool:
    if palabra in texto:
        return True
    else:
        return False

print(contiene_palabra("hola serrano", " "))