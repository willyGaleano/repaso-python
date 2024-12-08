def diferencia_de_temperatura(lista_temperaturas: list[int]) -> int:
    penultima_temperatura = lista_temperaturas[-2]
    ultima_temperatura = lista_temperaturas[-1]
    diferencia = penultima_temperatura - ultima_temperatura
    return diferencia

temperaturas = [22, 23, 21, 24, 23, 22, 20, 15, 15]
diferencia_de_2_ultimas_temperaturas = diferencia_de_temperatura(temperaturas)
print(diferencia_de_2_ultimas_temperaturas)