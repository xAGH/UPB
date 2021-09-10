# Importación de librerías.
from os import system as sys
from random import randint

print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
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
            sys("cls")
            print("Sesión iniciada")
            return 1

        else:
            error()

    except:
        error()

# Función que indica un fallo en el proceso.
def error():
    sys("cls")
    print("Error")
    print("El acceso no se completó")


def mostrar_menu(menu):
    """Esta función se encarga de mostrar el menú dado de una forma ordenada."""
    contador = 0
    for i in menu:
        print(f"{i}. {menu[i]}")

    while True:
        if contador >= 3:
            return "SALIR"

        else: 
            try:
                opcion = input("Elija una opción: ").replace(" ","")
                opcion = int(opcion)
                if opcion < 8 and opcion > 0:
                    return opcion

                else:
                    print("Error")
                    contador += 1

            except:
                print("Error")
                contador += 1

def cambiar_favorito(menu):
    """Función que se encarga de cambiar el favorito al seleccionado por el usuario."""
    try:
        nuevo_fav = input("Seleccione opción favorita: ").replace(" ","")

        if nuevo_fav.isdigit():
            nuevo_fav = int(nuevo_fav)
            if nuevo_fav < 6 and nuevo_fav > 0:

                confirmacion = input("Para confirmar por favor responda:\n1. Me separaron de mi hermano siamés, antes era un ocho y ahora soy un: ").replace(" ","")

                if confirmacion == '3':
                    confirmacion2 = input("Para confirmar por favor responda:\n2. Tengo forma de serpiente, y entre el dos y el cuatro siempre estoy cuando me buscas: ").replace(" ","")

                    if confirmacion2 == '3':
                        anterior = menu[1]
                        nuevo = menu[nuevo_fav]
                        menu[1] = nuevo
                        menu [nuevo_fav] = anterior
                        sys("cls")
                        return menu
            
        sys("cls")           
        print("Error")
        return "SALIR"


    except:
        sys("cls")           
        print("Error")
        return "SALIR"


def inicio_sesion():
    usuario = "51633"
    contrasena = "33615"
    acceso = credenciales(usuario, contrasena)

    if acceso == 1:
        validado = captcha_generador()
        if validado == 1:
            return 1

    else:
        error()

def main():
    inicio = inicio_sesion()
    if inicio == 1:
        contrasena = "Cambiar contraseña."
        coordenadas = "Ingresar coordenadas actuales."
        wifi = "Ubicar zona wifi más cercana."
        ubicacion = "Guardar archivo con ubicación cercana."
        registros = "Actualizar registros de zonas wifi desde archivo."
        favorita = "Elegir opción de menú favorita."
        cerrar = "Cerrar sesion."
        menu = {1:contrasena, 2:coordenadas, 3:wifi, 4:ubicacion, 5:registros, 6:favorita, 7:cerrar}

        while True:

            opcion = mostrar_menu(menu)

            try:
                if opcion == "SALIR":
                    break
            except:
                pass
            
            if opcion > 7 and opcion < 0:
                print("Error")

            else:
                if opcion == 1:
                    print("Usted ha elegido la opción 1")
                    break
                
                elif opcion == 2:
                    print("Usted ha elegido la opción 2")
                    break

                elif opcion == 3:
                    print("Usted ha elegido la opción 3")
                    break

                elif opcion == 4:
                    print("Usted ha elegido la opción 4")
                    break

                elif opcion == 5:
                    print("Usted ha elegido la opción 5")
                    break

                elif opcion == 6:
                    print("Usted ha elegido la opción 6")
                    menu = cambiar_favorito(menu)
                    if menu == "SALIR":
                        break

                elif opcion == 7:
                    sys("cls")
                    print("Hasta pronto")
                    break
    else:
        print("Error")
        print("El acceso no se completó")

if __name__ == '__main__':
    main()