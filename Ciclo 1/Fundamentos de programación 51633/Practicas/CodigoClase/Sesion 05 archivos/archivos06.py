#escribiendo en archivos - falta el TRY!!!
manejador = open("salida.txt",'w')
print(manejador)
linea1 = "linea 1 del archivo \n"
manejador.write(linea1)
linea2 = "linea 2 del archivo \n"
manejador.write(linea2)
manejador.close()