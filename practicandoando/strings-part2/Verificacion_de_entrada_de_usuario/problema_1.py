def verificar_edad(edad_usuario):
    edad_no_valida = ""
    if edad_usuario == edad_no_valida:
       return "Ingrese su edad sin dejar campos vacíos"
    else:
        return "Su edad es válida"

edad_user = input("Ingrese su edad: ")
resultado = verificar_edad(edad_user)
print(resultado)

