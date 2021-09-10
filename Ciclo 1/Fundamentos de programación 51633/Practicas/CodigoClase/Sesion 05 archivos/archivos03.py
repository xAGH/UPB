#abrindo un archivo que no existse 
# OJO a donde si y donde no debe ir el manejo de funciones

try:
    with open("noexiste.txt","r") as archivo:
        print("abriendo el archivo ",archivo.name)
        print("estado de la bandera closed: ",archivo.closed)
        print("manejador del archivo", archivo)
        contenido = archivo.read()
except:
    print("algo fallo con la lectura del archivo")
print("estado de la bandera closed: ",archivo.closed)