def tiene_acceso(rol: str, cuenta_activa: bool) -> bool:
    if (rol == "admin" or "usuario") and cuenta_activa:
        return True
    else:
        return False
print(tiene_acceso("admin", True))