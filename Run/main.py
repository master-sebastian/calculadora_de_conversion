import sys, json, random
import os
import csv
from datetime import datetime
base_path = os.path.dirname(os.path.abspath(__file__)).rsplit(os.sep, 1)

sys.path.insert(0, os.path.join(base_path[0], "Librery", "Conversion"))
sys.path.insert(0, os.path.join(base_path[0], "Librery", "Http"))
sys.path.insert(0, os.path.join(base_path[0], "Librery", "Reportes"))

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

lista_cliente_generados = []

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
    lista_cliente_generados.append({
        "nombre": cliente["name"],
        "id": cliente["id"],
        "cantidad": cantidad,
        "tipo_moneda":tipo_moneda,
        "response":response
    })

sumatoria = int(sumatoria * 100)/100

print("\n\nDolares Recolectados: "+ str(sumatoria))

dataset_folder = os.path.join(base_path[0], "dataset_api")
if not os.path.exists(dataset_folder):
    os.makedirs(dataset_folder)

dataset_folder = os.path.join(dataset_folder, "dataset_"+datetime.now().strftime('%Y%m%d%H%M%S')+".JSON")
with open(dataset_folder, 'w') as out:
    out.write(json.dumps(lista_cliente_generados, indent=4))


from PdfHtml import crearPDFPorHTML, obtenerPlantilla1

report_pdf_folder = os.path.join(base_path[0], "Reports", "pdf")

crearPDFPorHTML(
    html= obtenerPlantilla1(
        titulo="Clientes consultados por el API REST",
        cuerpo="Estamos bien ahora mismo",
        titulo_lista="Lista de vendedores",
        lista=["Sebastian", "Camilo"],
        titulo_tabla="Lista de clientes",
        tabla=[ ["Id del cliente", "Nombre del Cliente", "Cantidad", "Tipo" ,"conversión"] ] + [ [cliente["id"], cliente["nombre"], cliente["cantidad"], cliente["tipo_moneda"], "{:.2f}".format(cliente["response"]["conversion"])] for cliente in lista_cliente_generados]
    ),
    ruta_destino=os.path.join(report_pdf_folder, "report_"+datetime.now().strftime('%Y%m%d%H%M%S')+".pdf")
)
