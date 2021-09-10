while True:
    try:
        hora = int(input("Ingrese una hora: "))

        if hora > 0 and hora < 12:
            caso = 1
        
        elif hora >= 12 and hora < 19:
            caso = 2

        elif hora >= 19 and hora <= 23:
            caso = 3

        break

    except:
        print("Ingrese un número entre 0 y 23")

if caso == 1:
    print("Buenos días.")

elif caso == 2:
    print("Buenas tardes.")

elif caso == 3:
    print("Buenas noches.")

else:
    print("Hubo un problema")