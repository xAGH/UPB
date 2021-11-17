print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
# Se importra método randint de la librería random
from random import randint
from os import replace, system

# Ingreso y validación  de credenciales.
def credenciales(usuario, contrasena):
    ingreso_usuario = input("Ingresa el nombre de usuario: ").replace(" ","")

    if ingreso_usuario == usuario:
        ingreso_contrasena = input("Ingrese la contraseña: ").replace(" ","")
        
        if ingreso_contrasena == contrasena:
            return 1

    return 0

# Función que define y valida el captcha.
def captcha_generador():
    primera_parte = 633
    operacion1 = 6 % 5 + (3 - 1)
    operacion2 = (5 % 6 - 6 // 6) + (5 * 1 - (1 % 5 * 6))
    operacion3 = (6 % 1 + 1 * 1) + (6 % 5 + 1)
    operaciones = (operacion1, operacion2, operacion3)
    seleccion = randint(0, 2)
    segunda_parte = operaciones[seleccion]
    captcha_validacion = input(f"Indique el resultado de la operación: {primera_parte} + {segunda_parte} = ").replace(" ","")
    solucion = primera_parte + segunda_parte

    # Se valida lo ingresado por el usuario
    try:
        if int(captcha_validacion) == solucion:
            system("cls")
            print("Sesión iniciada")
            return

        else:
            error()

    except:
        error()

# Función que indica un fallo en el proceso.
def error():
    system("cls")
    print("Error")
    print("El acceso no se completó")

# Función que se encarga de manejar las demás funciones.
def main():

    # Se definen las credenciales.
    usuario = "51633"
    contrasena = "33615"
    acceso = credenciales(usuario, contrasena)

    if acceso == 1:
        captcha_generador()

    else:
        error()
main()