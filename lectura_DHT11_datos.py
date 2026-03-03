from pymodbus.client import ModbusTcpClient
import time
import datetime

IP = "IP"
PORT = 502
UNIT_ID = 1

client = ModbusTcpClient(IP, port=PORT)

if not client.connect():
    print("Error de conexion")
    exit()

print("Leyendo cada 2 segundos")
try:
    
    while True:
        
        rr = client.read_holding_registers(0, count=1, device_id=UNIT_ID)
        if rr.isError():
            print("Error en la lectura")
        else:
            temp = rr.registers[0]
            humid = rr.registers[1]
            
            print(f"Temperatura: {(temp/100):.2f} || Humedad: {(humid/100):.2f}")
            
            datos = {
                "Temperatura": temp,
                "Humedad": humid,
                "Fecha": datetime.datetime.now.strftime("%Y-%m-%d %H:%M:%S")
            }
            ruta = "/home/emilio/Documents/Github/GPIO/datos_DHT11.csv"
            
            with open(ruta, 'a', newline='') as csvfile:
                file = csvfile.write()
                
        
        time.sleep(2)

except KeyboardInterrupt:
    print("CTRL c ejecutado")
finally:
    client.close()
    print("Programa finalizado")