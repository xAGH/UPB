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

def datos():
    """Esta función pide los números con los que se operarán y la operación a realizar"""
    while True:
        try:
            operacion = int(input("Operación a realizar.\n1. Suma.\n2. Resta.\n3. Multiplicación.\n4. División.\n5. Potencia.\nElije una opción: "))
            numero1 = float(input('Ingrese el número 1: '))
            numero2 = float(input('Ingrese el número 2: '))
            return operacion, numero1, numero2
        
        except:
            print("\nIngrese un número. (Si el número tiene decimales, decláralas con un . en vez de con una ,)\n")

def suma(numero1, numero2):
    """Esta función hace una suma con dos datos entregados como parámetros."""
    suma = numero1 + numero2
    mensaje = f"Suma --> {numero1} + {numero2} = {suma}"
    return mensaje

def resta(numero1, numero2):
    """Esta función hace una resta con dos datos entregados como parámetros."""
    resta = numero1 - numero2
    mensaje = f"Resta --> {numero1} - {numero2} = {resta}"
    return mensaje

def multiplicacion(numero1, numero2):
    """Esta función hace una multiplicación con dos datos entregados como parámetros."""
    multiplicacion = numero1 * numero2
    mensaje = f"Multiplicación --> {numero1} * {numero2} = {multiplicacion}"
    return mensaje

def division(numero1, numero2):
    """Esta función hace una división con dos datos entregados como parámetros."""
    division = numero1 / numero2
    mensaje = f"División --> {numero1} / {numero2} = {division}"
    return mensaje

def potencia(numero1, numero2):
    """Esta función hace una potenciación con dos datos entregados como parámetros."""
    potencia1 = numero1 * numero1
    potencia2 = numero2 * numero2
    mensaje = f"Potencia al cuadrado (número 1) --> {numero1}\u00b2 = {potencia1}\nPotencia al cuadrado (número 2) --> {numero2}\u00b2 = {potencia2}"
    return mensaje

def main():
    bienvenida()
    operacion, numero1, numero2 = datos()

    if operacion == 1:
        print("----------------------------\n||     Mostrando Suma     ||\n----------------------------")
        mensaje = suma()

    elif operacion == 2:
        print("-----------------------------\n||     Mostrando Resta     ||\n-----------------------------")
        mensaje = resta()

    elif operacion == 3:
        print("--------------------------------------\n||     Mostrando Multiplicación     ||\n--------------------------------------")
        mensaje = multiplicacion()


if __name__ == '__main__':
    main()