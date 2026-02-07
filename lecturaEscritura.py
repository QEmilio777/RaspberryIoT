print("Bucando el archivo: 'datos.txt'")
archivo = open("datos.txt", 'a')

print("'datos.txt' ha sido abierto")
archivo.write("Se ejecuto el programa\n")

print("Se agregro el mensaje a el archivo 'datos.txt'")
archivo.close()

print("Se cerro el archivo 'datos.txt'")
