import random

# Definir dimensiones
ciudades = ["Guayaquil", "Quito", "Riobamba"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4  # Un mes

# Crear matriz 3D para almacenar temperaturas
matriz_temperaturas = []

# Llenar la matriz con valores aleatorios de temperatura
for ciudad in ciudades:
    temperaturas_ciudad = []
    for semana in range(semanas):
        temperaturas_semana = [random.uniform(10, 35) for _ in dias_semana]  # Temperaturas entre 10 y 35 grados
        temperaturas_ciudad.append(temperaturas_semana)
    matriz_temperaturas.append(temperaturas_ciudad)

# Calcular y mostrar el promedio de temperaturas por ciudad y semana
for i, ciudad in enumerate(ciudades):
    print(f"Promedio de temperaturas para {ciudad}:")
    for semana in range(semanas):
        promedio = sum(matriz_temperaturas[i][semana]) / len(dias_semana)
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")
    print()
