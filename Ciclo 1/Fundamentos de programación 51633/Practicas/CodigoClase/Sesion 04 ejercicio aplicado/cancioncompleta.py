base = [["Mami, ","Gata, ","Dama, ","Nena, ","Hembra, "],["yo quiero ","vamos a ", "yo voy a ","yo quiero ","yo vengo a "],["castigarte ","cogerte ","encederte ","darte ","azotarte "],["duro ","rapido ","lento ","suave ","fuerte "],["hasta que salga el sol ","toda la noche ","hasta el amanecer ","hasta la mañana ","todo el día "],["sin miedo ","sin anestesia ","contra el piso ","contra la pared ","sin compromiso "]]
n_autor = {"a":"El Nazi","b":"El Nicky","c":"El Bryan","d":"El Daddy","e":"Arcangel","f":"El Don","g":"El Tego","h":"Fido","i":"Tito","j":"El Kevin","k":"Pretty","l":"Boy","m":"El Ñengo","n":"Sexy","o":"Reyna","p":"La Gata","q":"Wisin","r":"La Yare","s":"Anaconda","t":"Queen","u":"Cassandra","v":"Ruby","w":"El Ñero","x":"Selva Negra","y":"Papaya","z":"Romeo"}
n_apellido = {"a":"Enciende","b":"Acapella","c":"Bellaco","d":"Perreante","e":"Reyna","f":"Baby","g":"Rakata","h":"Flow","i":"Mala Mala","j":"Princesa","k":"Rompe Rompe","l":"Fuego","m":"Fiera","n":"Papi","o":"Bomba","p":"Intenso","q":"Fuetazo","r":"Pegao","s":"Sandungueo","t":"Rompe","u":"Mami","v":"Tiraera","w":"Boricua","x":"Rampletera","y":"Trambo","z":"Rasta"}      
autor = {"nombre":n_autor,"apellido":n_apellido}

print("construyendo una cancion Urbana con Python\n")

while True:
    try:
        nombre = input("digite su nombre:    ")
        if nombre:
            break
    except:
        print("algo paso mal con la captura del nombre")
while True:
    try:
        apellido = input("digite su apellido:    ")
        if apellido:
            break
    except:
        print("algo paso mal con la captura del apellido")


import random
print("letra de la cancion: \n")
estrofa = ""
for j in range(0,6):
    renglon = ""
    for i in range(0,6):
        renglon = renglon + base[i][random.randint(0,4)]
    print(renglon)

print("\nCORO: \n")
a = ""
for j in range(0,3):
    a = a + base[2][random.randint(0,4)]    
a = a + base[4][random.randint(0,4)]+base[3][random.randint(0,4)]
for i in range(0,2):
    print(a)
print("\n")
estrofa = ""
for j in range(0,6):
    renglon = ""
    for i in range(0,6):
        renglon = renglon + base[i][random.randint(0,4)]
    #estrofa = estrofa + renglon + "\n"
    print(renglon)
print("\n Autor:\n")
n = autor['nombre'][nombre[0].lower()]
m = autor['apellido'][apellido[0].lower()]
print(n+" "+m)