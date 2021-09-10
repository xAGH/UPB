import random
#mapa de opciones
#0 = piedra
#1 = papel
#2 = tijera
print("Juguemos Piedra papel o tijera")
opcionPc = random.randint(0,2)
while ():
    try:
        opcionUsuario = input("señor usuario, escoja su opción: a =  piedra, b = papel, c = tijera o s = salir")
    except:
        print("error de captura")

    if (opcionPc==0 and opcionUsuario=='a'):
        print("Empate")
    elif (opcionPc==0 and opcionUsuario=='b'):
        print("Gana Usuario")
    elif (opcionPc==0 and opcionUsuario=='c'):
        print("Gana PC")
    elif (opcionPc==1 and opcionUsuario=='a'):
        print("Gana PC")
    elif (opcionPc==1 and opcionUsuario=='b'):
        print("Empate")
    elif (opcionPc==1 and opcionUsuario=='c'):
        print("Gana Usuario")
    elif (opcionPc==2 and opcionUsuario=='a'):
        print("Gana Usuario")
    elif (opcionPc==2 and opcionUsuario=='b'):
        print("Gana PC")
    else:
        print("Empate")