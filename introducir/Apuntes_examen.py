import sys 
sys.path.insert(0, "C:\Users\oscar\OneDrive\Documentos\algoritmos\oo")


'''Es una lista de directorios/carpetas donde Python busca los módulos cuando 
realizamos un import'''
#Lo necesitamos si o si para el examen.
#sería sys.path(0,la ruta del archivo)
#va en el main, y sin ponerlo es imposible que funcione.

#NO USAR FOR de ahora en adelante.

#en los bucles que crearemos. en else tenemos que llamar a la propia
#función creada y hacerle cosas.

#no usaremos apenas print, usaremos el return.

"""
Módulo que gestiona todas las funcionalidades de introducción de datos
"""

from numero import (
    solicitar_introducir_numero,
    solicitar_introducir_numero_extremo,
)

from buleano import (
    solicitar_introducir_si_o_no,
    solicitar_introducir_verdadero_o_falso,
)

from cadena import (
    solicitar_introducir_cadena,
    solicitar_introducir_char,
    solicitar_introducir_letra,
    solicitar_introducir_palabra,
)

#para que funcione y se importe solo hay que quitar el punto.