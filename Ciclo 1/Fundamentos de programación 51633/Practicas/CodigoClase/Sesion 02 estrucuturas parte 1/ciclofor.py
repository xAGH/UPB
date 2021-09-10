# Ejemplos de un ciclo for
# for year in range(2015,2021):
#   print("el año del reporte es",str(year))

listadeestudiantes = ["adriana","alejandro","luis","francisco"]
for estudiante in listadeestudiantes:
    print("enviando el correo al estudiante: ",estudiante)
print("Correos enviados")

for i in range(0,4):
    print(listadeestudiantes[i])

contador = 0
for valor in [3, 41, 56 , 78, 88, 13]:
    print(valor)
    contador = contador + 1
print(contador)
