informacion_personal = {"nombre": "Amy", "edad": 18, "ciudad": "Quito", "profesion": "Estudiante"}
print (informacion_personal)
# Modificar la ciudad
informacion_personal["ciudad"] = "Guayaquil"
print (informacion_personal)
# Modificar la profesión
informacion_personal["profesion"] = "Maquilladora"
print (informacion_personal)
# Verificar si "telefono" existe, si no, agregarlo
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "00000000"
print (informacion_personal)
# Eliminar la clave "edad"
del informacion_personal["edad"]
print(informacion_personal)
