#ejemplo para solucionar orden de Lista Danna

print("-"*50)
print("Menu principal")
print("-"*50)
print("  opcion 1: lavar papas")
print("  opcion 2: lavar peras")
print("  opcion 3: lavar manzanas")
print("  opcion 4: lavar guayabas")
print("  opcion 5: lavar sandias")
print("-"*50)

listamenu = ["opcion de usuario ", "opción de programador", "opcion salir"]

def imprimirmenuprincipal(listam):
    contador = 1
    for elementos in listam:
        print("opción ",str(contador),elementos)
        contador = contador + 1

imprimirmenuprincipal(listamenu)
print(listamenu)
listamenu = ["opicion de programador", "quejas", "opcion usuario", "opcion salir"]
imprimirmenuprincipal(listamenu)

variable= -75.666678786
print("texto {:.3f}".format(variable))


a = open("1info.txt","r")
data = a.read()
print(data)