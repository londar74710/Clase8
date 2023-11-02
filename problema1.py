def sumar_5_enteros():
    #definicion de variable
    lista = []
    contadorwhile = 0
    tamaño = 5
    suma = 0


    #ingresar los numeros
    while contadorwhile < tamaño:
        lista.append(int(input("Ingrese numero" + str(contadorwhile + 1) + ": ")))
        contadorwhile += 1

    #sumar  los numeros
    contadorwhile = 0
    while contadorwhile < tamaño:
        suma += lista[contadorwhile]
        contadorwhile += 1

    print("los elementos de la lista son:")
    for numero in lista:
        print(numero, end=', ')

    print("\nla suma de todos sus elementos es:")
    print(suma)
