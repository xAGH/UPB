#escribiendo en archivos binarios
manejador = open("salidab.txt",'wb')
print(manejador)
linea1 = bytearray([3,6,7,8,7,7,7,7,7,7,7,45,34])
manejador.write(linea1)
linea2 = bytearray([150,67])
manejador.write(linea2)
manejador.close()