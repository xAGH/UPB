while True:
    try:
        numero1 = float(input('Ingrese el número 1: '))
        numero2 = float(input('Ingrese el número 2: '))

        suma = numero1 + numero2
        resta = numero1 - numero2
        multiplicacion = numero1 * numero2
        division = (numero1 / numero2) if numero2 != 0 else "Error, no se puede dividir por 0."
        potencia1 = numero1 * numero1
        potencia2 = numero2 * numero2

        print(f"""
        Suma --> {numero1} + {numero2} = {suma}
        Resta --> {numero1} - {numero2} = {resta}
        Multiplicación --> {numero1} * {numero2} = {multiplicacion}
        División --> {numero1} / {numero2} = {division}
        Potencia al cuadrado --> {numero1}\u00b2 = {potencia1}
        Potencia al cuadrado --> {numero2}\u00b2 = {potencia2}""")
        break

    except:
        print("\nIngrese un número. (Si el número tiene decimales, decláralas con un . en vez de con una ,)\n")