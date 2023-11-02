import problema1
from alumnos import alumnos
'''
hasta ahora hemos
trabajado con variables
que permiten almacenar
 un unico valor
 '''

edad = 12

altura = 1.79

nombre = "juan"

estado = True

print("hello world")

'''
En python podemos 
usar una variable
que alamcena  una
coleccion de datos 
y luego accederla usando
 un subindice'''

#lista de enteros
lista1 = [10, 5, 3, 9]

#lista de decimales
lista2 = [1.78, 2.66, 1.55, 89.4]

#lista de string
lista3 = ["lunes", "martes", "miercoles"]

#lista elementos de distinto tipo
lista4 = ["juan", 45, 1.92, False]


if __name__ == '__main__':

    print(len(lista1))
    print(len(lista2))
    print(len(lista3))
    print(len(lista4))

    print()
    print(lista1, lista2, lista3, lista4)

    print()

    problema1.sumar_5_enteros()
    
    print()

    alumnos()

