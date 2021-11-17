# Ciclo infinito controlado hasta que se ingrese una hora válida.
while True:
    try:
        # Pedimos la hora y la intentamos convertir a un entero. Si no se puede, imprime "Ingresa una hora válida."
        hora = int(input("Ingrese una hora: "))

        # Verificamos que hora fue ingresada y asimismo se agrega un valor a la variable caso. 
        if hora > 0 and hora < 12:
            caso = 3

        else:
            if hora >= 19 and hora <= 23:
                caso = 2
        
            elif hora >= 12 and hora < 19:
                caso = 1
        
        break       
        
    except:
        print("Ingresa una hora válida.")

# Se identifica el caso y asimismo, se procede a imprimir un resultado.
if caso == 2:
    print("Buenas noches.")

else:
    if caso == 1:
        print("Buenas tardes.")

    else: 
        if caso == 3:
            print("Buenos días.")

        else:
            print("Valor por defecto, salió algo mal.")