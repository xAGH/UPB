from os import system as sys

def solicitud_numeros():
    """Funcion que recibe numeros de teclado y los agrega a una lista que sera agregada a una matriz"""
    matriz = []
    while True:
        lista = []
        sys("cls")
        decision = input("¿Desea agregar una lista a la matriz?\n1. SI.\n2. NO.\nOpción: ")
        if decision == '1':
            while True:
                numero = input("Ingrese un número entero (Enter para salir): ")
                if numero.isdigit():
                    lista.append(int(numero))

                elif numero == "":
                    matriz.append(lista)
                    break

        elif decision == '2':
            break

        else: 
            print("Entra incorrecta")
    
    return matriz

            
def imprimir_nums(matriz):
    """Funcion que imprime los elementos de una lista"""
    sys("cls")
    for i in range(len(matriz)):
        print(matriz[i])

def main():
    """Funcion principal encargadad de manejar el programa"""
    matriz = solicitud_numeros()
    imprimir_nums(matriz)

if __name__ == '__main__':
    main()