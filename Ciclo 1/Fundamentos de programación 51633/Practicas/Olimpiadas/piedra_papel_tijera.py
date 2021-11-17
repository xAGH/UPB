from random import choice

def opciones():
    while True:
        try:
            entrada = int(input("\n¿Qué eliges?\n1. Piedra.\n2. Papel.\n3. Tijera.\nOpción: "))

            if entrada == 1:
                opcion_jugador = "Piedra"
                print("\nIngresaste Piedra")
                return opcion_jugador
                break

            elif entrada == 2:
                opcion_jugador = "Papel"
                print("\nIngresaste Papel")
                return opcion_jugador
                break

            elif entrada == 3:
                opcion_jugador = "Tijera"
                print("\nIngresaste Tijera")
                return opcion_jugador
                break

            else:
                print("\nHas seleccionado una opción no disponible.")

        except:
            print("\nSolo se permiten números.")

def jugar(opcion_jugador):
    opcion_pc = choice(["Piedra", "Papel", "Tijera"])
    print(f"Mi elección fue {opcion_pc}, entonces...",end=" ")

    if opcion_pc == opcion_jugador:
        return "HEMOS QUEDADO EMPATE"
    elif  opcion_pc == "Piedra" and opcion_jugador == 'Tijera':
        return "HE GANADO"
    elif opcion_pc == "Tijera" and opcion_jugador == 'Piedra':
        return "HAS GANADO"
    elif opcion_pc == "Papel" and opcion_jugador == 'Piedra':
        return "HE GANADO"
    elif opcion_pc == "Piedra" and opcion_jugador == 'Papel':
        return "HAS GANADO"
    elif opcion_pc == "Tijera" and opcion_jugador == 'Papel':
        return "HE GANADO"
    elif opcion_pc == "Papel" and opcion_jugador == 'Tijera':
        return "HAS GANADO"

def main():
    i = 1
    while i == 1:
        opcion_jugador = opciones()
        resultado = jugar(opcion_jugador)
        if resultado == None:
            pass
        else:
            print(resultado)
        
        seguir = input("\nIngresa 1 para seguir jugando conmigo, sino, ingresa otro número: ")
        try:
            int(seguir)
        except:
            print("\nNo ingesaste un número, sigamos jugando.\n")

main()