from pymodbus.client import ModbusTcpClient
from time import sleep

PORT = 502
IP = "192.168.47.30"
COIL_relay = 6

client = ModbusTcpClient(IP, port=PORT)

try:
    while True:
        print("\n1 para encender | 0 para apagar | q para salir")
        respuesta = input("")
        
        if respuesta.lower() == 'q':
            break
        
        if respuesta not in ["1", "0"]:
            print("Respuesta fuera de los limites")
            continue
        
        valor = bool(int(respuesta))
        client.write_coil(COIL_relay, valor)
        
        print("El estado del relay es " + "encendido" if valor else "apagado")
except KeyboardInterrupt:
    print("\nContorl C ejecutado")
finally:
    client.write_coil(COIL_relay, False)
    client.close()
    print("\nPrograma finalizado")