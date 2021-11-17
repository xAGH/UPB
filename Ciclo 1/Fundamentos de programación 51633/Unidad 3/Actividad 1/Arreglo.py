from os import system as sys

def solicitud_numeros():
    """Funcion que recibe numeros de teclado y los agrega a una lista"""
    lista = []
    while True:
        numero = input("Ingrese un número entero (Enter para salir): ")
        if numero.isdigit():
            lista.append(int(numero))

        elif numero == "":
            return lista
            
def imprimir_nums(lista):
    """Funcion que imprime los elementos de una lista"""
    sys("cls")
    for i in reversed(lista):
        print(i)

def main():
    """Funcion principal encargadad de manejar el programa"""
    nums = solicitud_numeros()
    imprimir_nums(nums)

if __name__ == '__main__':
    main()