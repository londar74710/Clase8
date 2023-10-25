import problema1
from alumnos import alumnos

edad = 12
altura = 1.75
nombre = "Juan"
estado = True

lista1 = [10, 2, 3, 4]
lista2 = [1.72, 1.54, 1.23, 1.64]
lista3 = ["lunes", "martes", "miercoles"]
lista4 = ["juan", 45, 1.92, False]




if __name__ == '__main__':
    # Mostrar cantidad de elementos en las listas
    print(len(lista1))
    print(len(lista2))
    print(len(lista3))
    print(len(lista4))

    #Establecer un espacio
    print()
    # Mostar elementos de la lista
    print(lista1)
    print()
    # Cambiar valores de listas
    lista1[0] = 1
    print(lista1)

    print()
    # Mostrar un valor exacto de lista, siempre inicia en 0 el primer elemento.
    print(lista1[3])

    print()

    problema1.sumar_5_enteros()

    print()

    alumnos()
