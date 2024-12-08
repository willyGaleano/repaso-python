def quitar_espacios(nombre_usuario):
    nombre_usuario = nombre_usuario.strip()
    return nombre_usuario

nombre_del_usuario = input("Ingresa tu nombre de usuario: ")
resultado = quitar_espacios(nombre_del_usuario)
print(resultado)