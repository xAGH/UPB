while True:
    try:
        entero = int(input("Ingrese un número entero: "))
        flotante = float(input("Ingrese un flotante: "))
        booleano = bool(input("Ingrese un valor booleano(True/Flase): "))
        char = input("Ingrese un caracter: ")[0:1]
        cadena = input("Ingrese una cadena: ")

        print(f"Entero = {entero}.\nFlotante = {flotante}.\nBooleano = {booleano}.\nChar = {char}.\nCadena = {cadena}.")

        break

    except:
        print("\nIngresa valores válidos.\n")