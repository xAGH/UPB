from random import randint

letra = {'1':['Mami ', 'Gata ', 'Perra ', 'Zorra ', 'Chica '], '2':['yo quiero ', 'vamos a ', 'ya voy a ', 'yo quiero ', 'yo vengo a '], '3':['castigarte ', 'cogerte ', 'encenderte ', 'darte ', 'azotarte '], '4':['duro ', 'rápido ', 'lento ', 'suave ', 'fuerte '], '5':['hasta que salga el sol ', 'toda la noche ', 'hasta el amanecer ', 'hasta mañana ', 'todo el día '], '6':['sin miedo ', 'sin anestesia ', 'en el piso ', 'contra la pared ', 'sin compromiso ']}

cancion = ''

for i in range(1, 7):
    numero = randint(0, 4)
    seleccion = letra[str(i)][numero]
    cancion = cancion + seleccion

print('\n', cancion, '\n')