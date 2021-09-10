#ciclos asosciados a listas

cuadrados = []
for x in range(1,40):
    cuadrados.append(x**2)

print(cuadrados)

cuadrados2 = [(2*y-1)**2 for y in range(1,40)]

print(cuadrados2)

silla = {'color':'cafe','material':'madera','patas':4}
print(silla)
silla['espaldar']=False
print(silla)

arreglo_llaves = []
arreglo_valores = []
for llaves,valores in silla.items():
    print("la llave " + llaves +" tiene el valor: " +str(valores))
    arreglo_llaves.append(llaves)
    arreglo_valores.append(valores)
print(arreglo_llaves)
print(str(arreglo_valores))

for nombre in silla.keys():
    print("el valor del parametros es:" + str(silla[nombre]))