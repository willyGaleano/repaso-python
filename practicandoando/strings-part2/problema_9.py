def unir_apellido_nombre(nombre_usuario, apellido_usuario):
    full_name = nombre_usuario + apellido_usuario

    return full_name

name_user = input("Ingresa tu nombre: ")
apellido_user = input("Ingresa tu apellido: ")
resul = unir_apellido_nombre(name_user, apellido_user)
print(resul)