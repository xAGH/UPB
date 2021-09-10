class Persona:
    """ Ejemplo de crear una clase que crea objetos tipo persona"""
    def __init__(self,nombredeentrada,edaddeentrada):
        self.nombre = nombredeentrada
        self.edad = edaddeentrada
        self.peso = 65.0
    def comer(self):
        self.peso = self.peso + 0.5
    def iralbano(self):
        self.peso = self.peso - 0.5
    def preguntaredad(self):
        return self.edad
    

p1 = Persona("Juan",36)
p2 = Persona("Lupita",21)
print("lugar de ram donde esta el objeto p1: ",id(p1))
print("lugar de ram donde esta el objeto p2: ",id(p2))
print("accediendo al atributo nombre de p1: ",p1.nombre)
print("accediendo al atributo edad de p1: ",p1.edad)
print("accediendo al atributo peso de p1: ",p1.peso)
p1.nombre = "Juanito"
print("accediendo al atributo nombre de p1: ",p1.nombre)
p1.comer()
p1.comer()
p1.comer()
p1.iralbano()
print("accediendo al atributo peso de p1: ",p1.peso)
print("P1, ¿que edad tienes?: ",p1.preguntaredad())
px = p1
print("esta es la direccion de px: ",id(px))
print("esta es la direccion de p1: ",id(p1))
print("peso de p1: ",p1.peso)
px.peso = 55
print("peso de p1: ",p1.peso)


print("-"*50)
print("Ejercicio de introduccion para el proyecto")
print("ejercicio 1, capturar los datos de la base de datos mundial")

import pandas as pd
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context

todoslosdatos = pd.read_csv('~/Downloads/owid-covid-data.csv')
datosColombia = todoslosdatos[todoslosdatos['iso_code'].isin(['COL'])]

fechas = datosColombia['date'].tolist()
print(type(fechas))

nuevasmuertes = datosColombia['new_deaths'].tolist()
print(type(nuevasmuertes))