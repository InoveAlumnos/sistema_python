#!/usr/bin/env python
'''
Extra [Python]
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

import sys
import os


def excepciones(nombre_archivo):
    # Una excepcion ocurre cuando el sistema falla
    # de tal forma que Python no puede contener la falla.
    # Veamos una falla tipica matemática, la division por cero:
    try:
        division = 3 / 0
    except:
        print('No existe la division por cero')
        division = sys.float_info.max

    # Otra clásica excepción es intentar abrir un archivo que no existe
    try:
        fi = open(nombre_archivo, 'r')
    except:
        print('No se encuentra el archivo', nombre_archivo)
        fi = None

    return


def existencia_archivo(nombre_archivo):
    if os.access(nombre_archivo, os.F_OK) is False:
        print('No se pudo acceder a', nombre_archivo)

    if os.access('inove.jpg', os.F_OK) is False:
        print('No se pudo acceder a', nombre_archivo)

    return None


def directorios(nombre_archivo):
    direccion_script = os.path.realpath(__file__)
    print("Direccion al script:", direccion_script)
    path = os.path.dirname(direccion_script)
    print("Directorio del proyecto:", path)

    directorio_archivo = os.path.join(path, nombre_archivo)

    print('Directio del archivo:', directorio_archivo)

    if os.access(nombre_archivo, os.F_OK) is True:
        print('1* Se encontró el archivo por nombre:', nombre_archivo)

    if os.access(directorio_archivo, os.F_OK) is True:
        print('2* Se encontró el archivo por path:', nombre_archivo)
    
    return


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    '''
    Como agregar argumentos al lanzador
    "windows": {
                "args": ["casa.txt"]
              }
    '''

    print(sys.argv)
    if len(sys.argv) > 1:
        nombre_archivo = str(sys.argv[1])
    else:
        nombre_archivo = 'nombre.txt'  # Nombre por defecto

    excepciones(nombre_archivo)
    existencia_archivo(nombre_archivo)
    directorios('inove.jpg')
