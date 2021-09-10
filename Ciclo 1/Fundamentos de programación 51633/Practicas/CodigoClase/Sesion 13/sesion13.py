#llamado de bibliotecas
import math
import os
import numpy as np
#declaracion de variables globales

#declaracion de funciones
#funcion suma
def suma(*sumandos):
    """
    devuelve la suma de los elementos entregados a la fucion"""
    suma = 0
    for elemento in sumandos:
        suma = suma + elemento
    return suma
#funcion resta
def resta(n,m):
    """
    resta a n el valor de m """
    return n-m
#funcion multiplicacion
def multiplicacion(a,b):
    """
    devuelve la multiplicacion entre a y b"""
    return a*b
#fucnion division
def division(c,d):
    """devuelve la división entre c y d"""
    if d == 0:
        return "infinito"
    else:
        return c/d
#funcion modulo
def modulo(m,n):
    """devuelve el modulo m % n"""
    if n==0:
        return "division por cero"
    else:
        return m%n
#funcion de porcentaje
def porcentaje(r,porcentaje):
    """calcula el porcentaje de r"""
    return (r*porcentaje)/100
#funcion potenciacion al cuadrado
def cuadrado(m):
    """
    devuelve el cuadrado de m"""
    return m*m
#funcion potenciacion a la n
def potencia(m,n):
    """devuelve m a la n"""
    return m**n
#funcion para la raiz cuadrada
def raizcuadrada(n):
    """retorna la raiz cuadrada de n"""
    return math.sqrt(n)
#declaracion de funcion principal
def funcionprincipal():
    print('-'*50)
    print("prueba de suma:")
    print("la suma de 5,6 y 7 es: ",suma(5,6,7))
    print('-'*50)
    print("prueba de resta:")
    print("la resta de 5 y 6 es: ",resta(5,6))
    print('-'*50)
    print("prueba de multiplicacion:")
    print("la multiplicacion de 15,3 es: ",multiplicacion(15,3))
    print('-'*50)
    print("prueba de division:")
    print("la division de 7 y 0 es: ",division(7,0))
    print('-'*50)
    print("prueba de modulo:")
    print("El modulo de 27 y 6 es: ",modulo(27,6))
    print('-'*50)
    print("prueba de cuadrado:")
    print("el cuadrado de 57 es: ",cuadrado(57))
    print('-'*50)
    print("prueba de potenciacion:")
    print("el valor de 8 elevado a la 5 es: ",potencia(8,5))
    print('-'*50)
    print("prueba de porcentaje:")
    print("el 130 porciento de 14 es: ",porcentaje(14,130))
    print('-'*50)
    print("prueba de librerias:")
    print("usando la funcion coseno de la libreria math: ")
    print("coseno de 3.1416 radianes (cos(pi)) es: ", math.cos(3.1416))
    print('-'*50)
    print("prueba de raiz cuadrara:")
    print("la raiz cuadrada de 144 es: ",raizcuadrada(144))
    print('-'*50)
    print("usando el valor de pi desde la librearia numpy:")
    print("el valor de pi es: ",str(np.pi))

#lanzador de la funcion pricipal
if __name__ == '__main__':
   funcionprincipal()
