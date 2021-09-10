from os import system as sys

def solicitud_numeros():
    """Funcion que recibe numeros de teclado y los agrega a una lista que sera agregada a una matriz"""
    matrices = []
    for i in range(1, 3):
        matriz = []
        sys("cls")
        print(f"Matriz #{i}")
        while True:
            lista = []
            decision = input("¿Desea agregar una lista a la matriz?\n1. SI.\n2. NO.\nOpción: ")
            if decision == '1':
                while True:
                    numero = input("Ingrese un número entero (Enter para salir): ")
                    if numero.isdigit():
                        lista.append(int(numero))

                    elif numero == "":
                        matriz.append(lista)
                        print(matriz, lista)
                        break

            elif decision == '2':
                matrices.append(matriz)
                break

            else: 
                print("Entrada incorrecta")
    return matrices
      
            
def imprimir_nums(matrices):
    """Funcion que opera los elementos de 2 matrices."""
    sys("cls")
    resultados = []
    sumados = suma_matrices(matrices)
    restados = resta_matrices(matrices)
    multiplicados = multiplicacion_matrices(matrices)
    
    resultados.append({"Suma":sumados})
    resultados.append({"Resta":restados})
    resultados.append({"Multipliccion":multiplicados})

    return resultados

def suma_matrices(matrices):
    sumados = []
    for w in range(1):
        for e in range(len(matrices[w])):
            for r in range(len(matrices[w][e])):
                suma = matrices[0][e][r] + matrices[1][e][r]
                sumados.append(suma)
    return sumados

def resta_matrices(matrices):
    restados = []
    for w in range(1):
        for e in range(len(matrices[w])):
            for r in range(len(matrices[w][e])):
                resta = matrices[0][e][r] - matrices[1][e][r]
                restados.append(resta)
    return restados

def multiplicacion_matrices(matrices):
    multiplicados = []
    for w in range(1):
        for e in range(len(matrices[w])):
            for r in range(len(matrices[w][e])):
                multiplicacion = matrices[0][e][r] * matrices[1][e][r]
                multiplicados.append(multiplicacion)
    return multiplicados

def leer_matriz(matrices):
    """Funcion que lee matrices"""
    for i in range(len(matrices)):
        print(matrices[i])

def main():
    """Funcion principal encargadad de manejar el programa"""
    matriz = solicitud_numeros()
    resultados = imprimir_nums(matriz)
    print("Operaciones con las matrices: ")
    for i in range(len(matriz)):
        print(matriz[i])
    
    for i in range(len(resultados)):
        for j in resultados[i].keys():
            print(f"{j}: {resultados[i][j]}")
            
    
       

if __name__ == '__main__':
    main()

    