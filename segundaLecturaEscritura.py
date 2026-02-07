try:
    with open('datos.txt', 'a') as archivo:
        archivo.write("el programa\n")
except BaseException as e:
    print(e)
finally:
    print("Todo listo")