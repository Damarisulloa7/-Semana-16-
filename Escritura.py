# Escritura del archivo de texto
# ---------------------------

# Crear y abrir el archivo en modo escritura ('w')
archivo = open("my_notes.txt", "w")

# Escribir tres líneas de notas personales
archivo.write("1. Revisar el informe de ventas antes del viernes.\n")
archivo.write("2. Enviar recordatorio al equipo sobre la reunión de proyectos.\n")
archivo.write("3. Actualizar la base de datos de clientes con los nuevos registros.\n")

# Cerrar el archivo para guardar cambios
archivo.close()

# ---------------------------
# Lectura del archivo de texto
# ---------------------------

# Abrir el archivo en modo lectura ('r')
archivo = open("my_notes.txt", "r")

# Leer línea por línea usando readline()
print("Contenido del archivo:")
linea = archivo.readline()  # Leer primera línea
while linea:
    print(linea.strip())  # .strip() elimina saltos de línea adicionales
    linea = archivo.readline()  # Leer siguiente línea

# Cerrar el archivo después de leer
archivo.close()