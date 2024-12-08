def convertir_minuscula(correo_usuario):
    correo_user = correo_usuario.lower()
    return correo_user

user_mail = input("Ingresa tú correo electrónico: ")
resul = convertir_minuscula(user_mail)
print(resul)
