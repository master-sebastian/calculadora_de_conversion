#Ultima actualizacion de factor de conversion 16/07/2022 
import os
import json

base_path = os.path.dirname(os.path.abspath(__file__)).rsplit(os.sep, 1)

with open(os.path.join(base_path[0], "db", "JSON", "nombre_dolar.JSON")) as f:
   nombre_dolar = json.load(f)

#Configuración flexible agragando nuevo elemento al arreglo
with open(os.path.join(base_path[0], "db", "JSON", "coleccion_money.JSON")) as f:
   config_coleccion_de_monedas = json.load(f)

def __conversion_moneda(tipo_moneda):
    existe_moneda = False
    for moneda_actual in config_coleccion_de_monedas: 
        if(str(moneda_actual["id"]) == tipo_moneda):
            try:
                cantidad = float(input("Ingrese la cantidad a convertir: "))
            except:
                print("Cantidad no es validad")
                exit()
            if cantidad < 0:
                print("Cantidad no valida")
                exit()
            conversion = cantidad * moneda_actual["factor_de_conversion_dolar"]
            mensaje = moneda_actual["nombre"][("plural", "singular")[cantidad == 1]].replace("[cantidad]", str(cantidad)) + " equivale a " + nombre_dolar[("plural", "singular")[conversion == 1]].replace("[cantidad]", str(conversion))
            existe_moneda = True
            break
    if not existe_moneda:
        mensaje = "Ese tipo de moneda no esta configurada en este equipo"
    return mensaje

def obtener_dato_por_consola():
    print("Monedas posibles a convertir:")
    for moneda_actual in config_coleccion_de_monedas:
        print(str(moneda_actual["id"]) + " - "+ moneda_actual["tipo"])    
    
    tipo_moneda = input("Ingrese el tipo de modena que desea convertir: ")
    return __conversion_moneda(tipo_moneda) 



    
    