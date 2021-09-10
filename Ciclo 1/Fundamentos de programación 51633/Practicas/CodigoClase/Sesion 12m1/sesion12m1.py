def suma(ma, mb):
    '''
    Function that sums two matrix inputs of the same size 
    '''
    mc = []
    for i in range(0,len(ma)):
        col = []
        for j in range(0,len(ma[0])):
            col.append(ma[i][j] + mb[i][j])
        mc.append(col)
    return mc

def resta(ma, mb):
    '''
    Function that substracts two matrix inputs of the same size 
    '''
    mc = []
    for i in range(0,len(ma)):
        col = []
        for j in range(0,len(ma[0])):
            col.append(ma[i][j] - mb[i][j])
        mc.append(col)
    return mc

def escalarmul(ma, mb):
    '''
    Function that multiplies by scalar a single matrix'''
    mc = []
    for i in range(0,len(ma)):
        col = []
        for j in range(0,len(ma[0])):
            col.append(ma[i][j] * mb)
        mc.append(col)
    return mc

a = [[2,3,4],[5,6,7]]
b = [[6,6,6],[7,7,7]]

c =suma(a,b)
print(c)

def imprimirpantalla(mensaje, nombre='el Matius'):
    print(mensaje+" atte: "+nombre)

imprimirpantalla("Este es mi primer mensaje con atributo por defecto")
imprimirpantalla("este no es por defecto","leo")

imprimirpantalla(nombre="Pepe le buu",mensaje="mi mama me mima")



print(suma.__doc__)


import random

def generadormatriz():
    mv = []
    for i in range(0,3):
        mv.append([0]*4)
    for col in range(0,len(mv)):
        for fil in range(0,len(mv[0])):
            mv[col][fil] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    return mv
a = generadormatriz()
print(a)

#escribir en archivo la imagen
try:
    archivo = open("data.txt",'w')
    for col in range(len(a)):
        for fil in range(len(a[0])):
            datafile = a[col][fil]
            archivo.write(str(datafile))
    archivo.close()    
except:
    print("error en escritura de archivo")