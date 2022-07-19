import sys
import os
import csv

base_path = os.path.dirname(os.path.abspath(__file__)).rsplit(os.sep, 1)

sys.path.insert(0, os.path.join(base_path[0], "Librery"))

from conversores import obtener_dato_por_consola

clientes = []
with open(os.path.join(base_path[0], "db", "CSV", "Clientes.csv"), 'r') as f:
    for cliente in f:
        clientes.append(cliente.replace('\n','').split(";"))

for cliente in clientes:
    print(obtener_dato_por_consola(cliente[2], cliente[3]))