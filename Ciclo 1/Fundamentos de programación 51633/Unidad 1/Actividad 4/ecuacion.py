# Se inicia con las incógnitas desglozadas de acuerdo al método Gauss 
d = int((54/37) // (27/17))

c = int((-23 * d - 65) / -27)

b = int(-11 * c + 3 * d + 20)

a = 2 * b + 1 * c - 2 * d - 11

# Se define una ecuación de cuarto grado con cuatro incognitas.
ecuacion_4to_grado_1 = [[(-2 * a + 3 * b - c + 2 * d)],
                     [(3 * a - b +  3 * c - d) / 2],
                     [(-a + 2 * b + 5 * c - 2 * d)], 
                     [(6 * a - 3 * b + c + d)]]
# Se imprime el resultado de cada operación en la ecuación de cuarto grado.
print("1ra prueba")
for i in ecuacion_4to_grado_1:
    print(i)


# Se desglozan las incógnitas por medio del método Gauss
d = int((54/37) // (27/37))

c = int((-23 * d - 65) / -37)

b = int(-11 * c + 6 * d + 20)

a = 2 * b + 5 * c - 2 * d - 11

# Se retoma la ecuación con las incógnitas halladas.
ecuacion_4to_grado_2 = [[(-2 * a + 3 * b - c + 2 * d)],
                     [(3 * a - b +  3 * c - d) / 2],
                     [(-a + 2 * b + 5 * c - 2 * d)], 
                     [(6 * a - 3 * b + c + d)]]

# Se imprime el resultado de cada operación en la ecuación de cuarto grado.
print("2da prueba")
for i in ecuacion_4to_grado_2:
    print(i)