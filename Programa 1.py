# Definir la matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para buscar un número en la matriz
def buscar_valor(matriz, valor):
    # Recorrer la matriz fila por fila
    for fila in range(3):  # Hay 3 filas
        for columna in range(3):  # Hay 3 columnas
            if matriz[fila][columna] == valor:  # Si encontramos el valor
                return (fila, columna)  # Devolver la posición
    return None  # Si no se encuentra, devolver None

# Pedir al usuario que ingrese un número
valor_buscado = int(input("Ingrese el número que quiere buscar: "))

# Llamar a la función y guardar el resultado
posicion = buscar_valor(matriz, valor_buscado)

# Mostrar el resultado
if posicion is not None:
    print("El número", valor_buscado, "está en la posición:", posicion)
else:
    print("El número", valor_buscado, "no está en la matriz.")
