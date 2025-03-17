def calcular_promedio(datos):
    # Diccionario para guardar los promedios
    promedios = {}

    for ciudad in datos:
        suma = 0
        cantidad = 0

        for semana in datos[ciudad]:
            for temp in semana:
                suma = suma + temp  # Sumar cada temperatura
                cantidad = cantidad + 1  # Contar cada dato

        promedio = suma / cantidad  # Calcular el promedio
        promedios[ciudad] = promedio  # Guardar el resultado

    return promedios


# Datos de temperatura de varias ciudades
datos = {
    "Guayaquil": [[30, 32, 31, 29, 28, 27, 30], [31, 33, 34, 32, 30, 29, 28], [29, 30, 28, 27, 26, 25, 24],
                  [32, 31, 30, 28, 29, 27, 26]],
    "Quito": [[19, 20, 18, 17, 16, 15, 14], [20, 21, 22, 19, 18, 17, 16], [18, 19, 17, 16, 15, 14, 13],
              [21, 20, 19, 18, 17, 16, 15]],
    "Riobamba": [[13, 15, 14, 12, 11, 10, 9], [15, 16, 17, 14, 13, 12, 11], [14, 15, 13, 12, 11, 10, 9],
                 [16, 15, 14, 13, 12, 11, 10]]
}

# Imprimir los resultados
print(calcular_promedio(datos))