# Se solicita la acción a ejecutar, si cifrar o descifrar.
def accion_a_hacer():
    while True:
        try:
            opcion = int(input("\n¿Quieres cifrar(1) o descifrar(2)?\nQuiero: "))
            if opcion == 1 or opcion == 2:
                break

            else:
                print("Ingresó un  valor fuera de los definidos.")
        except:
            print("\nNo ingresó un número.\n")
    return opcion

# Se solicita el número de César.
def numero_cesar():
    while True:
        try:
            cesar = int(input("\nIngrese el número del César, el número debe de estar en el intérvalo 1-26: "))

            if cesar < 1 or cesar > 26:
                print("\nIntrodujo un valor fuera del intérvalo.")
            
            else:
                break

        except:
            print("\nNo ingresó un número")
    return cesar

# Se solicita la cadena a cifrar o descifrar.
def mensaje():
    while True:
        cadena = input(f"\nIngrese la cadena alfabética: ")
        if cadena.isalpha() or " " in cadena:
            break

        else:
            print("\nIngresó carácteres no válidos.")
    return cadena

# Función que cifra.
def cifrar(cesar, mensaje, abecedario):

    cadena_cifrada = ""

    for i in mensaje:
        if i == " ":
            cadena_cifrada += " "

        else:
            posicion = abecedario.index(i.upper())
            posicion_cesar = posicion + cesar

            if posicion_cesar > 26:
                posicion_cesar = posicion_cesar - 27
            
            nueva_letra = abecedario[posicion_cesar]

            if i.isupper():
                cadena_cifrada += nueva_letra 

            elif i.islower():
                cadena_cifrada += nueva_letra.lower()

    return cadena_cifrada

# Función que descifra.
def descifrar(cesar, mensaje, abecedario, ):
    cadena_descifrada = ""
    for i in mensaje:
        if i == " ":
            cadena_descifrada += " " 

        else:
            posicion = abecedario.index(i.upper())
            posicion_cesar = posicion - cesar

            if posicion_cesar < -26:
                posicion_cesar = 26 - cesar
                nueva_letra = abecedario[posicion_cesar]
            
            nueva_letra = abecedario[posicion_cesar]

            if i.isupper():
                cadena_descifrada += nueva_letra 

            elif i.islower():
                cadena_descifrada += nueva_letra.lower()

    return cadena_descifrada


    
# Función que controla y ejecuta las otras funciones.
def main():
    controlador = True
    # Se define el abecedario y los números.
    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    eleccion = accion_a_hacer()
    num_cesar = numero_cesar()
    mensaje_recibido = mensaje()

    if eleccion == 1:
        print(cifrar(num_cesar, mensaje_recibido, abecedario))

    else:
        print(descifrar(num_cesar, mensaje_recibido, abecedario))

main()