try:
    print("Verificando archivo...")
    with open('datos.txt') as archivo:
        archivo.write("el programa tercero")
except BaseException as e:
    print(e)
finally:
    print("Todo listo")