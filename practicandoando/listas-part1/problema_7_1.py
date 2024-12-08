def retornar_3_ultimas_canciones(lista_canciones):
    return lista_canciones[-3:]


canciones = ["Canción1", "Canción2", "Canción3", "Canción4", "Canción5", "Canción6", "Canción7", "Canción8"]
lista_3_ultimas_canciones = retornar_3_ultimas_canciones(canciones)
print(lista_3_ultimas_canciones)