# Importación de librerías.
from abc import abstractclassmethod
from os import access, system as sys
from random import randint
from math import atan2, radians, sin, cos, atan, sqrt


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
    try: 
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

    except:
        return "SALIR"
        

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
            cambio_coordenadas(matriz)

        except:
            sys("cls")
            print("Error actualización")
            return "SALIR"        

def cambio_coordenadas(matriz):
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


def ubicar_zona_wifi(matriz, ubicaciones_cercanas):
    """FUNCION QUE UBICA LA ZONA DE WIFI MAS CERCANA SEGUN LA ZONA ACTUAL"""
    if len(matriz) == 0:
        print("Error sin registro de coordenadas.")
    
    else:
        for i in range(len(matriz)):
            print(f"Coordenada [latitud, longitud] #{i+1}: {matriz[i]}")
        try:
            ubicacion = int(input("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión: "))
            if ubicacion  < 1 or ubicacion > 3:
                    sys("cls")
                    print("Error ubicación.")
                    return "SALIR"
                
            else:
                
                if ubicacion == 1:
                    ubicacion_actual = matriz[0]

                elif ubicacion == 2:
                    ubicacion_actual = matriz[1]

                elif ubicacion == 3:
                    ubicacion_actual = matriz[2]
                
                distancias = calculo_distancia(ubicaciones_cercanas, ubicacion_actual)
                mas_cerca = calculo_cercania(distancias)
                sys("cls")
                print("Zonas wifi cercanas con menos usuarios.")
                print(f"La zona wifi 1: ubicada en ['{mas_cerca[0][1][0]}', '{mas_cerca[0][1][1]}'] a {mas_cerca[0][0]} metros, tiene en promedio {mas_cerca[0][1][2]} usuarios.")
                print(f"La zona wifi 2: ubicada en ['{mas_cerca[1][1][0]}', '{mas_cerca[1][1][1]}'] a {mas_cerca[1][0]} metros, tiene en promedio {mas_cerca[1][1][2]} usuarios.")
                indicaciones = int(input("Elija 1 o 2 para recibir indicaciones de llegada: "))
                if indicaciones != 1 and indicaciones != 2:
                    sys("cls")
                    print("Error zona wifi.")
                    return "SALIR"

                indicaciones = indicaciones_llegada(indicaciones, distancias, ubicacion_actual)
                print(f"{indicaciones[0]}\n{indicaciones[1]}")

                salir = int(input("Ingrese 0 para salir: "))

                if salir == 0:
                    sys("cls")
                    return [mas_cerca[0], ubicacion_actual, indicaciones[2]]
                    
                sys("cls")
                print("Error zona wifi.")
                return "SALIR"
        except:
            sys("cls")
            print("Error zona wifi.")
            return "SALIR"

def calculo_distancia(ubicaciones_cercanas, ubicacion_actual):
    """FUNCION QUE CALCULA LA DISTANCIA ENTRE DOS PUNTOS."""
    RADIO_T = 6372.795477598
    lat1 = ubicacion_actual[0]
    lon1 = ubicacion_actual[1]
    resultados = []
    for i in range(len(ubicaciones_cercanas)):
        lat2 = ubicaciones_cercanas[i][0]
        lon2 = ubicaciones_cercanas[i][1]
        lat = lat2 - lat1
        lon = lon2 - lon1
        a = (sin(radians(lat) / 2)**2) + (cos(radians(lat1)) * cos(radians(lat2))) * (sin(radians(lon / 2))**2)
        b = 2 * atan2((sqrt(a)), (sqrt(1-a)))
        c = RADIO_T * b
        distancia = [round(c,3), ubicaciones_cercanas[i]]
        resultados.append(distancia)
    return resultados

def calculo_cercania(distancias):
    for recorrido in range(1, len(distancias)):
        for posicion in range(len(distancias) - recorrido):
            if distancias[posicion][1][2] > distancias[posicion + 1][1][2]:
                temp = distancias[posicion][1][2]
                distancias[posicion][1][2] = distancias[posicion + 1][1][2]
                distancias[posicion + 1][1][2] = temp
    return distancias
        
def indicaciones_llegada(indicaciones, distancias, ubicacion_actual):
    tiempo_promedio_bus = 16.67
    tiempo_promedio_bicicleta = 3.33
    if indicaciones == 1:
        ejeX = "Norte" if ubicacion_actual[0] > distancias[0][1][0] else "Sur"
        ejeY = "Oriente" if ubicacion_actual[1] > distancias[0][1][1] else "Occidente"
        distancia_zona_wifi = distancias[0][0]

    else:
        ejeX = "Norte" if ubicacion_actual[0] > distancias[1][1][0] else "Sur"
        ejeY = "Oriente" if ubicacion_actual[1] > distancias[1][1][1] else "Occidente"
        distancia_zona_wifi = distancias[1][0]

    if ejeX == None and ejeY != None:
        ruta = f"Para llegar a la zona wifi dirigirse al {ejeY}"
    
    elif ejeX != None and ejeY == None:
        ruta = f"Para llegar a la zona wifi dirigirse al {ejeX}"

    else:
        ruta = f"Para llegar a la zona wifi dirigirse al {ejeY} y luego hacia el {ejeX}."

    tiempo_bus = str(round((distancia_zona_wifi / tiempo_promedio_bus) * 60, 2)) + 'min'
    tiempo_bici = str(round((distancia_zona_wifi / tiempo_promedio_bicicleta) * 60, 2)) + 'min'
    tiempo_calculado = f"Se demorará aproximadamente {tiempo_bus} si va en bus o {tiempo_bici} si va en bicicleta."
    sys("cls")
    tiempo_medio = {'bus' : tiempo_bus, 'bici' : tiempo_bici}
    return [ruta, tiempo_calculado, tiempo_medio]


