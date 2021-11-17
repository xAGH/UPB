from os import system
from math import log, cos, radians, sin, sqrt

def bienvenida():
    """Función que da la bienvenida a la calculadora"""
    print( """            
  ____  _                           _     _                       _        
 |  _ \(_)                         (_)   | |  ____               | |       
 | |_) |_  ___ _ ____   _____ _ __  _  __| | / __ \      __ _    | | __ _  
 |  _ <| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ / _` |    / _` |   | |/ _` | 
 | |_) | |  __/ | | \ V /  __/ | | | | (_| | | (_| |   | (_| |   | | (_| | 
 |____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\ \__,_|    \__,_|   |_|\__,_| 
           | |          | |         | |      \____/                        
   ___ __ _| | ___ _   _| | __ _  __| | ___  _ __ __ _                     
  / __/ _` | |/ __| | | | |/ _` |/ _` |/ _ \| '__/ _` |                    
 | (_| (_| | | (__| |_| | | (_| | (_| | (_) | | | (_| |                    
  \___\__,_|_|\___|\__,_|_|\__,_|\__,_|\___/|_|  \__,_|                    
                                                                                                                   
    """)

def sys():
    """Función que limpia la consola."""
    system("cls")


def datos():
    """Esta función pide la operación a realizar"""
    while True:
        try:
            operacion = int(input("Operación a realizar.\n1. Suma.\n2. Resta.\n3. Multiplicación.\n4. Logaritmo.\n5. Coseno.\n6. Seno.\n7. Raíz cuadrada.\n8. Decimal a binario.\n9. Binario a decimal.\n10. Salir.\nElije una opción: "))
            if operacion < 11 and operacion > 0:
                return operacion
            
            else:
                sys()
                print("Ingrese un número del 1 al 9 de acuerdo a la operación que desea realizar.")
        
        except:
            print("Ingrese un número del 1 al 9 de acuerdo a la operación que desea realizar.")

def suma_operacion():
    """Esta función hace una suma."""
    while True:
        try: 
            sumando1 = float(input("Ingrese el sumando #1: "))
            sumando2 = float(input("Ingrese el sumando #2: ")) 
            break
        
        except:
            sys()
            print("Ingrese un número. (Si el número tiene decimales, decláralas con un . en vez de con una ,)\n")

    suma = sumando1 + sumando2
    mensaje = f"Suma --> {sumando1} + {sumando2} = {suma}"

    return mensaje

def resta_operacion():
    """Esta función hace una resta con dos datos entregados como parámetros."""
    while True:
        try: 
            minuendo = float(input("Ingrese el minuendo(valor total): "))
            sustraendo = float(input("Ingrese el sustranedo(valor que se restará al minuendo): ")) 
            break
        
        except:
            sys()
            print("Ingrese un número. (Si el número tiene decimales, decláralas con un . en vez de con una ,)\n")

    resta = minuendo - sustraendo
    mensaje = f"Resta --> {minuendo} - {sustraendo} = {resta}"

    return mensaje

def multiplicacion_operacion():
    """Esta función hace una multiplicación con dos datos entregados como parámetros."""
    while True:
        try: 
            multiplicando = float(input("Ingrese el multiplicando: "))
            multiplicador = float(input("Ingrese el multiplicador: ")) 
            break
        
        except:
            sys()
            print("Ingrese un número. (Si el número tiene decimales, decláralas con un . en vez de con una ,)\n")
    
    multiplicacion = multiplicando * multiplicador
    mensaje = f"Multiplicación --> {multiplicando} * {multiplicador} = {multiplicacion}"

    return mensaje

def logaritmo_operacion():
    """Esta función calcula el logaritmo de un número y su posible base."""
    base = None
    while True:
        try: 
            numero = float(input("Ingrese el número: "))
            break
        
        except:
            sys()
            print("Ingrese un número. (Si el número tiene decimales, decláralas con un . en vez de con una ,)\n")
    try:
        base = int(input("Ingrese la base(si no desea definir una base, ingrese cualquier caracter menos un número): "))
    
    except:
        pass

    if base == None:
        logaritmo = log(numero)
        mensaje = f"Logaritmo --> log({numero})  = {logaritmo}"

    else:
        logaritmo = log(numero, base)
        mensaje = f"Logaritmo(numero, base) --> log({numero},{base})  = {logaritmo}"

    return mensaje

