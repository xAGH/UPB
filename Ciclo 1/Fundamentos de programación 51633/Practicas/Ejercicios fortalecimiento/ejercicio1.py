# Se inicia definiendo la lista con los nombres.
nombres = ['Alejandro', 'Adriana', 'Michael', 'Jhon', 'Julen']

# Se define una lista vacia que almacenará los índices donde se encuentre la vocal a.
letra_a = []

# Se recorre cada uno de los elementos de la lista nombres.
for i in nombres:
    nombre = [f"Nombre: {i}, indices de 'a' en posición: "]
    for j in range(len(i)):
        if i[j].lower() == "a":
            nombre.append(j)
    if len(nombre) == 1:
        nombre.append("N/A")
    letra_a.append(nombre)

for i in letra_a:
    print('\n', i)