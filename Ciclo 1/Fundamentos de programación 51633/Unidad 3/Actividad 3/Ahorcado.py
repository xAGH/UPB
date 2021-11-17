from random import randint as rd
from os import system

def globales():
    """Función que define variables globales."""

    imagenes =['''
      +---+
      |   |
          |
          |
          |
          |
    =======
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =======
    ''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =======
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =======
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =======
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =======
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =======
    ''']
    
    palabras = [
    ["YIBUTI", "VANUATU", "BRAZIL", "NAURU", "GHANA"],# Paises.
    ["POMELO", "AGUACATE", "KIWI", "ALBARICOQUE", "PACANA"],# Frutas.
    ["RHYTHM", "METAL", "FUNK", "COUNTRY", "POP"],# Géneros musicales.
    ["AVESTRUZ", "JIRAFA", "SURICATA", "PATO NEGRO", "ORCA"],# Animales.
    ["CHERRY", "LA ERA DEL HIELO", "TITANIC", "EL CONJURO", "INDIANA JONES Y EL REINO DE LA CALAVERA DE CRISTAL"]# Películas.
    ]

    return imagenes, palabras

def sys():
    """Función que límpia la pantalla"""
    system("cls")

def eleccion_categoria():
    """Función que devuelve una categoría ingresada por el usuario."""
    bandera = None

    while bandera != 0:
        try:
            sys()
            categoria = int(input("Elije una categoría: \n1. Paises.\n2. Frutas.\n3. Géneros musicales.\n4. Animales.\n5. Películas.\nElección: "))

            if categoria > 0 or categoria < 6:
                bandera = 0 

        except:
            pass
        
    return categoria-1

def eleccion_palabra(categoria, palabras):
    """Función que elije la palabra de la matriz de acuerdo a la categoría ingresada y un índice de éste aleatorio"""
    numero_indice_random = rd(0, 4)
    palabra = palabras[categoria][numero_indice_random]

    return palabra

def ocultar_palabra(palabra):
    """Función que reemplaza las letras de la palabra por '_'"""
    palabra_oculta = ''

    for i in palabra:
        if i == ' ':
            palabra_oculta += ' '

        else:
            palabra_oculta += '_'

    return palabra_oculta

def rellenar_palabra(palabra_oculta, palabra, imagenes):
    sys()
    intentos = 0
    while True:

        if intentos == 7:
            estado = 'Perdiste'
            return estado

        elif palabra_oculta == palabra:
            estado = 'Ganaste'
            return estado

        else:
            posiciones = []
            sys()
            print(imagenes[intentos], '\nPalabra: ' ,palabra_oculta)
            letra = input("Ingrese una letra o una palabra: ").upper()

        if len(letra) == 1:

            if letra in palabra:
                for i in range(len(palabra)):
                    if palabra[i] == letra:
                        posiciones.append(i)
                lista_palabra = list(palabra_oculta)
                for j in range(len(posiciones)):
                    lista_palabra[posiciones[j]] = letra

                palabra_oculta = "".join(lista_palabra)

            else:
                intentos += 1

        else:

            if letra == palabra:
                estado = "Ganaste"
                return estado
                
            else:
                intentos += 1
 
def seguir_jugando(estado, palabra):
    """Función que pregunta si se quiere seguir jugando"""
    bandera = True
    while bandera == True:
        sys()
        print(f"La palabra era: {palabra}")
        seguir_jugando = input(f"{estado}, ¿Quieres seguir jugando?\n1. SI.\n2. NO.\nElección: ")
        if seguir_jugando == '1':
            return True

        elif seguir_jugando == '2':
            return False

def main():
    """Función que se encarga de relacionar y ejecutar las otras funciones."""
    while True:
        imagenes, palabras = globales()
        categoria = eleccion_categoria()
        palabra = eleccion_palabra(categoria, palabras)
        palabra_oculta = ocultar_palabra(palabra)
        estado = rellenar_palabra(palabra_oculta, palabra, imagenes)
        seguir = seguir_jugando(estado, palabra)
        if seguir:
            pass
        else: 
            break

if __name__ == '__main__':
    main()