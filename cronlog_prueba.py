from datetime import datetime

time = datetime.now().strftime("%d-%m-%y, %H:%M:%S")

ruta = "/home/emilio/Documents/Github/Test/cronolog_prueba.txt"

with open(ruta, 'a') as archivo_cronolog:
    archivo_cronolog.write(f"Ejecutado el: {time}\n")

print('Done')