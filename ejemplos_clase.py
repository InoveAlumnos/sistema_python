# Sistema [Python]
# Ejemplos de clase
# ---------------------------
# Autor: Inove Coding School
# Version: 2.0

# Descripcion:
# Programa creado para mostrar ejemplos prácticos de los visto durante la clase

import os


def excepciones(nombre_archivo):
    # Una excepcion ocurre cuando el sistema falla
    # de tal forma que Python no puede contener la falla.
    # Esto produce que el programa deba detenerse sin poder continuar
    # con su ejecución.

    # Veamos una falla tipica matemática, la division por cero:
    # Al intentar dividir un número por cero el sistema no puede
    # ejecutar la división.

    try:
        division = 3 / 0
    except:
        print('No existe la division por cero')

    # Otra clásica excepción es intentar abrir un archivo que no existe
    # Cuando esto ocurre el sistema falla y se detiene el programa al
    # no poder encontrar el archivo.

    try:
        fi = open(nombre_archivo, 'r')
    except:
        print('No se encuentra el archivo', nombre_archivo)

    return


def existencia_archivo(nombre_archivo):
    # Para ver si un archivo o directorio existe,
    # y si tengo los permisos para accederlo
    # puedo utilizar el método "access" del módulo "os":
    # Si el sistema es capaz de acceder al archivo/directorio
    # (os.F_OK) quiere decir que puedo utilizar ese archivo.

    if os.access(nombre_archivo, os.F_OK) is False:
        print('No se pudo acceder a', nombre_archivo)

    if os.access('inove.jpg', os.F_OK) is False:
        print('No se pudo acceder a', nombre_archivo)

    return None


def directorios(nombre_archivo):
    # Veamos como con el método "path" podemos acceder
    # a la ubicación real de donde se encuentra el archivo
    # en cuestión que estamos intentando abrir.
    # Supongamos que tenemos la certeza de que el archivo
    # se encuentra en el mismo directorio que el este programa.

    # Comenzamos obteniendo la dirección "path" de donde
    # se encuentra este programa "file":
    direccion_script = os.path.realpath(__file__)
    print("Direccion al script:", direccion_script)

    # Como el "path" nos tra el nombre del archivo además
    # de su dirección, atraemos unicamente la dirección
    # de donde se encuentra ubicado:
    path = os.path.dirname(direccion_script)
    print("Directorio del proyecto:", path)

    # Ahora creamos nuestro "path" como la union (join)
    # de la dirección de la carpeta de donde se ejecuta este programa
    # y el nombre del archivo que debería estar incluido en esa carpeta:
    directorio_archivo = os.path.join(path, nombre_archivo)
    print('Directio del archivo:', directorio_archivo)

    # Intento de acceder al archivo como si el programa se hubiera ejecutado
    # en el mismo directorio donde está el archivo en cuestión a acceder:
    if os.access(nombre_archivo, os.F_OK) is True:
        print('1* Se encontró el archivo por nombre:', nombre_archivo)

    # Si el archivo existe deberíamos poder acceder a este
    # sin importar desde donde nos encontremos ejecutando el programa.
    # Para eso utilizamos la ruta completa junto con el nombre:
    if os.access(directorio_archivo, os.F_OK) is True:
        print('2* Se encontró el archivo por path:', nombre_archivo)
    
    return


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    nombre_archivo = 'nombre.txt'

    excepciones(nombre_archivo)
    existencia_archivo(nombre_archivo)
    directorios('inove.jpg')
