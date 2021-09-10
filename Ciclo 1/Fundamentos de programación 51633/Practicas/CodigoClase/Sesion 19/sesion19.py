#solucion A
variablememoriausaurio = "51633"
varaiblememoriaclave = "33615"
print("Bienvenido al progra")
try:
    usuario=input("Entre el nombre del usuario: ")
except:
    print("Error de entrada de usuario")
if usuario == variablememoriausaurio:
    print("usaurio correcto")
    try: 
        contra = input("ingrese la contraseña")
    except:
        print("error captura contraseña")
    if contra == varaiblememoriaclave:
        print("acceso exitoso")
        print("resolver la parte del captcha")
        print("SEcuencia del menu principal del reto 2")
    else:
        print("Error")
else:
    print("usuario incorrecto")

#solucion B
variablememoriausaurio2 = "51633"
varaiblememoriaclave2 = "33615"
print("Bienvenido al progra")
estado_actual = "inicio"
estado_siguiente = ""

while estado_actual != "salir":
    if estado_actual=="inicio":
        print("ingrese el datos del nombre del usuario")
        try:
            usuario2 =input(" ")
        except:
            print("error de captura de usuario")
        if usuario2 == variablememoriausaurio2:
            estado_siguiente = "ingresarpswd"
        else:
            estado_siguiente = "error"
    elif estado_actual =="error":
        print("Error")
    elif estado_actual == "ingresarpswd":
        print("ingrese el password")
        try:
            psw = input(" ")
        except:
            print("error de captura en el pws")
        if psw == varaiblememoriaclave2:
            print("ingreso exitoso")
            estado_siguiente = "menuprincipal"
        else:
            estado_siguiente = "error"
    elif estado_actual = "menuprincipal":
        print("1. menu 1")
        print("2. menu 2")
        print("3. menu 3")
        print("4. menu 4")
        try:
            opcion = input("escoja la opcion: ")
        except:
            print("error de captura")
    elif estado_actual == "salir":
        estado_siguiente = "salir"
    estado_actual=estado_siguiente
print("fin de programa")