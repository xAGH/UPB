while True:
    try:
        hora = int(input("Ingrese una hora: "))

        if hora > 0 and hora < 12:
            print("Buenos días.")
        
        elif hora >= 12 and hora < 19:
            print("Buenas tardes.")

        elif hora >= 19 and hora <= 23:
            print("Buenas noches.")

        break

    except:
        print("Ingrese un número entre 0 y 23")