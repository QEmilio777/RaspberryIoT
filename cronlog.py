from datetime import datetime

ruta = "/home/emilio/Documents/Github/Test/log.txt"
fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(ruta, 'a') as archivo:
    archivo.write(f"Ejecucion del cron: {fecha_hora}\n")
