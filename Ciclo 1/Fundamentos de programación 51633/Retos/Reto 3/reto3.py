# Importación de librerías.
from os import system as sys
from random import randint
from typing import DefaultDict

print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
# Ingreso y validación  de credenciales.
def credenciales(usuario, contrasena):
    """Funcion que valida el usuario y contrasena"""
    ingreso_usuario = input("Ingresa el nombre de usuario: ").replace(" ","")

    if ingreso_usuario == usuario:
        ingreso_contrasena = input("Ingrese la contraseña: ").replace(" ","")
        
        if ingreso_contrasena == contrasena:
            return 1

    return 0

# Función que define y valida el captcha.
def captcha_generador():
    """Funcion que define y valida el captcha."""
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
    """Funcion que muestra un mensaje de error"""
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


def inicio_sesion(usuario, contrasena):
    """Funcion que se encarga de iniciar sesion y redirigir al captcha"""
    acceso = credenciales(usuario, contrasena)

    if acceso == 1:
        validado = captcha_generador()
        if validado == 1:
            return 1

    else:
        error()

def hallar_llave(menu, llave):
    """Esta funcion busca la llave de un valor pasado por parametros."""
    seleccion = menu[llave]
    if seleccion == "Cambiar contraseña.":
        return 1

    elif seleccion == "Ingresar coordenadas actuales.":
        return 2

    elif seleccion == "Ubicar zona wifi más cercana.":
        return 3

    elif seleccion == "Guardar archivo con ubicación cercana.":
        return 4
    
    elif seleccion == "Actualizar registros de zonas wifi desde archivo.":
        return 5

    return llave

def cambio_contrasena(contrasena):
    """Esta funcion cambia la contraseña."""
    contrasena_confirmacion = input("Ingrese la contraseña actual: ")

    if contrasena_confirmacion == contrasena:
        nueva_contrasena = input("Ingresa la nueva contraseña: ")

        if nueva_contrasena == contrasena:
            sys("cls")
            print("Las contraseñas no pueden ser iguales.")
            return

        else:    
            contrasena = nueva_contrasena
            return contrasena

    else:
        print("Error")
        return True
            
def ingresar_coordenadas(matriz):
    """Esta funcion guarda las coordenadas ingresadas."""
    if len(matriz) == 0:
        try:
            for i in range(3):
                latitud = float(input("Ingresa la latitud: "))
                longitud =  float(input("Ingresa la longitud: "))
                if latitud > 6.306 or latitud < 5.888 and longitud > -72.321 or latitud < -72.552:
                    print("Error coordenada")
                    return "SALIR"

                coordenada = [latitud, longitud]
                matriz.append(coordenada)
            return matriz
        except:
            print("Error coordenada")
            return "SALIR"

    else:
        norte_calculo = 419
        suma_lat = 0
        suma_lon = 0
        for i in range(len(matriz)):
            print(f"Coordenada [latitud, longitud] #{i+1}: {matriz[i]}")
            calculo = 6.306 - matriz[i][0]
            if calculo < norte_calculo:
                norte_calculo = calculo
                norte = matriz.index(matriz[i])

            suma_lat += matriz[i][0]
            suma_lon += matriz[i][1]
        
        promedio_lat = (suma_lat / 3)
        promedio_lon = suma_lon / 3
        coordenada_promedio = [round(promedio_lat, 3), round(promedio_lon, 3)]
        print(f"La cordenada {norte+1} es la que está más al norte.\nLas coordenadas promedio son [latitud, longitud]: {coordenada_promedio}.")
        try:
            cambio = int(input("Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú: "))

            if cambio < 0 or cambio > 3:
                sys("cls")
                print("Error actualización")
                return "SALIR"
            
            else:
                if cambio == 0:
                    sys("cls")
                    return 
                
                elif cambio == 1:
                    aCambio = matriz[0]

                elif cambio == 2:
                    aCambio = matriz[1]

                elif cambio == 3:
                    aCambio = matriz[2]

                sys("cls")
                print(f"Seleccionó la coordenada número {cambio}")
                latitud = float(input("Ingresa la latitud: "))
                longitud =  float(input("Ingresa la longitud: "))
                if latitud > 6.306 or latitud < 5.888 or longitud > -72.321 or latitud < -72.552:
                    print("Error actualización")
                    return "SALIR"
                coordenada = [latitud, longitud]

                for x in range(len(matriz)):
                    if matriz[x] == aCambio:
                        matriz[x] = coordenada
                        return matriz

        except:
            sys("cls")
            print("Error actualización")
            return "SALIR"        

def main():
    """Funcion principal envargada de ejecutar y relacionar todo el programa"""
    usuario = "51633"
    contrasena = "33615"
    inicio = inicio_sesion(usuario, contrasena)
    if inicio == 1:
        contrasena_opcion = "Cambiar contraseña."
        coordenadas_opcion = "Ingresar coordenadas actuales."
        wifi_opcion = "Ubicar zona wifi más cercana."
        ubicacion_opcion = "Guardar archivo con ubicación cercana."
        registros_opcion = "Actualizar registros de zonas wifi desde archivo."
        favorita_opcion = "Elegir opción de menú favorita."
        cerrar_opcion = "Cerrar sesion."
        menu = {1:contrasena_opcion, 2:coordenadas_opcion, 3:wifi_opcion, 4:ubicacion_opcion, 5:registros_opcion, 6:favorita_opcion, 7:cerrar_opcion}

        matriz_coordenadas = []

        while True:
            opcion = mostrar_menu(menu)
            seleccion = hallar_llave(menu, opcion)

            try:
                if seleccion == "SALIR":
                    break
            except:
                pass
            
            if seleccion > 7 and seleccion < 0:
                print("Error")

            else:
                if seleccion == 1:
                    sys("cls")
                    print("Usted ha elegido la opción 1")
                    contrasena_cambiada = cambio_contrasena(contrasena)
                    if contrasena_cambiada == None:
                        pass

                    elif contrasena_cambiada == True:
                        break

                    else:
                        contrasena = contrasena_cambiada
                        sys("cls")
                        print("Se ha cambiado la contraseña.")

                elif seleccion == 2:
                    sys("cls")
                    print("Usted ha elegido la opción 2")
                    nueva_matriz_coordenadas = ingresar_coordenadas(matriz_coordenadas)

                    if nueva_matriz_coordenadas == "SALIR":
                        break
                    
                    elif  nueva_matriz_coordenadas == None:
                        pass

                    else:
                        sys("cls")
                        print("Se han agregado las coordenadas.")
                        matriz_coordenadas = nueva_matriz_coordenadas

                elif seleccion == 3:
                    sys("cls")
                    print("Usted ha elegido la opción 3")
                    break

                elif seleccion == 4:
                    sys("cls")
                    print("Usted ha elegido la opción 4")
                    break

                elif seleccion == 5:
                    sys("cls")
                    print("Usted ha elegido la opción 5")
                    break

                elif seleccion == 6:
                    sys("cls")
                    print("Usted ha elegido la opción 6")
                    menu = cambiar_favorito(menu)
                    if menu == "SALIR":
                        break

                elif seleccion == 7:
                    sys("cls")
                    print("Hasta pronto")
                    break

if __name__ == '__main__':
    main()