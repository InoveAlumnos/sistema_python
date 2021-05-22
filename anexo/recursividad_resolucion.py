#!/usr/bin/env python
'''
Funciones Recursivas [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


def factorial(numero):
    if numero > 1:
        # La línea a continuación representa
        # numero! = numero * (numero-1)!
        # Si numero fuera 4, y quisiera calcular el factorial de 4 (4!):
        # 4! = 4 * (4-1)!
        # 4! = 4 * 3!
        resultado = numero * factorial(numero-1)
        return resultado
    else:
        if numero > 0:
            return numero
        else:
            print('Error, no existe el factorial de',numero)
            return 0    # No existe el factorial de cero o un número negativo


def practica():
    print("Dominando la recursividad")

    '''
    En este ejercicio se deberá plantear el calculo del
    factorial de un número utilizando recursividad
    Primero veamos a que nos referimos con el factorial
    de un número, por ejemplo el factorial (!) de 5 sería:
    --> 5! = 5 * 4 * 3 * 2 * 1
    Mientras que el factorial de 4 sería:
    --> 4! = 4 * 3 * 2 * 1
    Tambíen se podría decir que el factorial de 5 es:
    --> 5! = 5 * 4!
    Es decir, el factorial de 5 (5!) es igual a 5 * factorial de 4 (4!)
    Pueden ver más ejemplos y de que se trata el factorial en el
    siguiente link:
    https://www.disfrutalasmatematicas.com/numeros/factorial.html

    El objetivo es calcular el factorial utilizando recursividad,
    como pueden ver en el ejemplo anterior calcular el factorial de 5
    requiere además calcular el factorial de 4, y calcular el factorial de 4
    requiere calcular el factorial de 3:
    --> 4! = 4 * 3 * 2 * 1
    --> 4! = 4 * 3!
    --> 3! = 3 * 2 * 1
    --> 3! = 3 * 2!

    Les dejamos este ejercicio para que lo piensen, luego pueden pedirnos
    la resolución del mismo a través del campus.
    '''

    resultado = factorial(4)
    print('El factorial de 4 es', resultado)


if __name__ == '__main__':
    practica()
