# Debes implementar un programa que sea capaz de adivinar el número que estás pensando.
# El ordenador tendrá 10 intentos para adivinar el número. Este número estará entre 0 y 100.
# El ordenador irá mostrando por pantalla los números y preguntará si el número que estás
# pensando es mayor, menor o si ha acertado. Si el ordenador acierta terminará la partida.
# Si se le terminan los 10 intentos el ordenador mostrará que ha perdido.
limiteinferior = 0
limitesuperior = 100
print("Señor usuario(a), por favor piense un número entre :", limiteinferior)
print("... y el numero: ", limitesuperior)
try: 
    decision = input("Usted ya ha pensado el número? responda S si si o cualquier letra si no:")
    if decision.upper() == 'S':
        print("Gracias por jugar conmigo:")
        intento = 1
        respuestausuario = ''
        banderaresultado = False
        while ((intento <=10) and not(banderaresultado)):
            print("   intento numero: ", str(intento))
            calculado = round((limitesuperior - limiteinferior)/2 + limiteinferior)
            try:
                print("yo creo que el número que ud penso es:    ",calculado)
                respuestausuario = input("este numero es (m)mayor (n)menor o (i)igual?")
                if respuestausuario.lower() == 'm':
                    limitesuperior = calculado
                elif (respuestausuario.lower() == 'n'):
                    limiteinferior = calculado
                elif (respuestausuario.lower() == 'i'):
                    print("he ganado, he adivinado su número")
                    banderaresultado = True
                else:
                    print("ha digitado una opción no valida") 
            except:
                print("error capturando la apreciación del usuario")
            intento = intento + 1
    else:
        print("Gracias por no jugar:.. chao")
except:
    print("error al capturar la decision")