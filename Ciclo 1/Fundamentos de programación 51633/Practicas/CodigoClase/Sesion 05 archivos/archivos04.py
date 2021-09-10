#lectura de archivos usando ciclos, recuerde el tamaño del archivo, 
#No leer de una sola vez todo un archivo grande!!!!
try:
    archivo = open("datos01.txt","r")
    contadorlineas = 0
    for linea in archivo:
        contadorlineas = contadorlineas + 1
    print("lineas en el archivo = ", str(contadorlineas))    

except:
    print("algo fallo con la lectura del archivo")