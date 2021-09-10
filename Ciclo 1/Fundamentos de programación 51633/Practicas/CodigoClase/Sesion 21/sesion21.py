import math
#ejemplo de calculo de distancias de coordenadas

def funciondistancia(long_1, lat_1, long_2, lat_2):
    radiotierra = 6372.795477598
    distancia = 2*radiotierra*math.asin(math.sqrt(math.sin((lat_2-lat_1)/2)**2+math.cos(lat_1)*math.cos(lat_2)*math.sin((long_2-long_1)/2)**2))
    return distancia

origen_latitud = 4.5676
origen_longitud = -75.68888
estaciones_latitudes = [-75.777, -76.789, -77.6787]
estaciones_longitudes = [5.67, 4.7897, 5.01234]

for i in range(0,3):
    dis = funciondistancia(origen_longitud,origen_latitud,estaciones_longitudes[i],estaciones_latitudes[i])
    print("la distancia es:   ",str(dis))


