
'''
def verificar_acceso_usuario(rol_usuario):
    roles = ["admin", "publico1", "publico2", "supervisor"]

    if rol_usuario in roles:
        if rol_usuario == "admin" or rol_usuario == "supervisor":
            return True
        else:
            return False
    else:
        return False
'''

def verificar_acceso_usuario(rol_usuario):
    roles = ["admin", "publico1", "publico2", "supervisor"]

    #Primero validamos que el rol ingresado exista en mi lista
    if rol_usuario not in roles:
        return False

    es_un_rol_con_permisos: bool = rol_usuario == "admin" or rol_usuario == "supervisor"

    return es_un_rol_con_permisos

resul = verificar_acceso_usuario("admin")
print(resul)