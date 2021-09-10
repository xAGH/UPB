#Leer un archivo y cargar la estructura en un diccionario 
#cargar el archivo y pasar a un diccionario los elementos respectivos en orden
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
print(type(contenido))
a=contenido.split("\n")
print(a)
diccionario = {}
diccionario[a[0].split(",")[0]]=[a[i].split(",")[0] for i in range(1,len(a))]
diccionario[a[0].split(",")[1]]=[int(a[i].split(",")[1]) for i in range(1,len(a))]
diccionario[a[0].split(",")[2]]=[int(a[i].split(",")[2][0:-1]) for i in range(1,len(a))]
print(diccionario)