for i in range(1000000):
    try:
        centinela = int(input("\n\n1. Saludar.\n2. Es par.\n3. Promedio.\n4. Módulo.\n5. Porcentaje.\n6. Potencia.\n7. Salir.\nOpción: "))
        
        if centinela == 1:
            for i in range(2):
                try:
                    hora = int(input("Ingrese una hora: "))
                    if hora > 0 and hora < 12:
                        print("Buenos días.")
                    elif hora >= 12 and hora < 19:
                        print("Buenas tardes.")
                    elif hora >= 19 and hora <= 23:
                        print("Buenas noches.")
                    break

                except:
                    print("Error al ingresar la hora, inténtelo de nuevo.")
                

        elif centinela == 2:
            for i in range(2):
                try:
                    numero_par = int(input("Ingrese un número entero: "))
                    if numero_par % 2 == 0:
                        print(f"El número {numero_par} es par.")

                    else:
                        print(f"El número {numero_par} es impar.")

                    break
                except:
                    print("Error al ingresar el número, inténtelo de nuevo.")
                

        elif centinela == 3:
            lista_nums = []
            suma = 0
            for i in range(2):
                try:
                    cantidad = int(input("¿Cuántos números utilizará para el promedio?: "))

                    if cantidad < 1:
                        print("El valor no puede ser igual o menor a 0.")
                    

                    else:
                        for i in range(1, cantidad+1):
                            numero = float(input(f"Ingrese el número #{i}: "))
                            lista_nums.append(numero)

                        for i in lista_nums:
                            suma += i
                        promedio = suma/len(lista_nums)
                        print(f"El promedio de los {cantidad} números es: {promedio}.")
                        break

                except:
                    print("Error al obtener los datos, inténtelo de nuevo.")
                     

        elif centinela == 4:
            for i in range(2):
                try:
                    numero1 = int(input("Ingrese el número entero 1: "))
                    numero2 = int(input("Ingrese el número entero 2: "))

                    if numero2 == 0:
                        print("El número 2 no puede ser 0.")
                    

                    else:
                        modulo = numero1 % numero2
                        print(f"El módulo de {numero1} % {numero2} es {modulo}.")
                        break

                except:
                    print("Error al ingresar los números, inténtelo de nuevo.")
                

        elif centinela == 5:
            for i in range(2):
                try:
                    numero_porcentaje = float(input("Ingrese el número al cual le desea calcular el porcentaje: "))
                    porcentaje_aplicado = float(input("Ingrese el porcentaje que se le va a aplicar: "))

                    if porcentaje_aplicado < 0 or porcentaje_aplicado > 100:
                        print("Error al ingresar el porcentaje, inténtelo de nuevo.")
                    
                    
                    else:
                        porcentaje_calculo = (numero_porcentaje * porcentaje_aplicado) / 100
                        print(f"El {porcentaje_aplicado}% de {numero_porcentaje} es {porcentaje_calculo}.")
                        break

                except:
                    print("Error al ingresar los datos, inténtelo de nuevo.")
                

        elif centinela == 6:
            for i in range(2):
                try:
                    numero_potencia = float(input("Ingres el número a potenciar: "))
                    potenciacion = float(input("Ingrese la potenciación: "))
                    potenciacion_calculo = numero_potencia ** potenciacion
                    print(f"{numero_potencia} potenciado al {potenciacion} es igual a {round(3,potenciacion_calculo)}.")
                    break

                except:
                    print("Error al ingresar los datos, inténtelo de nuevo.")
                
        
        elif centinela == 7:
            print("Saliendo...")
            break
        
        else:
            print("Entrada inválida.")
        

    except:
        print("Error al ingresar la opción, inténtelo de nuevo.")
    