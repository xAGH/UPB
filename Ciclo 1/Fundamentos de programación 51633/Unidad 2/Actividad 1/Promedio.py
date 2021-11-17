while True:
    try:
        numero1 = float(input('Ingrese el número 1: '))[0:3]
        numero2 = float(input('Ingrese el número 2: '))[0:3]
        numero3 = float(input('Ingrese el número 3: '))[0:3]
        numero4 = float(input('Ingrese el número 4: '))[0:3]
        numero5 = float(input('Ingrese el número 5: '))[0:3]

        suma = numero1 + numero2 + numero3 + numero4 + numero5
        promedio = suma / 5

        print(F"EL promedio es {promedio}")

    except:
        print("\nSolo se permiten números.\n")