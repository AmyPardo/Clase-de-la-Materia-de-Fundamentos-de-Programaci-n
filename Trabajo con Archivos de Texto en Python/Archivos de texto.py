# Escribimos información personal en un archivo de texto

archivo = open("my_notes.txt", "w")  # Abrimos el archivo para escribir

archivo.write("Me llamo Amy Pardo.\n")
archivo.write("Me gusta jugar futbol.\n")
archivo.write("Tengo 18 años de edad.\n")

archivo.close()  # Cerramos el archivo después de escribir

# Ahora vamos a leer lo que escribimos

archivo = open("my_notes.txt", "r")  # Abrimos el archivo para leer

# Leemos las líneas manualmente
linea1 = archivo.readline()
linea2 = archivo.readline()
linea3 = archivo.readline()

# Imprimimos cada línea
print("Primera línea:", linea1.strip())
print("Segunda línea:", linea2.strip())
print("Tercera línea:", linea3.strip())

archivo.close()  # Cerramos el archivo al final