def coseno_operacion():
    """Esta función calcula el coseno."""
    while True:
        try:
            grados = float(input("Ingrese los grados: "))
            if grados < -361 or grados > 361:
                sys()
                print("Los grados deben de estar en el rango -360°, 360°")

            else:
                break

        except:
            sys()
            print("Los grados deben de estar en el rango -360°, 360°")

    coseno = cos(radians(grados))

    mensaje = f"Coseno(numero) --> cos({grados})  = {coseno}"

    return mensaje

def seno_operacion():
    """Esta función calcula el seno."""
    while True:
        try:
            grados = float(input("Ingrese los grados: "))
            if grados < -361 or grados > 361:
                sys()
                print("Los grados deben de estar en el rango -360°, 360°")

            else:
                break

        except:
            sys()
            print("Los grados deben de estar en el rango -360°, 360°")

    seno = sin(radians(grados))

    mensaje = f"Seno --> sen({grados})  = {seno}"

    return mensaje

def raiz_cuadrada_operacion():
    """Esta función calcula la raíz cuadrada."""
    while True:
        try:
            numero = float(input("Ingrese el número: "))
            break

        except:
            sys()
            print("Ingrese un número. (Si el número tiene decimales, decláralas con un . en vez de con una ,)\n")

    raiz_cuadrada = sqrt(numero)

    mensaje = f"Raíz cuadrada --> √({numero}=)  = {raiz_cuadrada}"

    return mensaje

def decimal_binario_operacion():
    """Esta función convierte un número decimal a binario."""
    while True:
        try:
            numero = int(input("Ingrese el número: "))
            break

        except:
            sys()
            print("Ingrese un número entero.")

    decimal_binario = int(bin(numero)[2:])

    mensaje = f"Decimal a binario --> {numero} en binario = {decimal_binario}"

    return mensaje

def binario_decimal_operacion():
    """Esta función convierte un número binario a decimal."""
    contador = 0 
    while True:
        try:
            numero = input("Ingrese el número: ")
            for i in range(len(numero)):

                if int(numero[i]) > 1 or int(numero[i]) < 0:
                    contador += 1

            if contador == 0:
                break

            else:
                sys()
                print("Solo se admiten 0 y 1")

        except:
            sys()
            print("Solo se admiten 0 y 1")

    binario_decimal = int(numero, 2)

    mensaje = f"Binario a decimal --> {numero} en decimal = {binario_decimal}"

    return mensaje

def mostrar_operacion(palabra):
    """FUnción que organiza espacios para imprimir un mensaje en pantalla"""

    mostrar = f'||     Mostrando {palabra}     ||'
    caracteres = len(mostrar)
    guiones = "-" * caracteres
    print(f"{guiones}\n{mostrar}\n{guiones}\n")

def main():
    while True:
        bienvenida()
        operacion = datos()

        if operacion == 10:
            sys()
            break

        else:

            if operacion == 1:
                sys()
                mostrar_operacion('Suma')
                mensaje = suma_operacion()

            elif operacion == 2:
                sys()
                mostrar_operacion('Resta')
                mensaje = resta_operacion()

            elif operacion == 3:
                sys()
                mostrar_operacion('Multiplicación')
                mensaje = multiplicacion_operacion()

            elif operacion == 4:
                sys()
                mostrar_operacion('Logaritmo')
                mensaje = logaritmo_operacion()

            elif operacion == 5:
                sys()
                mostrar_operacion('Coseno')
                mensaje = coseno_operacion()

            elif operacion == 6:
                sys()
                mostrar_operacion('Seno')
                mensaje = seno_operacion()

            elif operacion == 7:
                sys()
                mostrar_operacion('Raíz cuadrada')
                mensaje = raiz_cuadrada_operacion()

            elif operacion == 8:
                sys()
                mostrar_operacion('Decimal a binario')
                mensaje = decimal_binario_operacion()

            elif operacion == 9:
                sys()
                mostrar_operacion('Binario a decimal')
                mensaje = binario_decimal_operacion()

            print(f"\n\n{mensaje}\n\n")

if __name__ == '__main__':
    main()