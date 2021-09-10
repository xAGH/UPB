#importar librerias

#definir funciones
def menuprincipal(m):
    print("-"*50)
    for elemento in m:
        print(elemento)
    print("-"*50)
def menutransacciones():
    print("-"*50)
    print("1. Transferir")
    print("2. Pagar tarjetas")
    print("3. regresar al menu anterior")
    print("-"*50)
#funcion principal
def principal():
    opcion = ''
    detonadortiempo = 0
    estado = ''
    estado_futuro = ''
    menu = ['1 : Transacciones','2 : Quejas','3 : Crear Servicios','4 : Salir']
    print("Bienvenido a la sucursal terminal del Banco Pepito:")
    maximo = 10
    while (opcion != '4') or (detonadortiempo == maximo):
        menuprincipal(menu)
        try:
            opcion = input("introduzca su opción:   ")
        except:
            print("Error de captura de la información")
        estado = opcion
#        if estado == '':
#            sentencias
#            condicion de siguiente estado
        if estado == '1':
            print("el usuario ingreso al menu de trasacciones: ")
            menutransacciones()
            try:
                opciontr = input("introduzca la opción de transacciones: ")
            except:
                print("Error en la captura de transacciones")
            if opciontr == '1':
                #sentencias asociadas a transferencias
                print("menu opcion transferencias")
            elif opciontr == '2':
                print("menu pagar tarjetas")
                estado_futuro = '0'
            elif opciontr == '3':
                estado_futuro = '0'
            else:
                print("error de navegacion en el menu de transacciones")
        elif estado == '2':
            print("el usuario ingreso al menu de quejas")
        elif estado == '3':
            print("el usuario ingreso al menu de crear servicios")
        elif estado == '4':
            print("El usuario dio la opción de salir")
        else:
            print("estado no reconocido")
        estado = estado_futuro
        
    print("Sesión cerrada por el usuario")
#lanzador
if __name__ == '__main__':
    principal()
