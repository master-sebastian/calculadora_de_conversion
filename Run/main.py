import sys
import os

base_path = os.path.dirname(os.path.abspath(__file__)).rsplit(os.sep, 1)

sys.path.insert(0, os.path.join(base_path[0], "Librery"))

from conversores import obtener_dato_por_consola

print(obtener_dato_por_consola())