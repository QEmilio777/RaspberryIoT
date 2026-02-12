# MCP3008_simple.py
# Librería estilo ADC0834 con opción de rango 0–255 o 0–1023

from gpiozero import MCP3008 as _MCP
import time

# Inicializa 8 canales
_channels = [_MCP(channel=i) for i in range(8)]

def getResult(channel=0, bits=8):
    """
    Lee un canal (0-7) del MCP3008 y devuelve un valor escalado.
    - bits=8 → valor 0-255
    - bits=10 → valor 0-1023
    """
    if not 0 <= channel <= 7:
        raise ValueError("Canal debe ser entre 0 y 7")
    raw = _channels[channel].value  # 0.0 - 1.0

    if bits == 8:
        return int(raw * 255)
    elif bits == 10:
        return int(raw * 1023)
    elif bits == 12:
        return int(raw * 4095)
    else:
        raise ValueError("bits debe ser 8 o 10")

def getResult1(bits=8):  # compatibilidad con ADC0834
    return getResult(1, bits=bits)

def loop(bits=8, delay=0.5):
    """Ejemplo de lectura continua de todos los canales"""
    try:
        while True:
            for i in range(8):
                print(f"res{i} = {getResult(i, bits=bits)}")
            time.sleep(delay)
    except KeyboardInterrupt:
        print("Lectura finalizada")