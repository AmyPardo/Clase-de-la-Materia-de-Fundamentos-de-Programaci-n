# Definir la matriz 3x3
matriz = [
    [12, 5, 9],
    [3, 8, 1],
    [7, 4, 6]
]

# Función para ordenar una fila específica usando el método de selección (Selection Sort)
def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if matriz[fila][j] < matriz[fila][min_idx]:
                min_idx = j
        matriz[fila][i], matriz[fila][min_idx] = matriz[fila][min_idx], matriz[fila][i]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Pedir al usuario qué fila desea ordenar
fila_a_ordenar = int(input("Ingrese el número de la fila a ordenar (0-2): "))

# Ordenar la fila seleccionada
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
