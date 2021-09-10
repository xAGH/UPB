#manejo del while
n = 5
while n>0:
    print(n)
    n = n-1
print("boom")

while True:
    try:
        nombre = input("digite su nombre:    ")
        if nombre:
            break
    except:
        print("algo paso mal con la captura del nombre")
print("finalizo el while infinito")