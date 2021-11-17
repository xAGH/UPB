while True:
    try:
        IVA = 1.19
        precio = float(input("Ingrese el precio del producto: $"))
        paga = float(input("Ingrese con cuánto paga: $"))
        precio_final = precio * IVA
        devuelta = paga - precio_final

        if precio_final > paga:
            print("No te alcanza para comprar el producto.")

        elif precio_final < 0:
            print("El valor no puede ser negativo.")

        else:
            precio_final = round(precio_final, 2)
            print(f"EL precio a pagar es ${precio_final}")
            print(f"Pagó ${paga}")
            print(f"Sus devueltas son ${devuelta}")

        break

    except:
        print("Ingrese un número positivo.")