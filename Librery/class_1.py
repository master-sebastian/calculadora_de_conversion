#Ultima actualizacion de factor de conversion 16/07/2022 
nombre_dolar =  {
    "plural": "[cantidad] dolares",
    "singular": "un dolar"
}


#Configuración flexible agragando nuevo elemento al arreglo
config_coleccion_de_monedas = [
    {
        'id': 1,
        "tipo": "Modena chilena",
        'nombre': {
            "plural": "Los [cantidad] pesos chilenos",
            "singular": "Un peso chileno"
        },
        'factor_de_conversion_dolar': 0.0010
    },
    {
        'id': 2,
        "tipo": "Modena colombiana",
        'nombre': {
            "plural": "Los [cantidad] pesos colombianos",
            "singular": "Un peso colombiano"
        },
        'factor_de_conversion_dolar': 0.00022
    },
    {
        'id': 3,
        "tipo": "Modena argentina",
        'nombre': {
            "plural": "Los [cantidad] pesos argentinos",
            "singular": "Un peso argentino"
        },
        'factor_de_conversion_dolar':  0.0078
    },
    {
        'id': 4,
        "tipo": "Modena mexicana",
        'nombre': {
            "plural": "Los [cantidad] pesos mexicanos",
            "singular": "Un peso mexicano"
        },
        'factor_de_conversion_dolar': 0.049
    }
]

def conversion_v1(tipo_moneda):
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
if __name__ == "__main__":

    print("Monedas posibles a convertir:")
    for moneda_actual in config_coleccion_de_monedas:
        print(str(moneda_actual["id"]) + " - "+ moneda_actual["tipo"])    
    
    tipo_moneda = input("Ingrese el tipo de modena que desea convertir: ")
    print(conversion_v1(tipo_moneda)) 



    
    