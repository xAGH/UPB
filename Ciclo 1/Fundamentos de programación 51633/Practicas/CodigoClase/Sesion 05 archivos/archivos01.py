#primer acercamiento con archivos
#abrir un archivo en solo lectura
#ver los metodos y atributos de las funciones
archivo = open("estadisticas.txt","r")
nombre = archivo.name
modo = archivo.mode
codificacion = archivo.encoding
contenido = archivo.read()
archivo.close()

print("el nombre del archivo es: ",nombre)
print("el modo de apertura es: ", modo)
print("la codificacion del archiovo es: ", codificacion)
print("el contenido del archivo es: ", contenido)
