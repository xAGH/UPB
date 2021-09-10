def imprimir_mensaje():
    print("hola mundo")

def imprimir_mensaje_personalizado(mensaje):
    print(str(mensaje))

def cuadradodeunnumero(numero_entrada):
    return numero_entrada * numero_entrada

imprimir_mensaje()
imprimir_mensaje()
imprimir_mensaje()

imprimir_mensaje_personalizado("esta funcion imprime en pantalla")
imprimir_mensaje_personalizado("otra vez mandando un mensaje")
imprimir_mensaje_personalizado("de nuevo por aca imprimiendo un mensaje")

print(cuadradodeunnumero(3))
print(cuadradodeunnumero(5))

a = cuadradodeunnumero(7)
print(a)

def etapa_covidvacuna(edad):
    """
    esta funcion te va a decir a que etapa del proceso de vacunación
    en Colombia pertenece.
    el parámetro de entrada es un entero de la edad de la persona que esta consultando
    La función devuelve un string con la etapa de la vacunacion
    """ 
    if edad > 60:
        return "etapa 1"
    elif (edad <= 60) and (edad > 55):
        return "etapa 2"
    elif edad <= 55 :
        return "etapa 3"

usuario1 = etapa_covidvacuna(34)
usuario2 = etapa_covidvacuna(57)

print("el usuario 1 pertenece a: ",usuario1)
print("el usuario 2 pertenece a: ",usuario2)

def cambiodevariables(a,b):
    return b, a
m = 2
n = 3
x, y = cambiodevariables(m,n)
print("el valor de x es:", x)
print("el valor de y es:", y)

w = 0
z = 9
w, z = cambiodevariables(w,z)
print("el valor de w es:", w)
print("el valor de z es:", z)

a = -5
b = 7
a, b = cambiodevariables(a, b)
print("el valor de a es:", a)
print("el valor de b es:", b)

def sumarmatrices(ma, mb):
    mc = [[0]*len(mb[0])]*len(mb)    
    for i in range(0,len(ma)):
        for j in range(0,len(mb[0])):
            mc[i][j] = ma[i][j] + mb[i][j]
            print("el valor de i es: ",i)
            print("el valor de j es: ",j)
            print("la suma es: ", mc[i][j])
            print("matriz de salida en el ciclo interno: ", mc)
        print("matriz de salida en el ciclo externo: ", mc)
    return mc

def sumarmatrices2(ma, mb):
    mc = []    
    for i in range(0,len(ma)):
        col=[]
        for j in range(0,len(mb[0])):
            col.append(ma[i][j] + mb[i][j])
        mc.append(col)
    return mc


matriza = [[2,4,6],[3,5,7]]
matrizb = [[7,7,7],[9,9,9]]
matrizc = sumarmatrices(matriza, matrizb)
print(matrizc)

matrizc2 = sumarmatrices2(matriza, matrizb)
print(matrizc2)

def ecuacion1(a,b,c,d):
    return ((a+b)/c)*d
print("salida de la ecuacion1: ",ecuacion1(3.5,7.4,-2,2.6))

def saludos(*args):
    for elementos in args:
        print("Hola ",elementos)

saludos('pepe')
saludos('juan', 'alvaro','lina','ana')

def nombrecompleto(nombre,segundonombre, apellido, segundoapellido):
    """
    Esta funcion concatena el nombre completo de una persona, con su segundo nombre, apellido y apellido secundario"""
    nombre_total = nombre + " " + segundonombre + " " + apellido + " " +segundoapellido
    return nombre_total

print(nombrecompleto("emilio","de jesus","alvarez","castro"))

saludos("alejandro",45,67.7)