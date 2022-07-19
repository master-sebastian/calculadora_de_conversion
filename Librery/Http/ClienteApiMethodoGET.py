import requests

def solcitudMetodoGetRespuestaJSON(url):
    response = requests.get(url)
    return response.json()