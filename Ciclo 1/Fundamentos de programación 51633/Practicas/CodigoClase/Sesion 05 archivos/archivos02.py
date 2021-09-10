#archivos - recuerde usar bien el try con archivos
try:
    with open("datos01.txt","r") as archivo:
        print("abriendo el archivo ",archivo.name)
        print("estado de la bandera closed: ",archivo.closed)
        print("manejador del archivo", archivo)
        contenido = archivo.read()
except:
    print("algo fallo con la lectura del archivo")
print("estado de la bandera closed: ",archivo.closed)