def guardar_archivo(zonas_wifi_cercanas):
    """Funcion que guarda datos en un archivo externo."""
    informacion = {
        'actual' : zonas_wifi_cercanas[1],
        'zonawifi1' : zonas_wifi_cercanas[0][1],
        'recorrido' : [zonas_wifi_cercanas[0][0], zonas_wifi_cercanas[2]]
    }
    sys("cls")
    print(informacion)
    confirmacion =  input("¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal: ")
    if confirmacion == '1':
        return informacion
    
    elif confirmacion == '0':
        return

    else:
        sys("cls")
        print("Error de alistamiento")
        return "SALIR"

def actualizar_registros():
    """Funcion que actualiza los registros de acuerdo a un archivo externo"""
    salir = input("Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal: ")
    if salir == '0':
        return 

    sys("cls")
    print("Error de actualización.")
    return "SALIR"

def datos_globales():
    contrasena_opcion = "Cambiar contraseña."
    coordenadas_opcion = "Ingresar coordenadas actuales."
    wifi_opcion = "Ubicar zona wifi más cercana."
    ubicacion_opcion = "Guardar archivo con ubicación cercana."
    registros_opcion = "Actualizar registros de zonas wifi desde archivo."
    favorita_opcion = "Elegir opción de menú favorita."
    cerrar_opcion = "Cerrar sesion."
    menu = {1:contrasena_opcion, 2:coordenadas_opcion, 3:wifi_opcion, 4:ubicacion_opcion, 5:registros_opcion, 6:favorita_opcion, 7:cerrar_opcion}

    matriz_coordenadas = []
    ubicaciones_cercanas = [
        [6.211,-74.482, 2],
        [6.212, -72.470, 25],
        [6.105, -72.342, 25],
        [6.210, -72.442, 50]
    ]

    return menu, matriz_coordenadas, ubicaciones_cercanas


def main():
    """Funcion principal encargada de ejecutar y relacionar todo el programa"""
    usuario = "51633"
    contrasena = "33615"
    inicio = inicio_sesion(usuario, contrasena)
    if inicio == 1:
        menu, matriz_coordenadas, ubicaciones_cercanas = datos_globales()

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
                    print(f"Usted ha elegido la opción {opcion}")
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
                    print(f"Usted ha elegido la opción {opcion}")
                    nueva_matriz_coordenadas = ingresar_coordenadas(matriz_coordenadas)

                    if nueva_matriz_coordenadas == "SALIR":
                        break
                    
                    elif  nueva_matriz_coordenadas == None:
                        pass

                    else:
                        print("Se han agregado las coordenadas.")
                        matriz_coordenadas = nueva_matriz_coordenadas

                elif seleccion == 3:
                    sys("cls")
                    print(f"Usted ha elegido la opción {opcion}")
                    zonas_wifi_cercanas = ubicar_zona_wifi(matriz_coordenadas, ubicaciones_cercanas)
                    if zonas_wifi_cercanas == "SALIR":
                        break
                    
                    
                elif seleccion == 4:
                    sys("cls")
                    print(f"Usted ha elegido la opción {opcion}")
                    try:
                        if len(matriz_coordenadas) > 1 and zonas_wifi_cercanas:
                            archivo_guardao = guardar_archivo(zonas_wifi_cercanas)
                            if archivo_guardao == "SALIR":
                                sys("cls")
                                print('Error de alistamiento.')
                                break

                            elif archivo_guardao == None:
                                pass

                            else:
                                sys("cls")
                                print("Exportando archivo.")
                                break

                        else:
                            sys("cls")
                            print('Error de alistamiento.')
                            break

                    except:
                        sys("cls")
                        print('Error de alistamiento.')
                        break

                elif seleccion == 5:
                    sys("cls")
                    print(f"Usted ha elegido la opción {opcion}")
                    datos_actualizados = actualizar_registros()
                    if datos_actualizados == None:
                        pass

                    else:
                        break

                elif seleccion == 6:
                    sys("cls")
                    print(f"Usted ha elegido la opción {opcion}")
                    menu = cambiar_favorito(menu)
                    if menu == "SALIR":
                        break

                elif seleccion == 7:
                    sys("cls")
                    print(f"Usted ha elegido la opción {opcion}")
                    print("Hasta pronto")
                    break

if __name__ == '__main__':
    main()