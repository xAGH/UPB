#programa en python que genera canciones urbanas de forma automatica
#ejercicio para practicar estructuas de datos, indexación y ciclos

import random

base = [["Mami, ","Gata, ","Dama, ","Nena, ","Hembra, "],["yo quiero ","vamos a ", "yo voy a ","yo quiero ","yo vengo a "],["castigarte ","cogerte ","encederte ","darte ","azotarte "],["duro ","rapido ","lento ","suave ","fuerte "],["hasta que salga el sol ","toda la noche ","hasta el amanecer ","hasta la mañana ","todo el día "],["sin miedo ","sin anestesia ","contra el piso ","contra la pared ","sin compromiso "]]
n_autor = {"a":"El Nazi","b":"El Nicky","c":"El Bryan","d":"El Daddy","e":"Arcangel","f":"El Don","g":"El Tego","h":"Fido","i":"Tito","j":"El Kevin","k":"Pretty","l":"Boy","m":"El Ñengo","n":"Sexy","o":"Reyna","p":"La Gata","q":"Wisin","r":"La Yare","s":"Anaconda","t":"Queen","u":"Cassandra","v":"Ruby","w":"El Ñero","x":"Selva Negra","y":"Papaya","z":"Romeo"}
n_apellido = {"a":"Enciende","b":"Acapella","c":"Bellaco","d":"Perreante","e":"Reyna","f":"Baby","g":"Rakata","h":"Flow","i":"Mala Mala","j":"Princesa","k":"Rompe Rompe","l":"Fuego","m":"Fiera","n":"Papi","o":"Bomba","p":"Intenso","q":"Fuetazo","r":"Pegao","s":"Sandungueo","t":"Rompe","u":"Mami","v":"Tiraera","w":"Boricua","x":"Rampletera","y":"Trambo","z":"Rasta"}      
autor = {"nombre":n_autor,"apellido":n_apellido}


#capturar de teclado el nombre y apellido del autor que ejecuta el programa
while True:
    try:
        nombre = input("Ingrese su nombre:   ")
        if nombre:
            break
    except:
        print("Algo paso con la captura de su nombre")

while True:
    try:
        apellido = input("Ingrese su apellido:   ")
        if apellido:
            break
    except:
        print("Algo paso con la captura de su apellido")

print("construyendo una cancion Urbana con Python\n")
print("\n")

#crear la estrofa de la cancion
estrofa = ""
for j in range(0,6):
    renglon = ""
    for i in range(0,6):
        renglon = renglon + base[i][random.randint(0,4)]
    print(renglon)

#crear el coro
print("\n CORO:  \n")
a = ""
for j in range(0,3):
    a = a + base[2][random.randint(0,4)]
a = a + base[4][random.randint(0,4)] + base[3][random.randint(0,4)]
for i in range(0,3):
    print(a)
print("\n")

#crear la segunda estrofa
estrofa = ""
for j in range(0,6):
    renglon = ""
    for i in range(0,6):
        renglon = renglon + base[i][random.randint(0,4)]
    print(renglon)

#firmar la cancion
print("\n Autor de la canción: \n")
#imprimir en pantalla
n = autor['nombre'][nombre[0]]
m = autor['apellido'][apellido[0]]
print(n + " "+ m)
