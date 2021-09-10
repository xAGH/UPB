def funcion(b):
    a = b * 2
    return a



salida = lambda x: x*2
print(salida(3))
#FILTER
#ejemplo de filtro en python

lista = [1,2,3,4,6,8,11,3,12]
nuevalista = list(filter(lambda i:(i%2==0),lista))

print(lista)
print(nuevalista)

lista = [1,2,3,4,6,8,11,3,12]
pares = []
for i in lista:
    if i%2==0:
        pares.append(i)
print(pares)

listabase = [i for i in range(0,100)]
mul_5 = list(filter(lambda x:(x%5==0),listabase))
print(mul_5)

#MAP 
a = [1,2,3,4,5,6,0,9,8]
b = [6,7,8,9,10]

c = []
for i in range(0,5):
    c.append(a[i]+b[i])

d = list(map(lambda x, y: x+y, a, b))
print(a)
print(b)
print(c)
print(d)

#ordenar una lista con el parametro key - requiere un lambda
listausers = [{'nombre':'leo','edad':40},{'nombre':'pepe','edad':42},{'nombre':'martha','edad':21}]
print(listausers)
listausers.sort(key= lambda k:k['edad'])
print(listausers)