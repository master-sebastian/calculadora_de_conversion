import sys, json, random
import os
import csv

base_path = os.path.dirname(os.path.abspath(__file__)).rsplit(os.sep, 1)

sys.path.insert(0, os.path.join(base_path[0], "Librery", "Conversion"))
sys.path.insert(0, os.path.join(base_path[0], "Librery", "Http"))

with open(os.path.join(base_path[0], "config.JSON")) as f:
   config_json = json.load(f)

from conversores import obtener_dato_por_consola
from ClienteApiMethodoGET import solcitudMetodoGetRespuestaJSON

clientes = []
with open(os.path.join(base_path[0], "db", "CSV", "Clientes.csv"), 'r') as f:
    for cliente in f:
        clientes.append(cliente.replace('\n','').split(";"))

sumatoria = 0

#Clientes en CSV
for cliente in clientes:
    print("Nombre de cliente: ", cliente[1])
    print("Referencia: ", cliente[0])
    response = obtener_dato_por_consola(cliente[2], cliente[3])
    if response != None:
        print(response["mensaje"])
    if response != None and response["conversion"] != None:
        sumatoria += response["conversion"]

#Clientes en API
for cliente in solcitudMetodoGetRespuestaJSON(config_json["api_users"]):    
    print("Nombre de cliente: ", cliente["name"])
    print("id: ", cliente["id"])
    tipo_moneda = random.sample(range(1, 5, 1), 1)[0]
    cantidad = random.sample(range(config_json["min_money"], config_json["max_money"] + 1, 100), 1)[0]
    response = obtener_dato_por_consola(tipo_moneda, cantidad)
    if response != None:
        print(response["mensaje"])
    if response != None and response["conversion"] != None:
        sumatoria += response["conversion"]

sumatoria = int(sumatoria * 100)/100

print()
print()
print("Dolares Recolectados: "+ str(sumatoria))