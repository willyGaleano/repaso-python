def es_palindromo(palabra):
    palabra_inversa = palabra[::-1]
    print(palabra_inversa)
    if palabra == palabra_inversa:
        return True
    else:
        return False

otra_palabra = input("Ingresa una palabra: ")
resul = es_palindromo(otra_palabra)
print(resul)