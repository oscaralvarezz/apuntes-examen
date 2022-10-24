from importlib.resources import path
import sys
sys.path(0,path) #sys.path.append

"""
Módulo que sirve solo para iniciar el juego
"""

from juego import jugar

if __name__ == "__main__":
    jugar()
    