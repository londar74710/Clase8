def sumar_5_enteros():
    lista = []
    contadorWhile = 0
    tamano = 5
    suma = 0

    while contadorWhile < tamano:
        # Agregar numeros a la lista.
        lista.append(int(input("Ingrese numero " + str(contadorWhile+1) + ": ")))
        contadorWhile += 1

    contadorWhile = 0
    while contadorWhile < tamano:
        suma += lista[contadorWhile]
        contadorWhile += 1

    print("Los elementos de la lista son:")
    for numero in lista:
        print(numero,end=", ")

    print("\nLa suma de todos sus elementos es:")
    print(suma)