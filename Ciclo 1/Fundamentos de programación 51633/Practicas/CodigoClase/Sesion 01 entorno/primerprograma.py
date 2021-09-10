#ejemplos en la primera sesion
print("hola mundo")

a = "esta es una cadena de texto"
a.split()
edad = 50
print(edad)
if edad > 18 and edad <50:
    print("el joven puede comprar licor y no se puede vacunar del covid todavía")
    if edad ==27:
        print("puede todo pero no puede celebrar el cumpleaños")
elif edad > 50:
    print("el joven puede vacunarse y no se le recomienda tomar licor si se vacuna")
else:
    print("el joven NO puede comprar licor")
#esta linea permite comentar y no se ejecuta
try:
  nombreusuario = input("digite solamente su nombre:\n")
except:
  print("hubo un error tratando capturar el nombre de la persona")
print(nombreusuario)

velocidad = input("digite la velocidad del carro: \n")

velocidadreal = float(velocidad)
print(velocidadreal)
print(type(velocidadreal))


try:
    print(w)
except:
    print("algo salio mal imprimiento x")
finally:
    print("El try se ejecuto correctamente a pesar de que hubo error")